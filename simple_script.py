#!/usr/bin/env python3
"""
Simple test script for basic vbase_env_runner testing.
"""
import sys
from pathlib import Path


def main():
    """Simple main function that creates a basic output file."""
    # Create vbase-env directory structure
    vbase_env_dir = Path("/vbase-env")
    data_dir = vbase_env_dir / "data"
    output_dir = data_dir / "output"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create a simple output file
    output_file = output_dir / "simple.txt"
    output_file.write_text("Simple output from mock repository")

    print("[simple_script] Simple output created successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
