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

## Usage

### Set up accounts
Create an `accounts.json` file with the following format

```json
{
  "AccountNumber1": "TFSA",
  "7892754938254": "401K"
}
```

Create a folder consisting of only the files you wish to rename.

Run: `python3 app.py path_to_input_directory`