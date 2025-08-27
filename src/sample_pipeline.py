#!/usr/bin/env python3
"""
Sample pipeline entrypoint for vbase_env_runner testing.

This script simulates a typical data processing pipeline that:
1. Reads input data
2. Processes the data
3. Generates output files
4. Logs progress
"""
import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def process_data(
    input_data: Union[List[Dict[str, Any]], Dict[str, Any]],
) -> Dict[str, Any]:
    """Process input data and return results.

    Args:
        input_data: Input data to process, either a list of dictionaries or a single dictionary

    Returns:
        Dictionary containing processed data with metadata
    """
    # Simulate data processing
    processed_data = {
        "input": input_data,
        "processed_at": datetime.now().isoformat(),
        "status": "completed",
        "record_count": len(input_data) if isinstance(input_data, list) else 1,
    }
    return processed_data


def main() -> int:
    """Main entrypoint function.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    logger.info("Starting test data processing...")

    # Get environment variables
    env_id = os.environ.get("ENV_ID", "unknown")
    entrypoint_args = os.environ.get("ENTRYPOINT_ARGS", "")

    logger.info("Environment ID: %s", env_id)
    logger.info("Entrypoint args: %s", entrypoint_args)

    # Create output directory structure (relative to work root)
    output_dir = Path("/work/output/data/output")
    logs_dir = Path("/work/logs")

    # Create all necessary directories
    output_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)

    # Simulate input data
    input_data = [
        {"id": 1, "name": "Test Item 1", "value": 100},
        {"id": 2, "name": "Test Item 2", "value": 200},
        {"id": 3, "name": "Test Item 3", "value": 300},
    ]

    logger.info("Processing %d items...", len(input_data))

    # Process data
    results = process_data(input_data)

    # Write results to output files
    output_file = output_dir / "result.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Processing completed at {results['processed_at']}\n")
        f.write(f"Status: {results['status']}\n")
        f.write(f"Records processed: {results['record_count']}\n")
        f.write(f"Environment: {env_id}\n")

    # Create JSON output
    json_output = output_dir / "results.json"
    with open(json_output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # Create CSV-like output
    csv_output = output_dir / "data.csv"
    with open(csv_output, "w", encoding="utf-8") as f:
        f.write("id,name,value\n")
        for item in input_data:
            f.write(f"{item['id']},{item['name']},{item['value']}\n")

    # Create a log file
    log_file = logs_dir / "processing.log"
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] Processing started\n")
        f.write(f"[{datetime.now().isoformat()}] Environment: {env_id}\n")
        f.write(f"[{datetime.now().isoformat()}] Items processed: {len(input_data)}\n")
        f.write(f"[{datetime.now().isoformat()}] Processing completed\n")

    logger.info("Output files created:")
    logger.info("- %s", output_file)
    logger.info("- %s", json_output)
    logger.info("- %s", csv_output)
    logger.info("- %s", log_file)

    logger.info("Data processing completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
