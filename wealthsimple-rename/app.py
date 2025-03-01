import os
import sys
import json
import re
from pypdf import PdfReader

def load_accounts():
  accounts = {}

  with open("accounts.json") as file:
    accounts = json.load(file)

  return accounts

def extract_account_number(filename):
  # Get account number from file name
  return filename.split("_")[2].strip()

def extract_ticker(filename):
  # Get ticker from file name
  return filename.split("_")[3].strip()

def extract_settlement_date(filepath):
  # Get settlement date from file contents
  reader = PdfReader(filepath)
  page = reader.pages[0]
  for line in page.extract_text().split("\n"):
    if "For Settlement On" in line:
      return line.split(":")[1].strip()

def file_exists(filename):
  # Does the filename exist
  return os.path.isfile(filename)

def format_name(input_directory, account_number, ticker, settlement_date):
  # Interpolate the new file name
  # Loop until a unique filename is found
  file_collision = True
  iterations = 0
  account_name = accounts[account_number]
  name = "none.pdf"
  while file_collision:
    name = "{account_name}-{ticker}-{settlement_date}-{iterations}.pdf".format(**locals())

    file_collision = file_exists(os.path.join(input_directory, name))
    iterations += 1

  return name

def rename_file(input_directory, old_name, new_name):
  print("Renaming {old_name} -> {new_name}".format(**locals()))
  os.rename(
    os.path.join(input_directory, old_name),
    os.path.join(input_directory, new_name)
  )

def rename_files(input_directory):
  directory = os.fsencode(input_directory)

  for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if re.search("^.*-.*-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9].pdf", filename):
      continue
    filepath = os.path.join(input_directory, filename)

    account_number = extract_account_number(filename)
    ticker = extract_ticker(filename)
    settlement_date = extract_settlement_date(filepath)

    new_name = format_name(input_directory, account_number, ticker, settlement_date)

    rename_file(input_directory, filename, new_name)

def main():
  input_directory = "."
  if len(sys.argv) == 2:
    input_directory = sys.argv[1]

  if not os.path.isdir(input_directory):
    print("Specify a valid input directory")
    return

  rename_files(input_directory)

accounts = load_accounts()
main()
