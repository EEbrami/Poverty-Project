# Test HTML to Markdown Conversion

This is a **test file** to verify the GitHub Actions workflow works correctly.

## Features to Test

- Automatic conversion on push
- Proper markdown formatting
- Skip marker prevents infinite loops

## Expected Result

After pushing this file, the workflow should:

1.  Detect the new HTML file
2.  Convert it to `test-workflow.md`
3.  Remove this `test-workflow.html` file
4.  Commit with skip marker
5.  Not trigger again

Visit the [GitHub repository](https://github.com) to see the results.
