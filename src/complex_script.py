#!/usr/bin/env python3
"""
Complex test script using pandas for vbase_env_runner testing.
"""
import json
import logging
from pathlib import Path
from typing import Any, Dict

import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main() -> int:
    """Complex main function using pandas.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    # Create vbase-env directory structure
    vbase_env_dir = Path("/vbase-env")
    data_dir = vbase_env_dir / "data"
    output_dir = data_dir / "output"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create a pandas DataFrame
    df = pd.DataFrame(
        {
            "A": [1, 2, 3, 4, 5],
            "B": [10, 20, 30, 40, 50],
            "C": ["alpha", "beta", "gamma", "delta", "epsilon"],
        }
    )

    # Save as CSV
    csv_file = output_dir / "data.csv"
    df.to_csv(csv_file, index=False)
    logger.info("Data saved to CSV: %s", csv_file)

    # Create summary statistics
    summary: Dict[str, Any] = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
    }

    json_file = output_dir / "summary.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, default=str)

    logger.info("Summary saved to JSON: %s", json_file)
    logger.info("Complex data processing completed")
    return 0


if __name__ == "__main__":
    main()
