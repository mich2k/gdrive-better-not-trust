#@title Check if the file integrity is preserved between src & target folders
from google.colab import drive
import os
import hashlib

print('Mounting Google Drive...')
drive.mount('/gdrive')

src_path = '/gdrive/MyDrive/Source_Path_Here' #@param {type: 'string'}
assert os.path.exists(src_path), f"Source '{src_path}' doesn't exist!"

target_path = '/gdrive/MyDrive/Target_Path_Here' #@param {type: 'string'}
assert os.path.exists(target_path), f"Target '{target_path}' doesn't exist!"

i=0


for item1 in os.listdir(src_path):
  print("Analizzo " + str(i+1) + " elemento")
  item2 = os.listdir(target_path)[i]
  with open(src_path + "/" + item1,"rb") as f1:
    with open(target_path + "/" + item2, "rb") as f2:
      bytes = f1.read()
      hash1 = hashlib.sha256(bytes).hexdigest();
      bytes = f2.read()
      hash2 = hashlib.sha256(bytes).hexdigest();
  if hash1 == hash2:
    print("Compatibili")  
  i=i+1

print("Fine analisi su " + str(i+1) + " elementi")

