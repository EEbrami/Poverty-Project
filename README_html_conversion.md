# HTML to Markdown Conversion Workflow

This repository includes an automated GitHub Actions workflow that converts HTML files to GitHub-flavored Markdown (GFM) format whenever HTML files are added or modified.

## Overview

The workflow automatically:
- Detects when HTML files are added or modified
- Converts them to Markdown using pandoc
- Commits the new `.md` files
- Removes the original `.html` files
- Prevents infinite workflow loops using a skip marker

## How It Works

### Automatic Trigger

The workflow automatically runs when:
- New HTML files (`.html`) are added to the repository
- Existing HTML files are modified
- You manually trigger it from the Actions tab (workflow_dispatch)

### Conversion Process

1. **Detection**: The workflow checks if the last commit contains the skip marker to prevent infinite loops
2. **Search**: Finds all `.html` files in the repository (excluding `.git`, `node_modules`, `.venv`)
3. **Conversion**: Uses pandoc to convert each HTML file to GitHub-flavored Markdown with these features:
   - Preserves headers, lists, links, and code blocks
   - Converts images to Markdown format
   - Maintains relative paths
   - Uses `--wrap=preserve` to avoid line wrapping issues
4. **Commit**: Commits the new `.md` files and removes the original `.html` files
5. **Skip Marker**: Includes `[skip html-to-md] converter-bot` in the commit message to prevent re-triggering

## File Structure

```
repository/
├── .github/workflows/html-to-md.yml    # GitHub Action workflow
├── scripts/convert-html-to-md.sh       # Bash conversion script
└── your-html-files.html                # Source HTML files
```

## Configuration Options

You can configure the workflow by editing `.github/workflows/html-to-md.yml`:

### Push Mode (Default: Direct Push)

By default, the workflow pushes directly to the current branch:

```yaml
env:
  PUSH_MODE: "true"  # Direct push mode
```

To create a Pull Request instead (for human review before merging):

```yaml
env:
  PUSH_MODE: "false"  # PR mode (requires additional setup)
```

**Note**: PR mode requires additional configuration using GitHub CLI or API.

### Skip Marker (Default: `[skip html-to-md] converter-bot`)

Change the skip marker if needed:

```yaml
env:
  SKIP_MARKER: "[skip html-to-md] converter-bot"
```

### Pandoc Arguments

Add custom pandoc conversion options:

```yaml
env:
  PANDOC_ARGS: "--standalone --toc"  # Add table of contents
```

## Manual Usage

You can also run the conversion script manually:

```bash
# Set environment variables
export SKIP_MARKER="[skip html-to-md] converter-bot"
export PUSH_MODE="false"  # Don't push automatically when testing
export PANDOC_ARGS=""

# Run the script
bash scripts/convert-html-to-md.sh
```

## Disabling the Workflow

To temporarily disable automatic conversion:

1. **Via Commit Message**: Include the skip marker in your commit message when adding HTML files
   ```bash
   git commit -m "[skip html-to-md] Adding HTML files for manual review"
   ```

2. **Via GitHub Actions**: Go to the Actions tab → Select "Convert HTML to Markdown" → Click "..." → "Disable workflow"

## Safety Features

### Infinite Loop Prevention

The workflow checks if the last commit message contains the skip marker. If found, it exits immediately without converting files. This prevents the workflow from:
- Triggering itself repeatedly
- Creating endless commit chains
- Wasting GitHub Actions minutes

### Idempotence

Re-running the workflow on the same files won't create duplicate commits if:
- No HTML files have changed
- The last commit was made by the converter (contains skip marker)
- All HTML files have already been converted

### Error Handling

The script uses `set -euo pipefail` for safe execution:
- Exits on any command failure
- Treats undefined variables as errors
- Catches errors in piped commands

## Example Workflow Run

When you add `example.html`:

```
1. Commit: "Add example.html"
   Trigger: Workflow detects HTML file change
   
2. Workflow runs:
   - Checks last commit (no skip marker found)
   - Finds example.html
   - Converts to example.md using pandoc
   - Stages example.md
   - Removes example.html
   - Commits with: "[skip html-to-md] converter-bot Converted 1 HTML file(s) to Markdown"
   - Pushes to repository
   
3. Workflow triggered again by the new commit
   - Checks last commit (skip marker found!)
   - Exits without doing anything ✓
```

## Testing Locally

Before pushing HTML files, you can test the conversion locally:

```bash
# Install pandoc (Ubuntu/Debian)
sudo apt-get install pandoc

# Or on macOS
brew install pandoc

# Test conversion manually
pandoc --from=html --to=gfm --wrap=preserve -o output.md input.html

# Or run the full script in test mode
export PUSH_MODE="false"
bash scripts/convert-html-to-md.sh
```

## Conversion Quality

The pandoc conversion preserves:
- ✓ Headers (h1-h6)
- ✓ Paragraphs and line breaks
- ✓ Bold, italic, and code formatting
- ✓ Lists (ordered and unordered)
- ✓ Links (preserves relative paths)
- ✓ Images (converts to Markdown image syntax)
- ✓ Code blocks
- ✓ Tables (when possible)

Note: Complex HTML with heavy CSS styling may not translate perfectly to Markdown, as Markdown is a simplified format.

## Troubleshooting

### Workflow doesn't trigger

- Check if the HTML file is in a path that matches `**/*.html`
- Ensure the workflow is enabled in the Actions tab
- Verify you have push access to the repository

### Conversion produces empty files

- Check if the HTML file is valid
- Verify pandoc is installed correctly in the workflow
- Review the workflow logs for pandoc errors

### Infinite loop detected

If the workflow seems to run repeatedly:
1. Check if the skip marker is included in commit messages
2. Verify the `SKIP_MARKER` environment variable matches between workflow and script
3. Review recent commits in the repository history

### Changes not committed

- Ensure `permissions: contents: write` is set in the workflow
- Check if there are actual changes to commit (diff not empty)
- Review workflow logs for git errors

## Permissions

The workflow requires:
- `contents: write` - To commit and push converted files

These permissions are set in the workflow file and use the default `GITHUB_TOKEN`.

## Benefits

1. **Automation**: No manual conversion needed when HTML files are updated
2. **Consistency**: Standardized conversion process using pandoc
3. **Version Control**: Markdown files work better with git diff
4. **Documentation**: Generated Markdown is more readable in GitHub
5. **Safety**: Built-in loop prevention and error handling

## See Also

- [Pandoc Documentation](https://pandoc.org/MANUAL.html)
- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
