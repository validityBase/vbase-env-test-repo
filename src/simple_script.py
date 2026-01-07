#!/usr/bin/env python3
"""
Simple test script for basic vbase_env_runner testing.
"""
import logging
import os
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main() -> int:
    """Simple main function that creates a basic output file.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    # Use the standard vbase_env_runner data root (/data in container)
    # Can be overridden with VBASE_DATA_ROOT for local testing
    data_root = Path(os.environ.get("VBASE_DATA_ROOT", "/data"))
    output_dir = data_root / "output"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create a simple output file
    output_file = output_dir / "simple.txt"
    output_file.write_text("Simple output from mock repository")

    logger.info("Simple output created successfully at %s", output_file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
