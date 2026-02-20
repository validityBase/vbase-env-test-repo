#!/usr/bin/env python3
"""
Sample pipeline entrypoint for vbase_env_runner testing.

This script simulates a typical data processing pipeline that:
1. Reads input data from /data/internal/ (if available)
2. Processes the data
3. Generates output files to /data/output/
"""
import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Union

from env_utils import DataDirs, configure_logging, get_data_dirs

logger = configure_logging(__name__)


def load_input_data(internal_dir: Path) -> List[Dict[str, Any]]:
    """Load input data from /data/internal/ if available.

    Args:
        internal_dir: Path to the internal data directory

    Returns:
        List of input data records, or empty list if no input found
    """
    input_file = internal_dir / "input.json"
    if input_file.exists():
        logger.info("Loading input data from %s", input_file)
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return [data]

    logger.info("No input data found at %s, using default data", input_file)
    return []


def process_data(
    input_data: Union[List[Dict[str, Any]], Dict[str, Any]],
) -> Dict[str, Any]:
    """Process input data and return results.

    Args:
        input_data: Input data to process

    Returns:
        Dictionary containing processed data with metadata
    """
    return {
        "input": input_data,
        "processed_at": datetime.now().isoformat(),
        "status": "completed",
        "record_count": len(input_data) if isinstance(input_data, list) else 1,
    }


def write_outputs(
    dirs: DataDirs,
    results: Dict[str, Any],
    input_data: List[Dict[str, Any]],
    env_id: str,
) -> None:
    """Write all output files.

    Args:
        dirs: Data directory paths
        results: Processed results dictionary
        input_data: Original input data records
        env_id: Environment identifier
    """
    output_file = dirs.output / "result.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Processing completed at {results['processed_at']}\n")
        f.write(f"Status: {results['status']}\n")
        f.write(f"Records processed: {results['record_count']}\n")
        f.write(f"Environment: {env_id}\n")

    json_output = dirs.output / "results.json"
    with open(json_output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    csv_output = dirs.output / "data.csv"
    with open(csv_output, "w", encoding="utf-8") as f:
        f.write("id,name,value\n")
        for item in input_data:
            f.write(f"{item['id']},{item['name']},{item['value']}\n")

    logger.info("Output files created:")
    logger.info("- %s", output_file)
    logger.info("- %s", json_output)
    logger.info("- %s", csv_output)


def main() -> int:
    """Main entrypoint function.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    parser = argparse.ArgumentParser(description="Sample data processing pipeline")
    parser.add_argument("--test-mode", action="store_true", help="Run in test mode")
    args = parser.parse_args()

    logger.info("Starting test data processing...")
    logger.info("Command line arguments: %s", args)

    env_id = os.environ.get("ENV_ID", "unknown")
    entrypoint_args = os.environ.get("ENTRYPOINT_ARGS", "")
    logger.info("Environment ID: %s", env_id)
    logger.info("Entrypoint args: %s", entrypoint_args)

    dirs = get_data_dirs()
    dirs.output.mkdir(parents=True, exist_ok=True)

    # Try to load input data from /data/internal/
    input_data = load_input_data(dirs.internal)

    # If no input data found, use default sample data
    if not input_data:
        if args.test_mode:
            logger.info("Running in test mode")
            input_data = [
                {"id": 1, "name": "Test Item 1", "value": 100, "mode": "test"},
                {"id": 2, "name": "Test Item 2", "value": 200, "mode": "test"},
            ]
        else:
            input_data = [
                {"id": 1, "name": "Test Item 1", "value": 100},
                {"id": 2, "name": "Test Item 2", "value": 200},
                {"id": 3, "name": "Test Item 3", "value": 300},
            ]

    logger.info("Processing %d items...", len(input_data))
    results = process_data(input_data)

    write_outputs(dirs, results, input_data, env_id)

    logger.info("Data processing completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
