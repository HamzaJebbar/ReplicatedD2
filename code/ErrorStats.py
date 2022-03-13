"""
Purpose: Knowing error statistics in the data for DE and IT using LanguageTool
"""

import language_tool_python  # new package
import os, collections, pprint

def write_featurelist(file_path,some_list):
    print(file_path)
    fh = open(file_path, "w")
    for item in some_list:
      fh.write(item)
      fh.write("\n")
    fh.close()

def error_stats(inputpath,lang,output_path):
    files = os.listdir(inputpath)
    checker = language_tool_python.LanguageTool(lang)
    rules = {}
    categories = {}
    err = 0
    passed = 0
    for i,file in enumerate(files):
        if i%100 == 0:
            print(i)
        if file.endswith(".txt"):
            try :
                text = open(os.path.join(inputpath,file)).read()
                matches = checker.check(text)
                for match in matches:
                    rule = match.ruleId
                    #loc = match.locqualityissuetype
                    cat = match.category
                    rules[rule] = rules.get(rule,0) +1
                    #locqualityissuetypes[loc] = locqualityissuetypes.get(loc,0) +1
                    categories[cat] = categories.get(cat,0)+1
                    passed += 1
            except:
                err += 1
    print("PASSED:",passed)
    print("ERRORS:",err)
    write_featurelist(os.path.join(output_path,lang+"-rules.txt"), sorted(rules.keys()))
    #write_featurelist(output_path+lang+"-locquality.txt", sorted(locqualityissuetypes.keys()))
    write_featurelist(os.path.join(output_path,lang+"-errorcats.txt"), sorted(categories.keys()))
inputpath_de = r"../Datasets/DE/"
inputpath_it = r"../Datasets/IT/"
print(inputpath_de)
error_stats(inputpath_de, "de", r"../features/")
print("STATS DE")
print(inputpath_it)
error_stats(inputpath_it, "it",r"../features/")
print("STATS IT")
