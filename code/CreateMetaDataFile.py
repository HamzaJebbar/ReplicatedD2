#Create a metadata file for MERLIN corpus data, listing all other proficiencylabels.
import os

'''
format:
Rating:
Overall CEFR rating: B1
Grammatical accuracy: B1
Orthography: B2
Vocabulary range: B1
Vocabulary control: B2
Coherence/Cohesion: B1
Sociolinguistic appropriateness: B1
'''
#Not using this
def list_to_dict(rlist):
    return dict(map(lambda s : s.replace(" ","_").split(':_'), rlist))


#Takes input folder, and stores metadata file for that folder.
def getMetaData(dirpath,inputdir,outpath):
        ratings_dict = {}
        files = os.listdir(os.path.join(dirpath,inputdir))
        fw = open(os.path.join(outpath),"w",  encoding="utf8")
        for file in files:
            #print(file)
            if file.endswith(".txt"):
                content = open(os.path.join(dirpath,inputdir,file),"r", encoding="utf8").read()
                ratings = content.split("Rating:")[1].split("\n\n")[0].strip().split("\n") #get all ratings in a list
                #join the list contents to a string, and remove white spaces and slashes in descriptions.
                fw.write(file.replace(".txt","")+","+",".join(ratings).replace(" ","").replace("/",""))
                fw.write("\n")

        fw.close()


def main():
    dirpath = r"../DataRaw/" #CZ_ltext_txt", DE_ltext_txt, IT_ltext_txt
    inputdirs = ["czech", "german", "italian"]
    outputnames = ["CZMetadata.txt","DEMetadata.txt","ITMetadata.txt"]
    outputdirpath = r"../Datasets/"
    for i in range(0, len(inputdirs)):
        outpath = os.path.join(outputdirpath,outputnames[i])
        getMetaData(dirpath,inputdirs[i],outpath)
        print("Wrote to: ", outpath)

main()
