#!/bin/bash
# HTML to Markdown Converter Script
# 
# This script automatically converts HTML files to GitHub-flavored Markdown (GFM),
# commits the new .md files, and removes the original .html files.
#
# Features:
# - Detects if the last commit was made by this converter (via SKIP_MARKER) to avoid infinite loops
# - Converts HTML files to Markdown using pandoc with GFM format
# - Preserves relative links and images
# - Commits and pushes changes with a skip marker in the commit message
# - Reports a summary of all conversions
#
# Environment Variables (set by workflow):
# - SKIP_MARKER: String to include in commit message to prevent re-triggering (default: "[skip html-to-md] converter-bot")
# - PUSH_MODE: "true" to push directly, "false" to create a PR (default: "true")
# - PANDOC_ARGS: Additional pandoc arguments (optional)

set -euo pipefail

# Default configuration
SKIP_MARKER="${SKIP_MARKER:-[skip html-to-md] converter-bot}"
PUSH_MODE="${PUSH_MODE:-true}"
PANDOC_ARGS="${PANDOC_ARGS:-}"

echo "=================================================="
echo "HTML to Markdown Conversion Script"
echo "=================================================="
echo "Skip Marker: $SKIP_MARKER"
echo "Push Mode: $PUSH_MODE"
echo "Additional Pandoc Args: ${PANDOC_ARGS:-none}"
echo ""

# Check if the last commit contains the skip marker
echo "Checking last commit message for skip marker..."
LAST_COMMIT_MSG=$(git log -1 --pretty=%B)
echo "Last commit message: $LAST_COMMIT_MSG"

if echo "$LAST_COMMIT_MSG" | grep -qF "$SKIP_MARKER"; then
    echo "✓ Last commit contains skip marker '$SKIP_MARKER'"
    echo "✓ Skipping conversion to avoid infinite loop"
    exit 0
fi

echo "✓ Skip marker not found, proceeding with conversion"
echo ""

# Find all HTML files (excluding .git directory and node_modules)
echo "Searching for HTML files to convert..."
HTML_FILES=$(find . -name "*.html" -type f ! -path "*/\.git/*" ! -path "*/node_modules/*" ! -path "*/\.venv/*" || true)

if [ -z "$HTML_FILES" ]; then
    echo "ℹ️ No HTML files found to convert"
    exit 0
fi

echo "Found HTML files:"
echo "$HTML_FILES"
echo ""

# Arrays to track conversions
CONVERTED_FILES=()
REMOVED_FILES=()
FAILED_FILES=()

# Convert each HTML file
while IFS= read -r html_file; do
    if [ -z "$html_file" ]; then
        continue
    fi
    
    echo "----------------------------------------"
    echo "Processing: $html_file"
    
    # Compute output .md path (same directory, same base name)
    base_dir=$(dirname "$html_file")
    base_name=$(basename "$html_file" .html)
    md_file="${base_dir}/${base_name}.md"
    
    echo "  Output: $md_file"
    
    # Check if output already exists and is identical
    if [ -f "$md_file" ]; then
        echo "  ⚠️  Warning: $md_file already exists, will overwrite"
    fi
    
    # Run pandoc conversion
    echo "  Running pandoc conversion..."
    if pandoc --from=html --to=gfm --wrap=preserve $PANDOC_ARGS -o "$md_file" "$html_file"; then
        echo "  ✓ Conversion successful"
        
        # Check if the output file is non-empty
        if [ -s "$md_file" ]; then
            # Stage the new .md file
            git add "$md_file"
            CONVERTED_FILES+=("$md_file")
            
            # Remove the original .html file
            git rm "$html_file"
            REMOVED_FILES+=("$html_file")
            
            echo "  ✓ Staged $md_file and removed $html_file"
        else
            echo "  ⚠️  Warning: Output file is empty, skipping"
            rm -f "$md_file"
            FAILED_FILES+=("$html_file (empty output)")
        fi
    else
        echo "  ✗ Conversion failed for $html_file"
        FAILED_FILES+=("$html_file (pandoc error)")
    fi
done <<< "$HTML_FILES"

echo ""
echo "=================================================="
echo "Conversion Summary"
echo "=================================================="
echo "Converted files: ${#CONVERTED_FILES[@]}"
for file in "${CONVERTED_FILES[@]}"; do
    echo "  + $file"
done
echo ""
echo "Removed files: ${#REMOVED_FILES[@]}"
for file in "${REMOVED_FILES[@]}"; do
    echo "  - $file"
done
echo ""
if [ ${#FAILED_FILES[@]} -gt 0 ]; then
    echo "Failed files: ${#FAILED_FILES[@]}"
    for file in "${FAILED_FILES[@]}"; do
        echo "  ✗ $file"
    done
    echo ""
fi

# Check if there are changes to commit
if [ ${#CONVERTED_FILES[@]} -eq 0 ]; then
    echo "ℹ️ No files were converted, nothing to commit"
    exit 0
fi

# Check if there are actually staged changes
if git diff --staged --quiet; then
    echo "ℹ️ No staged changes found, nothing to commit"
    exit 0
fi

# Configure git user
echo "Configuring git user..."
git config --local user.email "${GITHUB_ACTOR:-github-actions}@users.noreply.github.com"
git config --local user.name "${GITHUB_ACTOR:-github-actions}"

# Create commit message with skip marker
COMMIT_MSG="$SKIP_MARKER Converted ${#CONVERTED_FILES[@]} HTML file(s) to Markdown

Converted files:
$(for file in "${CONVERTED_FILES[@]}"; do echo "  - $file"; done)

Removed files:
$(for file in "${REMOVED_FILES[@]}"; do echo "  - $file"; done)"

echo "Creating commit..."
git commit -m "$COMMIT_MSG"

if [ "$PUSH_MODE" = "true" ]; then
    echo "Pushing changes to remote..."
    git push
    echo "✓ Changes pushed successfully"
else
    echo "ℹ️ PUSH_MODE is false, skipping push (PR mode would be implemented here)"
    echo "ℹ️ In PR mode, a new branch would be created and a PR opened"
    # Note: PR creation would require additional GitHub API calls or gh CLI
    # For now, we just commit locally
fi

echo ""
echo "=================================================="
echo "✓ HTML to Markdown conversion completed!"
echo "=================================================="
