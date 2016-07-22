import sys
import re

#get the input file name in order to save the root of the name for future file names for easy recognition
def captureName(x):
    samSearch = re.search("([A-Za-z0-9_]+)\.txt",x)
    samCapture = samSearch.group(1)
    return samCapture


#Four classification groups from Gupta, et al miRiad paper
involve = ["involved in","implicated in","required for","needed for","plays a role in",
"necessary for","sufficient for","crucial for","dependent on","participates in",
"contributes to","influences","fosters","affects","allows","initiates"]
association = ["associated with","correlated with","linked to"]
is_a = ["is a","are a","acts as","functions as","serves as"]
found = ["found in","detected in","increased in","overexpressed in",
"highly expressed in","upregulated in","mutated in"]

#Lists for storing the 100 training sentences for each training group
involve_sent =[]
assoc_sent =[]
is_sent =[]
found_sent =[]


#Provide the input file which should contain every single abstract sentence per line
fileName = sys.argv[1]
getRoot = captureName(fileName)
newName = getRoot + '_for_testing.txt'
openFile = open(fileName,'r')
newFile = open(newName,'w')

for line in openFile:
    if not line.startswith('PMID'):
        data = line.split('\t')
        sent = data[2].rstrip('\n')
        if len(involve_sent) < 100 and any(x in sent for x in involve):
                involve_sent.append(sent)
        elif len(assoc_sent) < 100 and any(x in sent for x in association):
                assoc_sent.append(sent)
        elif len(is_sent) < 100 and any(x in sent for x in is_a):
                is_sent.append(sent)
        elif len(found_sent) < 100 and any(x in sent for x in found):
                found_sent.append(sent)
        else:
            newFile.write(line)

openFile.close()
newFile.close()


testingName = "testing_file.tsv"
testFile = open(testingName,'w')

for x in involve_sent:
    line = x + '\tinvolve\n'
    testFile.write(line)

for x in assoc_sent:
    line = x+'\tassoc\n'
    testFile.write(line)

for x in is_sent:
    line = x + '\tis\n'
    testFile.write(line)

for x in found_sent:
    line = x + '\tfound\n'
    testFile.write(line)

testFile.close()
