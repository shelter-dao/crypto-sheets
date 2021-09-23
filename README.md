# Crypto Sheets

A tool for tracking crypto currency prices in Google sheets

## Development

1. Copy environment variables
```
$ cp .env.example .env
```

2. Set your API keys by using vim or another text editor to modify the `.env` file
```
vim .env
```

3. Install [poetry](https://python-poetry.org/)

4. Run scripts using `$ poetry run <command>`. Commands for running scripts are defined in `pyproject.toml`

```
# pyproject.toml

[tool.poetry.scripts]

# Find script command definitions here
# ...
```
