"""
Shared utilities for vbase_env_runner entrypoint scripts.

Provides common setup for logging and data directory resolution
using vbase_env_runner environment variables.
"""

import logging
import os
from pathlib import Path
from typing import NamedTuple


class DataDirs(NamedTuple):
    """Data directory paths resolved from vbase_env_runner environment variables."""

    root: Path
    internal: Path
    output: Path


def configure_logging(name: str) -> logging.Logger:
    """Configure logging and return a logger for the given module name.

    Args:
        name: Module name (typically __name__)

    Returns:
        Configured logger instance
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger(name)


def get_data_dirs() -> DataDirs:
    """Resolve data directory paths from vbase_env_runner environment variables.

    The container sets DATA_ROOT, DATA_INTERNAL_DIR, DATA_OUTPUT_DIR
    automatically. For local testing outside containers,
    override DATA_ROOT, e.g.: DATA_ROOT=. python src/sample_pipeline.py

    Returns:
        DataDirs with resolved paths for root, internal, and output
    """
    data_root = Path(os.environ.get("DATA_ROOT", "/data"))
    return DataDirs(
        root=data_root,
        internal=Path(os.environ.get("DATA_INTERNAL_DIR", str(data_root / "internal"))),
        output=Path(os.environ.get("DATA_OUTPUT_DIR", str(data_root / "output"))),
    )
