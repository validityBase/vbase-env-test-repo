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

- `output/result.txt` - Text summary
- `output/results.json` - JSON results
- `output/data.csv` - CSV data export
- `logs/processing.log` - Processing logs

## Environment Variables

- `ENV_ID` - Environment identifier
- `ENTRYPOINT_ARGS` - Additional arguments
