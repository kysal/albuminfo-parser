import re
import sys
import os
from pprint import pprint

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

def parse_album_info(raw_album_info: str):
  album_info = {
    "Discs": []
  }
  
  data_points = raw_album_info.splitlines()
  header_pattern = re.compile(r'\[(.*?)\]\s+(.+)')
  
  line_index = 0;
  
  # header details
  while data_points[line_index] != "":
    header_match = header_pattern.match(data_points[line_index])
    key, value = header_match.groups()
    album_info[key] = value.strip()
    line_index += 1
    
  line_index += 2
  
  # disc track details
  track_pattern = re.compile(r'\[(\d+)\]\s+(.+)')
  current_disc = []
  while line_index < len(data_points):
    if data_points[line_index][0] == "=":
      album_info["Discs"].append(current_disc)
      current_disc = []
      line_index += 1
      continue
    
    track_match = track_pattern.match(data_points[line_index])
    track_num, track_title = track_match.groups()
    current_disc.append({"TrackNumber": int(track_num), "Title": track_title})
    line_index += 1
    
  album_info["Discs"].append(current_disc)

  return album_info

if __name__ == "__main__":
  file_path = get_filepath()
  with open(file_path, "r") as file:
    raw_album_info = file.read()
    album_info = parse_album_info(raw_album_info)
    pprint(album_info)
  
  
  