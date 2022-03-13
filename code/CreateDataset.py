'''
Create a new dataset with new filenames, and removed metadata.
Renamed corpora are in the Datasets/ folder in this repo
Original corpora for all languages can be downloaded from MERLIN website
http://www.merlin-platform.eu/C_data.php
'''

import os

dirpath = r"../DataRaw/" #CZ_ltext_txt", DE_ltext_txt, IT_ltext_txt
outputdirpath = r"../Datasets/"
files = os.listdir(dirpath)
inputdirs = ["czech", "german", "italian"]
outputdirs = ["CZ","DE","IT"]

for i in range(0, len(inputdirs)):
    files = os.listdir(os.path.join(dirpath,inputdirs[i]))
    for file in files:
        print(file)
        if file.endswith(".txt"):
            content = open(os.path.join(dirpath,inputdirs[i],file),"r", encoding="utf8").read()
            cefr = content.split("Learner text:")[0].split("Overall CEFR rating: ")[1].split("\n")[0]
            newname = file.replace(".txt","") + "_" + outputdirs[i] + "_" + cefr + ".txt"
            fh = open(os.path.join(outputdirpath,outputdirs[i],newname), "w", encoding="utf8")
            text = content.split("Learner text:")[1].strip()
            fh.write(text) # Solutions
            print("wrote: ", os.path.join(outputdirpath,outputdirs[i],newname))
