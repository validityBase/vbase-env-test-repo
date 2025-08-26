#!/usr/bin/env python3
"""
Complex test script using pandas for vbase_env_runner testing.
"""
import json
from pathlib import Path

import pandas as pd


def main():
    """Complex main function using pandas."""
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
    df.to_csv(output_dir / "data.csv", index=False)

    # Create summary statistics
    summary = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
    }

    with open(output_dir / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, default=str)

    print("[complex_script] Complex data processing completed")
    return 0


if __name__ == "__main__":
    main()
