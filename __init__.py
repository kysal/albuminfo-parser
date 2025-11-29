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

def parse_album_headers(raw_album_info: str):
  album_headers = {}
  header_pattern = re.compile(r'\[(.*?)\]\s+(.+)')
  
  for line in raw_album_info.splitlines():
    match = header_pattern.match(line)
    if match and not match.group(1).isdigit():
      key, value = match.groups()
      album_headers[key] = value.strip()
  
  return album_headers

def parse_album_tracks(raw_album_info: str):
  tracks = []
  track_pattern = re.compile(r'\[(\d+)\]\s+(.+)')
  
  for line in raw_album_info.splitlines():
    match = track_pattern.match(line)
    if match:
      track_num, track_title = match.groups()
      tracks.append({"TrackNumber": int(track_num), "Title": track_title})
  
  return tracks


def parse_album_info(raw_album_info: str):
  album_info = parse_album_headers(raw_album_info)
  tracks = parse_album_tracks(raw_album_info)
  album_info["Tracks"] = tracks
  
  return album_info

if __name__ == "__main__":
  file_path = get_filepath()
  with open(file_path, "r") as file:
    raw_album_info = file.read()
    album_info = parse_album_info(raw_album_info)
    pprint(album_info)
  
  
  