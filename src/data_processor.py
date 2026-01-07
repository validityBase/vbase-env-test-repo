#!/usr/bin/env python3
"""
Data processing script for vbase_env_runner testing.
"""
import json
import logging
import os
from pathlib import Path
from typing import Any, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main() -> int:
    """Data processing main function.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    # Use the standard vbase_env_runner data root (/data in container)
    # Can be overridden with VBASE_DATA_ROOT for local testing
    data_root = Path(os.environ.get("VBASE_DATA_ROOT", "/data"))
    output_dir = data_root / "output"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process some data
    data: Dict[str, Any] = {"processed": True, "count": 42, "status": "completed"}

    # Write JSON output
    json_file = output_dir / "data.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    logger.info("Data processing completed, output saved to: %s", json_file)
    return 0


if __name__ == "__main__":
    main()
