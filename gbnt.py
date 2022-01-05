#@title Check if the file integrity is preserved between src & target folders
from google.colab import drive
import os
import hashlib

print('Mounting Google Drive...')
drive.mount('/gdrive')
i=0

src_path = '/gdrive/MyDrive/src_here' #@param {type: 'string'}
assert os.path.exists(src_path), f"Source '{src_path}' doesn't exist!"

target_path = '/gdrive/MyDrive/dest_here' #@param {type: 'string'}
assert os.path.exists(target_path), f"Target '{target_path}' doesn't exist!"



for item1 in os.listdir(src_path):
  print("Checking " + str(i+1) + " element")
  item2 = os.listdir(target_path)[i]
  with open(src_path + "/" + item1,"rb") as f1:
    with open(target_path + "/" + item2, "rb") as f2:
      bytes = f1.read()
      hash1 = hashlib.md5(bytes).hexdigest();
      bytes = f2.read()
      hash2 = hashlib.md5(bytes).hexdigest();
      print(str(hash1) + " - " + str(hash2) )  
  if hash1 == hash2:
    print("\n\tChecksum verified")
  else:
    print("\n\tCorrupted or different file")
  i=i+1

print(str(i+1) + " elements have been checked")
