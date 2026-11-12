# Batch PLIP Runner

A lightweight Python utility to recursively find `complexes` directories and run the Protein-Ligand Interaction Profiler (PLIP) on target PDB models (`model_1_complex.pdb` to `model_5_complex.pdb`).

## Prerequisites

- Python 3.8+
- [PLIP](https://github.com/pharmai/plip) installed and accessible in your system `PATH`.

```bash
pip install -r requirements.txt
```

## Usage

Run in the current directory:
```bash
python run_plip.py
```

Or specify a target directory:
```bash
python run_plip.py /path/to/your/screening_folder
```
