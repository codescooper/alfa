# alfa
Simple app to learn Alphabet, Click on a letter an hear his prononciation, tell a letter and see how to write it.

## Cuniculture Manager

This repository also includes a simple command line tool to manage a rabbit farm and track resources and waste generated during operations.

### Usage

The script `cuniculture_manager.py` stores its data in `cuniculture_data.json` (created automatically if missing). Run `python cuniculture_manager.py -h` to see all available commands.

Example commands:

```bash
# Add a new rabbit
python cuniculture_manager.py add-rabbit "Rex" "Cage A" 5

# Record resource usage
python cuniculture_manager.py add-resource feed 10 kg

# Record waste output
python cuniculture_manager.py add-waste manure 3 kg

# List data
python cuniculture_manager.py list-rabbits
python cuniculture_manager.py list-resources
python cuniculture_manager.py list-waste
```
