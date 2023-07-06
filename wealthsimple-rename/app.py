import os
import sys
from dotenv import load_dotenv

def main():
  input_directory = "."
  if len(sys.argv) == 2:
    input_directory = sys.argv[1]

  if not os.path.isdir(input_directory):
    print("Specify a valid input directory")
    return

  directory = os.fsencode(input_directory)

  for file in os.listdir(input_directory):
    filename = os.fsdecode(file)
  
load_dotenv()
main()