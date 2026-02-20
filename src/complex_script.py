#!/usr/bin/env python3
"""
Complex test script using pandas for vbase_env_runner testing.
"""
import json
import sys
from typing import Any, Dict

import pandas as pd

from env_utils import configure_logging, get_data_dirs

logger = configure_logging(__name__)


def main() -> int:
    """Complex main function using pandas.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    dirs = get_data_dirs()
    dirs.output.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(
        {
            "A": [1, 2, 3, 4, 5],
            "B": [10, 20, 30, 40, 50],
            "C": ["alpha", "beta", "gamma", "delta", "epsilon"],
        }
    )

    csv_file = dirs.output / "data.csv"
    df.to_csv(csv_file, index=False)
    logger.info("Data saved to CSV: %s", csv_file)

    summary: Dict[str, Any] = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
    }

    json_file = dirs.output / "summary.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, default=str)

    logger.info("Summary saved to JSON: %s", json_file)
    logger.info("Complex data processing completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
