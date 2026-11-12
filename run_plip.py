# -*- coding: utf-8 -*-
import argparse
from pathlib import Path
import subprocess

# Target complex filenames
COMPLEX_FILENAMES = [
    "model_1_complex.pdb",
    "model_2_complex.pdb",
    "model_3_complex.pdb",
    "model_4_complex.pdb",
    "model_5_complex.pdb"
]

# PLIP base command arguments
PLIP_BASE_COMMAND = ["plip", "--peptides", "B", "-t", "-f"] 


def run_plip_batch(root_dir: Path):
    """Find 'complexes' subdirectories and run PLIP on specified PDB files."""
    
    print(f"Searching in: {root_dir.resolve()}")
    found_any = False
    
    # Traverse directories using pathlib
    for dirpath in root_dir.rglob("complexes"):
        if dirpath.is_dir():
            found_any = True
            print("-" * 50)
            print(f"Entered: {dirpath}")
            
            current_files = {f.name for f in dirpath.iterdir() if f.is_file()}

            for complex_file in COMPLEX_FILENAMES:
                if complex_file in current_files:
                    file_path = dirpath / complex_file
                    output_name = complex_file.replace(".pdb", "_PLIP")
                    output_path = dirpath / output_name
                    
                    print(f" Processing: {complex_file}")
                    
                    # Construct full command
                    command = PLIP_BASE_COMMAND + [str(file_path), "-o", str(output_path)]
                    
                    # Run command
                    try:
                        subprocess.run(
                            command, 
                            capture_output=True, 
                            text=True, 
                            check=True
                        )
                        print(f" [Success] Report saved to {output_name}")
                        
                    except subprocess.CalledProcessError as e:
                        print(f" [PLIP Error] Failed to process {complex_file}")
                        err_msg = e.stderr.strip()
                        if err_msg:
                            print(f" Details: {err_msg.splitlines()[-1]}")
                    except FileNotFoundError:
                        print(" [System Error] 'plip' command not found in PATH. Make sure PLIP is installed.")

                else:
                    print(f" {complex_file} not found. Skipping.")

    if not found_any:
        print("No 'complexes' directories found.")

    print("-" * 50)
    print("Batch processing completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run PLIP batch processing on complex PDB files.")
    parser.add_argument(
        "root_dir", 
        nargs="?", 
        default=".", 
        type=Path, 
        help="Root directory to search for 'complexes' folders (default: current directory)."
    )
    args = parser.parse_args()
    
    run_plip_batch(args.root_dir)
