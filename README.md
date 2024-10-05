# Py-playground

Just some small try outs to learn the language Python and compare it with other languages I know.

## General Setup

Some packages contains a `requirement.txt` with containing the dependencies. It's generally recommended to install them into a specific environment:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

Some packages contains test code. It can be run via:

```sh
python -m unittest discover -p "*_test.py"
```

## Packages

### Pocket Money

Calculates how many pocket money you get from a start date to now.

### Wrong Number

Determines a wrong number in a row (influenced by math homework). It implements two different algorithms (one with raw python, the other with numpy).
