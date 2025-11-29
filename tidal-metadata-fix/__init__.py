from pprint import pprint
from album_info_parser import *

def get_directory() -> str:
  if len(sys.argv) < 2:
    print("Error: No directory provided.")
    print("Usage: python __init__.py <album-directory>")
    sys.exit(1)
  
  file_dir = sys.argv[1]
  
  if not os.path.isdir(file_dir):
    print(f"Error: '{file_dir}' is not a valid file directory")
    sys.exit(1)
  
  return file_dir  

if __name__ == "__main__":
  dir = get_directory()
  print(dir)
  with open(dir + "/AlbumInfo.txt", "r") as file:
    raw_album_info = file.read()
    album_info = parse_album_info(raw_album_info)
    pprint(album_info)
  
  
  