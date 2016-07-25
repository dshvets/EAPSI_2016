import re
#script for creating the testing data set
#using the 4 manually curated files will build testing set where sentences match the patterns in the 4 curated files

file_array = ['../Associations.txt','../Is_A.txt','../Found_In.txt','../Involvement.txt']
assoc_list = []
involve_list = []
found_list = []
is_list = []

#get the double and triplet pattern from the file to be used for searching sentences in the abstracts
def getPattern(x):
    samSearch = re.search("[A-Z,]+\",\"([A-Za-z,]+)",x)
    samCapture = samSearch.group(1)
    return samCapture

assocFile = open('../Associations.txt','r')
for line in assocFile:
    result = getPattern(line)
    pattern = result.replace(',',' ')
    assoc_list.append(pattern)
assocFile.close()

isFile = open('../Is_A.txt','r')
for line in isFile:
    result = getPattern(line)
    pattern = result.replace(',',' ')
    is_list.append(pattern)
isFile.close()

foundFile = open('../Found_In.txt','r')
for line in foundFile:
    result = getPattern(line)
    pattern = result.replace(',',' ')
    found_list.append(pattern)
foundFile.close()

involveFile = open('../Involvement.txt','r')
for line in involveFile:
    result = getPattern(line)
    pattern = result.replace(',',' ')
    involve_list.append(pattern)
involveFile.close()

dataFile = open("split_file_for_testing.txt",'r')
testingFile = open("testing_data.txt",'w')
for line in dataFile:
    if not line.startswith('PMID'):
        data = line.split('\t')
        sent = data[2]
        if any(x in sent for x in involve_list) or any(x in sent for x in found_list) or any(x in sent for x in is_list) or any(x in sent for x in assoc_list):
            testingFile.write(sent)



dataFile.close()
testingFile.close()
