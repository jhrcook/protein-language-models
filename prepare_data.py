#!/usr/bin/env python3

"""Prepare the raw data."""

import argparse
from dataclasses import dataclass
from pathlib import Path
import shutil
from urllib.request import urlretrieve
import logging

logging.basicConfig(level="INFO")


def prepare_alphamissense_data(data_dir: Path, force: bool = False) -> None:
    filename = data_dir / "AlphaMissense_aa_substitutions.tsv.gz"
    if force or filename.exists():
        logging.info("AlphaMissense data already downloaded.")
        return
    logging.info("Downloading AlphaMissense dataset...")
    urlretrieve(
        "https://zenodo.org/records/8360242/files/AlphaMissense_aa_substitutions.tsv.gz?download=1",
        filename=filename,
    )
    logging.info("Done.")


def prepare_esm1b_data(data_dir: Path, force: bool = False) -> None:
    filename = data_dir / "ALL_hum_isoforms_ESM1b_LLR.zip"
    if force or not filename.exists():
        logging.info("Downloading ESM1b dataset...")
        urlretrieve(
            "https://huggingface.co/spaces/ntranoslab/esm_variants/resolve/main/ALL_hum_isoforms_ESM1b_LLR.zip",
            filename,
        )
        logging.info("Done.")
    else:
        logging.info("ESM1b data already downloaded.")
    logging.info("Unpacking ESM1b data...")
    esm1b_data_dir = data_dir / "esm1b-predictions"
    if force or not esm1b_data_dir.exists():
        shutil.unpack_archive(filename, esm1b_data_dir)
        shutil.move(
            esm1b_data_dir / "content" / "000_uniprot_df.csv",
            esm1b_data_dir.parent / "000_uniprot_df.csv",
        )
    logging.info("Done.")


@dataclass
class CliArguments:
    data_dir: Path
    force: bool


def _parse_args() -> CliArguments:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--data-dir", default=Path("./raw-data"), help="Data directory."
    )
    parser.add_argument("-f", "--force", action="store_true", help="Force all actions.")
    args = parser.parse_args()
    return CliArguments(data_dir=Path(args.data_dir), force=args.force)


def main() -> None:
    args = _parse_args()
    if not args.data_dir.exists():
        logging.info("Creating data directory.")
        args.data_dir.mkdir(parents=True)
    prepare_alphamissense_data(args.data_dir, force=args.force)
    prepare_esm1b_data(args.data_dir, force=args.force)
    logging.info("Data preparation complete!")


if __name__ == "__main__":
    main()
