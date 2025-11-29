import re
import sys
import os

def get_filepath() -> str:
  if len(sys.argv) < 2:
    print("Error: No file provided.")
    print("Usage: python __init__.py <file>")
    sys.exit(1)
  
  file_path = sys.argv[1]
  
  if not os.path.isfile(file_path):
    print(f"Error: '{file_path}' is not a valid file")
    sys.exit(1)
  
  return file_path  

def parse_album_headers(raw_album_info: str):
  album_headers = {}
  header_pattern = re.compile(r'\[(.*?)\]\s+(.+)')
  
  for line in raw_album_info.splitlines():
    match = header_pattern.match(line)
    if match and not match.group(1).isdigit():
      key, value = match.groups()
      album_headers[key] = value.strip()
  
  return album_headers

def parse_album_info(raw_album_info: str):
  album_info = {}
  tracks = []
  
  track_pattern = re.compile(r'\[(\d+)\]\s+(.+)')

def __init__():
  file_path = get_filepath()
  with open(file_path, "r") as file:
    raw_album_info = file.read()
    
  
  
  