# Usage

## File

File provides a quick and convienient class for editing a file inplace without the need for any context managers. Saves a few lines of code.

```python
from pyparseedit import File

f = File('./hello_world.txt')
contents: str = f.read()  # This does not produce anything to clean up! No .close needed

# Do some arbitrary work on the string
contents = edit(contents)

# Overwrite the file with contents
# Automatically produces a backup file './hello_world.txt.bk'
# Will not overwrite './hello_world.txt.bk' if it exists. Will error out.
# This does not produce anything to clean up! No .close needed
f.write(contents)
```

## PyParsing Aliases

```python
from pyparseedit.aliases import *
```

Produces a set of aliases to common pyparsing types.

* `Literal`: `L`
* `Word`: `W`

# Installation for Development

```
# Create virtual environment and activate
python3 -m venv .venv
. ./.venv/bin/activate

# Install requirements
pip install -r requirements.txt
pip install -r dev_requirements.txt

# Set up pre-commit
pre-commit install
```
