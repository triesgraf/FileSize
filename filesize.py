#Import modules
import sys
import os
import json
import operator

#Verify that parameter was provided
try:
    folder_path = str(sys.argv[1])
except IndexError:
    print ("Missing argument for Mount point")
    sys.exit()

#Verify that folder_path exists
if not os.path.exists(folder_path):
    print (folder_path + " is not a valid directory")
    sys.exit()

#Create a dictionary to store file path and file sizes
fileinfo = dict()

#Walk through all directories and files under given folder
for root, dirs, files in os.walk(folder_path):
   for file in files:
      path = os.path.join(root, file)   #Join current path with current file
      size = os.path.getsize(path)      #Get size of current file
      fileinfo.update({path: size})     #Add current path/file and current size to the dictionary

#Sort by filesize
sorted_fileinfo = sorted(fileinfo.items(), key=operator.itemgetter(1),reverse=True)
#Print out all file locations and sizes
print (json.dumps(sorted_fileinfo, indent=1))
