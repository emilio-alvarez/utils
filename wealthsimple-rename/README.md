# Wealthsimple Renaming Utility

This utility renames wealthsimple trade confirmations based on their contents.

Converts filenames like `TRADE_CONFIRM_4873294732_TSLA _order-57894hfi32.pdf` into `Account-TSLA-2023-07-09`.

## Setup

### Requirements
- pip3
  ```
  sudo apt install python3-pip python3.10-venv
  python3 -m pip install --user --upgrade pip
  ```
- venv
  ```
  python3 -m pip install --user virtualenv
  ```

### Create a virtual environment

```
python3 -m venv .venv
```

### Start virtual environment

```
source .venv/bin/activate
```

### Install requirements

```
python3 -m pip install -r requirements.txt
```

# Notes

## Required data
- Account mapping (number -> desired file account name)
  - id in the original file name
  - desired file account name in env mapping
- Ticker symbol
  - in original file name after `TRADE_CONFIRM_ID_TICKER`
- Settlement date
  - in pdf after `For Settlement On:`

## Command line arguments
- input directory