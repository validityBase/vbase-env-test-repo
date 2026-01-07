# Test Repository for vbase_env_runner

This is a mock repository for testing the vbase_env_runner system, following Python best practices.

## Project Structure

```
vbase-env-test-repo/
├── src/                    # Source code directory
│   ├── __init__.py        # Package initialization
│   ├── sample_pipeline.py # Main entrypoint script
│   ├── simple_script.py   # Simple test script
│   ├── complex_script.py  # Pandas-based test script
│   └── data_processor.py  # Data processing utility
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Usage

The main entrypoint is `src/sample_pipeline.py` which:
- Processes sample data
- Generates output files
- Logs execution progress with proper logging

### Running Scripts

```bash
# Run the main pipeline
python src/sample_pipeline.py

# Run simple test script
python src/simple_script.py

# Run complex pandas script
python src/complex_script.py

# Run data processor
python src/data_processor.py
```

## Expected Outputs

When running under **vbase_env_runner** inside a container:

- `/data/output/result.txt` - Text summary
- `/data/output/results.json` - JSON results
- `/data/output/data.csv` - CSV data export
- `/data/logs/processing.log` - Processing logs

On the host, these map to:

- `<BASE_DIR>/data/<ENV_ID>/output/result.txt`
- `<BASE_DIR>/data/<ENV_ID>/output/results.json`
- `<BASE_DIR>/data/<ENV_ID>/output/data.csv`
- `<BASE_DIR>/data/<ENV_ID>/logs/processing.log`

By default `BASE_DIR` is `/opt/vbase-envs`. The repository code is stored at `<BASE_DIR>/repos/<ENV_ID>/` on the host and mounted as `/repo` in the container.

For **local runs outside containers**, you can set `VBASE_DATA_ROOT` to write into the project directory instead of `/data`, for example:

```bash
VBASE_DATA_ROOT=. python src/sample_pipeline.py
```

This will create:

- `./output/result.txt`
- `./output/results.json`
- `./output/data.csv`
- `./logs/processing.log`

## Environment Variables

- `ENV_ID` - Environment identifier
- `ENTRYPOINT_ARGS` - Additional arguments
