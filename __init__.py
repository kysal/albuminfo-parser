import re
import sys
import os

def get_filepath(file_path):
  if len(sys.argv) < 2:
    print("Error: No file provided.")
    print("Usage: python __init__.py <file>")
    sys.exit(1)
  
  file_path = sys.argv[1]
  
  if not os.path.isfile(file_path):
    print(f"Error: '{file_path}' is not a valid file")
    sys.exit(1)
  
  return file_path  

def __init__():
  file_path = get_filepath()
  with open(file_path, "r") as file:
    raw_album_info = file.read()
    
  
  
  