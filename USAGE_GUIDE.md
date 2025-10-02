# HTML to Markdown Conversion - Testing and Usage Guide

## Quick Start

The HTML to Markdown conversion workflow is now active in this repository! It will automatically convert any HTML files you add or modify.

## Testing the Workflow

### What Just Happened

A test file `test-workflow.html` was just pushed to the repository. The GitHub Actions workflow should now:

1. ✅ Detect the new HTML file (via push trigger)
2. ✅ Install pandoc in the runner
3. ✅ Run the conversion script
4. ✅ Create `test-workflow.md` with proper markdown formatting
5. ✅ Remove `test-workflow.html`
6. ✅ Commit with message: `[skip html-to-md] converter-bot Converted 1 HTML file(s) to Markdown`
7. ✅ Not trigger again (skip marker prevents infinite loop)

### How to Verify the Workflow Worked

1. **Check GitHub Actions**: 
   - Go to the "Actions" tab in the repository
   - Look for a workflow run named "Convert HTML to Markdown"
   - It should show as completed successfully
   - Click on it to see the detailed logs

2. **Check the Commit History**:
   - Look for a new commit with message `[skip html-to-md] converter-bot ...`
   - This commit should be right after "Add test HTML file to verify workflow triggers correctly"

3. **Check the Files**:
   - `test-workflow.html` should be deleted
   - `test-workflow.md` should exist with proper markdown content
   - The markdown should have properly formatted headers, lists, links, etc.

4. **Verify No Loop**:
   - Check that the workflow only ran once (not repeatedly)
   - The second trigger should have exited early with "Skipping because last commit is by converter"

## Manual Testing

You can also test the conversion locally before pushing:

```bash
# 1. Create a test HTML file
cat > my-test.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>My Test</title></head>
<body>
    <h1>Hello World</h1>
    <p>This is a <strong>test</strong>.</p>
</body>
</html>
EOF

# 2. Install pandoc (if not already installed)
# Ubuntu/Debian:
sudo apt-get install pandoc

# macOS:
brew install pandoc

# 3. Test the conversion manually
pandoc --from=html --to=gfm --wrap=preserve -o my-test.md my-test.html

# 4. Check the output
cat my-test.md
```

## Running the Script Manually

To run the full conversion script without pushing:

```bash
# Export environment variables
export SKIP_MARKER="[skip html-to-md] converter-bot"
export PUSH_MODE="false"  # Don't push automatically
export PANDOC_ARGS=""
export GITHUB_ACTOR="your-username"

# Run the script
bash scripts/convert-html-to-md.sh
```

Expected output:
```
==================================================
HTML to Markdown Conversion Script
==================================================
Skip Marker: [skip html-to-md] converter-bot
Push Mode: false
Additional Pandoc Args: none

Checking last commit message for skip marker...
✓ Skip marker not found, proceeding with conversion

Searching for HTML files to convert...
Found HTML files:
./my-test.html

Processing: ./my-test.html
  ✓ Conversion successful
  ✓ Staged ./my-test.md and removed ./my-test.html

Conversion Summary
Converted files: 1
  + ./my-test.md
Removed files: 1
  - ./my-test.html

✓ HTML to Markdown conversion completed!
```

## Testing Different Scenarios

### Scenario 1: Add a New HTML File

```bash
# Add a new HTML file
echo '<h1>Test</h1>' > new-file.html
git add new-file.html
git commit -m "Add new HTML file"
git push

# Result: Workflow converts to new-file.md and removes new-file.html
```

### Scenario 2: Modify an Existing HTML File (won't work since they're deleted)

Since HTML files are deleted after conversion, you would need to:
1. Add a new HTML file (scenario 1)
2. Or edit the .md file directly

### Scenario 3: Skip Conversion

```bash
# Add HTML but skip automatic conversion
echo '<h1>Manual</h1>' > manual.html
git add manual.html
git commit -m "[skip html-to-md] Adding HTML for manual review"
git push

# Result: Workflow detects skip marker and exits without converting
```

### Scenario 4: Batch Convert Multiple Files

```bash
# Add multiple HTML files
echo '<h1>File 1</h1>' > file1.html
echo '<h1>File 2</h1>' > file2.html
echo '<h1>File 3</h1>' > file3.html
git add *.html
git commit -m "Add multiple HTML files"
git push

# Result: Workflow converts all 3 files in a single run
```

## Troubleshooting

### Issue: Workflow Doesn't Trigger

**Symptoms**: You pushed an HTML file but the workflow didn't run.

**Solutions**:
1. Check if the file path matches `**/*.html`
2. Go to Actions tab → Workflows → "Convert HTML to Markdown" → Ensure it's enabled
3. Check if your commit message contains the skip marker
4. Verify you're pushing to a branch (not just committing locally)

### Issue: Workflow Runs But Doesn't Commit

**Symptoms**: Workflow runs successfully but no new commit appears.

**Solutions**:
1. Check workflow logs for "No files were converted, nothing to commit"
2. Verify the HTML file exists and is not empty
3. Check if the file was already converted in a previous run
4. Look for "Last commit contains skip marker" in logs

### Issue: Conversion Output is Empty or Broken

**Symptoms**: The .md file exists but is empty or poorly formatted.

**Solutions**:
1. Check if the HTML file is valid HTML
2. Review the HTML structure - complex CSS/JavaScript won't convert well
3. Try converting manually with pandoc to see the output
4. Check workflow logs for pandoc errors

### Issue: Infinite Loop Detected

**Symptoms**: Workflow keeps running repeatedly on the same files.

**Solutions**:
1. Check if `SKIP_MARKER` environment variable is set correctly in the workflow
2. Verify the commit message includes the skip marker
3. Check the script's skip marker detection logic
4. Manually disable the workflow in Actions tab if needed

## Expected Conversion Quality

### What Converts Well ✅

- Headers (h1-h6) → `# Header`
- Bold text → `**bold**`
- Italic text → `*italic*`
- Links → `[text](url)`
- Images → `![alt](src)`
- Lists (ul/ol) → `- item` or `1. item`
- Code blocks → ` ```code``` `
- Paragraphs → Plain text with spacing

### What May Not Convert Well ⚠️

- Complex CSS styling (lost in conversion)
- JavaScript functionality (not applicable to Markdown)
- Complex tables (may need manual adjustment)
- Custom HTML elements
- Embedded media (videos, iframes)
- Forms and interactive elements

## Performance Expectations

### Small Files (< 100 KB)
- Conversion time: < 5 seconds per file
- Workflow total time: ~30-60 seconds

### Medium Files (100 KB - 1 MB)
- Conversion time: ~10-30 seconds per file
- Workflow total time: ~1-2 minutes

### Large Files (> 1 MB)
- Conversion time: ~30-60 seconds per file
- Workflow total time: ~2-5 minutes
- Consider splitting very large files

### Batch Conversions
- Processing time increases linearly with number of files
- GitHub Actions timeout: 6 hours (should never be reached)

## Best Practices

1. **Test Locally First**: Use pandoc locally to verify conversion quality before committing
2. **Small Commits**: Commit HTML files in small batches for easier troubleshooting
3. **Review Conversions**: Check the converted .md files to ensure quality
4. **Use Skip Marker**: When adding HTML files that shouldn't be converted yet
5. **Keep HTML Simple**: Simpler HTML converts better to Markdown
6. **Document Changes**: Note any manual adjustments needed after conversion

## Next Steps

After verifying the workflow works correctly:

1. **Clean Up**: Remove `test-workflow.md` if you don't need it
2. **Add More Files**: Start adding your HTML files
3. **Customize**: Adjust `PANDOC_ARGS` in the workflow if needed
4. **Monitor**: Watch the Actions tab for any issues
5. **Share**: Update your main README to mention this feature

## Getting Help

If you encounter issues:

1. Check the workflow logs in the Actions tab
2. Review `README_html_conversion.md` for detailed documentation
3. Test locally using pandoc to isolate the problem
4. Check pandoc documentation for advanced conversion options
5. Open an issue in the repository

## Configuration Reference

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SKIP_MARKER` | `[skip html-to-md] converter-bot` | String to detect in commits to skip conversion |
| `PUSH_MODE` | `true` | `true` for direct push, `false` for PR mode |
| `PANDOC_ARGS` | `""` | Additional pandoc arguments |
| `GITHUB_ACTOR` | (set by Actions) | Git commit author name |

### Workflow Triggers

| Event | Trigger | Description |
|-------|---------|-------------|
| `push` | `**/*.html` | Any HTML file added/modified on push |
| `pull_request` | `**/*.html` | Any HTML file in a PR |
| `workflow_dispatch` | Manual | Trigger from Actions tab |

### File Locations

| File | Purpose |
|------|---------|
| `.github/workflows/html-to-md.yml` | Workflow definition |
| `scripts/convert-html-to-md.sh` | Conversion script |
| `README_html_conversion.md` | Main documentation |
| `USAGE_GUIDE.md` | This testing guide |

## Success Criteria

✅ The workflow is working correctly if:

1. HTML files are automatically detected when pushed
2. Conversion creates properly formatted Markdown files
3. Original HTML files are removed after conversion
4. Commits include the skip marker
5. Workflow doesn't trigger on its own commits (no infinite loop)
6. All conversions complete without errors
7. Generated Markdown is readable and properly formatted

You can now confidently use this workflow for all your HTML to Markdown conversions!
