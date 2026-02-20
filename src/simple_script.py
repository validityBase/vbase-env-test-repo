#!/usr/bin/env python3
"""
Simple test script for basic vbase_env_runner testing.
"""
import sys

from env_utils import configure_logging, get_data_dirs

logger = configure_logging(__name__)


def main() -> int:
    """Simple main function that creates a basic output file.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    dirs = get_data_dirs()
    dirs.output.mkdir(parents=True, exist_ok=True)

    output_file = dirs.output / "simple.txt"
    output_file.write_text("Simple output from mock repository")

    logger.info("Simple output created successfully at %s", output_file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
