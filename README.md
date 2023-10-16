# Protein language models

## Setup

```bash
pyenv local 3.11
python -m venv .env
source .env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

```bash
pre-commit install
```

## Data preparation

Run the following script to download and prepare the raw data:

```bash
./prepare_data.py
```

Data sources:

downloaded AlphaMissesnse predictions: <https://zenodo.org/records/8360242>
downloaded the file: "AlphaMissense_aa_substitutions.tsv.gz"

ESM1b paper: <https://www.nature.com/articles/s41588-023-01465-0>
Downloaded ESM1b: <https://huggingface.co/spaces/ntranoslab/esm_variants/tree/main>
downloaded the file: "ALL_hum_isoforms_ESM1b_LLR.zip"

Copied them to "raw-data/"
