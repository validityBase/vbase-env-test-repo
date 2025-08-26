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
import os
import sys
from datetime import datetime
from pathlib import Path


def process_data(input_data):
    """Process input data and return results."""
    # Simulate data processing
    processed_data = {
        "input": input_data,
        "processed_at": datetime.now().isoformat(),
        "status": "completed",
        "record_count": len(input_data) if isinstance(input_data, list) else 1,
    }
    return processed_data


def main():
    """Main entrypoint function."""
    print("[sample_pipeline] Starting test data processing...")

    # Get environment variables
    env_id = os.environ.get("ENV_ID", "unknown")
    entrypoint_args = os.environ.get("ENTRYPOINT_ARGS", "")

    print(f"[sample_pipeline] Environment ID: {env_id}")
    print(f"[sample_pipeline] Entrypoint args: {entrypoint_args}")

    # Create output directory structure (relative to current working directory)
    output_dir = Path("data/output")
    logs_dir = Path("logs")

    # Create all necessary directories
    output_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)

    # Simulate input data
    input_data = [
        {"id": 1, "name": "Test Item 1", "value": 100},
        {"id": 2, "name": "Test Item 2", "value": 200},
        {"id": 3, "name": "Test Item 3", "value": 300},
    ]

    print(f"[sample_pipeline] Processing {len(input_data)} items...")

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

    print("[sample_pipeline] Output files created:")
    print(f"[sample_pipeline] - {output_file}")
    print(f"[sample_pipeline] - {json_output}")
    print(f"[sample_pipeline] - {csv_output}")
    print(f"[sample_pipeline] - {log_file}")

    print("[sample_pipeline] Data processing completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
