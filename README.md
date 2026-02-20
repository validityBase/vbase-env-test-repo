# Test Repository for vbase_env_runner

This is a sample repository for testing the vbase_env_runner system, following Python best practices.

## Project Structure

```
vbase-env-test-repo/
├── src/                    # Source code directory
│   ├── __init__.py        # Package initialization
│   ├── sample_pipeline.py # Main entrypoint script (reads from /data/internal/, writes to /data/output/)
│   ├── simple_script.py   # Minimal test script
│   └── complex_script.py  # Pandas-based test script
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Usage

The main entrypoint is `src/sample_pipeline.py` which:
- Reads input data from `/data/internal/` (if available, falls back to default sample data)
- Processes the data
- Generates output files to `/data/output/`

### Running Scripts

```bash
# Run the main pipeline
python src/sample_pipeline.py

# Run simple test script
python src/simple_script.py

# Run complex pandas script
python src/complex_script.py
```

## Expected Outputs

When running under **vbase_env_runner** inside a container:

- `/data/output/result.txt` - Text summary
- `/data/output/results.json` - JSON results
- `/data/output/data.csv` - CSV data export

On the host, these map to:

- `<BASE_DIR>/data/<ENV_ID>/output/result.txt`
- `<BASE_DIR>/data/<ENV_ID>/output/results.json`
- `<BASE_DIR>/data/<ENV_ID>/output/data.csv`

where `<BASE_DIR>` is the root directory configured for vbase_env_runner (defaults to `/opt/vbase-envs-<DAGSTER_ENV>/` but can be set to other paths).

The repository code is stored at `<BASE_DIR>/repos/<ENV_ID>/` on the host and mounted as `/repo` in the container.

For **local runs outside containers**, set `DATA_ROOT` to write into a local directory instead of `/data`:

```bash
DATA_ROOT=. python src/sample_pipeline.py
```

This will create:

- `./output/result.txt`
- `./output/results.json`
- `./output/data.csv`

## Environment Variables

The following environment variables are automatically set by the vbase_env_runner container:

- `DATA_ROOT` - Root data directory (defaults to `/data`)
- `DATA_INTERNAL_DIR` - Persistent data directory for storing data between runs (`/data/internal/`)
- `DATA_OUTPUT_DIR` - Output directory for results accessed by the outside framework (`/data/output/`)
- `ENV_ID` - Environment identifier
- `ENTRYPOINT_ARGS` - Additional command-line arguments

## Internal Data

The `/data/internal/` directory is used to store persistent data between calls to the producer. The main pipeline (`src/sample_pipeline.py`) demonstrates reading input data from `/data/internal/input.json`. If this file exists, it is loaded and processed. Otherwise, default sample data is used.
