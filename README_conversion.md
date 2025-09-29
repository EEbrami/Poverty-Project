# Excel File Conversion Workflow

This repository includes an automated workflow that converts Excel files (`.xlsx`) to multiple presentable formats: CSV, JSON, and Markdown tables.

## How It Works

### Automatic Trigger
The workflow automatically runs when:
- New Excel files (`.xlsx`) are added to the repository
- Existing Excel files are modified
- You can also trigger it manually from the Actions tab

### Conversion Process
1. **Detection**: The workflow detects which Excel files have been added or changed
2. **Conversion**: Uses a Python script to convert each Excel file to three formats:
   - **CSV**: Standard comma-separated values format
   - **JSON**: Structured data format for programmatic use
   - **Markdown**: Human-readable table format for documentation
3. **Storage**: All converted files are saved in the `converted_files/` directory
4. **Commit**: Automatically commits the converted files back to the repository

### Features

#### Multi-Sheet Support
- Handles Excel files with multiple sheets
- Each sheet is converted to separate files with descriptive names
- Example: `variables-definition.xlsx` with sheets "Major Economic Aggregates" and "Household Composition" creates files like:
  - `variables-definition - Major Economic Aggregates.csv`
  - `variables-definition - Household Composition and Livin.json`

#### Large File Optimization
- For large datasets (>1000 rows or >10MB estimated markdown size):
  - Shows dataset summary with row/column counts
  - Displays sample data (first 50-100 rows)
  - Limits columns displayed for readability
  - Maintains full data in CSV and JSON formats
- Prevents creation of excessively large files that could cause issues

#### Error Handling
- Continues processing if one file fails
- Provides detailed logging of conversion process
- Reports success/failure counts

## File Structure

```
repository/
├── .github/workflows/convert-excel.yml    # GitHub Action workflow
├── convert_excel.py                       # Python conversion script
├── converted_files/                       # Output directory
│   ├── filename.csv                      # CSV format
│   ├── filename.json                     # JSON format
│   └── filename.md                       # Markdown format
└── your-excel-files.xlsx                 # Source Excel files
```

## Manual Usage

You can also run the conversion script manually:

```bash
# Convert a specific file
python convert_excel.py --file path/to/your/file.xlsx --output converted_files

# Convert all Excel files in current directory
python convert_excel.py --directory . --output converted_files

# Get help
python convert_excel.py --help
```

## Requirements

The workflow automatically installs these Python dependencies:
- `pandas`: For Excel file reading and data manipulation
- `openpyxl`: For Excel file format support
- `tabulate`: For creating formatted markdown tables

## Current Converted Files

The repository currently includes converted versions of:
- `codebook.xlsx` → CSV, JSON, Markdown
- `our-lis-documentation.xlsx` → CSV, JSON, Markdown (with optimization for large dataset)
- `variables-definition.xlsx` → Multiple sheets converted separately
- `our-lis-documentation-availability-matrix.xlsx` → Multiple sheets converted

## Workflow Configuration

The workflow is configured to:
- Run on push/pull request events that modify `.xlsx` files
- Use Ubuntu latest environment
- Install Python 3.x and required dependencies
- Commit changes with meaningful commit messages
- Provide execution summaries

## Benefits

1. **Accessibility**: Excel data becomes accessible in multiple formats
2. **Version Control**: CSV and JSON formats work better with git diff
3. **Documentation**: Markdown tables provide human-readable documentation
4. **Automation**: No manual conversion needed when Excel files are updated
5. **Consistency**: Standardized conversion process for all Excel files