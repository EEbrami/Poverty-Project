#!/usr/bin/env python3
"""
Excel File Converter Script
Converts Excel files to CSV, JSON, and Markdown table formats.
"""

import os
import sys
import json
import pandas as pd
from pathlib import Path
import argparse


def convert_excel_to_formats(excel_file_path, output_dir):
    """
    Convert an Excel file to CSV, JSON, and Markdown formats.
    
    Args:
        excel_file_path (str): Path to the Excel file
        output_dir (str): Directory to save converted files
    """
    try:
        # Read the Excel file
        excel_file = Path(excel_file_path)
        if not excel_file.exists():
            print(f"Error: Excel file {excel_file_path} does not exist")
            return False
            
        print(f"Converting {excel_file.name}...")
        
        # Create output directory if it doesn't exist
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Get the base filename without extension
        base_name = excel_file.stem
        
        # Read Excel file - handle multiple sheets
        excel_data = pd.read_excel(excel_file_path, sheet_name=None)
        
        # If single sheet, process directly
        if len(excel_data) == 1:
            sheet_name, df = next(iter(excel_data.items()))
            _convert_dataframe_to_formats(df, base_name, output_path)
        else:
            # Multiple sheets - convert each sheet separately
            for sheet_name, df in excel_data.items():
                # Clean sheet name for filename
                clean_sheet_name = "".join(c for c in sheet_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
                sheet_base_name = f"{base_name} - {clean_sheet_name}" if clean_sheet_name else f"{base_name} - Sheet{list(excel_data.keys()).index(sheet_name) + 1}"
                _convert_dataframe_to_formats(df, sheet_base_name, output_path)
        
        print(f"Successfully converted {excel_file.name}")
        return True
        
    except Exception as e:
        print(f"Error converting {excel_file_path}: {str(e)}")
        return False


def _convert_dataframe_to_formats(df, base_name, output_path):
    """
    Convert a pandas DataFrame to CSV, JSON, and Markdown formats.
    
    Args:
        df (pandas.DataFrame): The dataframe to convert
        base_name (str): Base name for output files
        output_path (Path): Path to output directory
    """
    # Convert to CSV
    csv_file = output_path / f"{base_name}.csv"
    df.to_csv(csv_file, index=False)
    print(f"  Created: {csv_file}")
    
    # Convert to JSON
    json_file = output_path / f"{base_name}.json"
    df.to_json(json_file, orient='records', indent=2)
    print(f"  Created: {json_file}")
    
    # Convert to Markdown
    md_file = output_path / f"{base_name}.md"
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(f"# {base_name}\n\n")
        f.write("Data converted from Excel file.\n\n")
        f.write(df.to_markdown(index=False))
        f.write("\n")
    print(f"  Created: {md_file}")


def find_excel_files(directory):
    """
    Find all Excel files in a directory and its subdirectories.
    
    Args:
        directory (str): Directory to search
        
    Returns:
        list: List of Excel file paths
    """
    excel_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.xlsx'):
                excel_files.append(os.path.join(root, file))
    return excel_files


def main():
    parser = argparse.ArgumentParser(description='Convert Excel files to CSV, JSON, and Markdown formats')
    parser.add_argument('--file', help='Specific Excel file to convert')
    parser.add_argument('--directory', default='.', help='Directory to search for Excel files (default: current directory)')
    parser.add_argument('--output', default='converted_files', help='Output directory for converted files (default: converted_files)')
    
    args = parser.parse_args()
    
    success_count = 0
    total_count = 0
    
    if args.file:
        # Convert specific file
        total_count = 1
        if convert_excel_to_formats(args.file, args.output):
            success_count = 1
    else:
        # Find and convert all Excel files
        excel_files = find_excel_files(args.directory)
        total_count = len(excel_files)
        
        if not excel_files:
            print("No Excel files found in the specified directory.")
            return
        
        print(f"Found {total_count} Excel file(s) to convert...")
        
        for excel_file in excel_files:
            if convert_excel_to_formats(excel_file, args.output):
                success_count += 1
    
    print(f"\nConversion complete: {success_count}/{total_count} files converted successfully")
    
    if success_count < total_count:
        sys.exit(1)


if __name__ == "__main__":
    main()