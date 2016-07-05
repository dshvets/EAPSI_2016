import re 

#Script for splitting inputfile into 200 line resulting files, with one file representing a document of text. Final files include start and stop of miRNA within the document. 

#Reg-ex function to search for miRNA in the sentence and obtain the start and end position
#Input x is the sentence, y is an array including the miRNA of interest
def getPosition(x,y):
    y=list(set(y)) #Get only unique miRNA from list
    dict = {}   #dictionary to store miRNA name and positions within sentence 
    for i in y:
        pos_array=[]
        regex = r"\b"+re.escape(i)+r"\b"
        for match in re.finditer(regex,x):
            s=match.start()
            e=match.end()
            start_end=[s,e]
            pos_array.append(start_end)
        dict[i] = pos_array 
    return dict 

#Open original file for reading 
#If file is .XLSX, convert it to .Txt (tab-separated file)
#Check that set list has correct new line characters in original file 
orig_file = open("practice.txt","r")

count = 1 #initialize count of every 200 line document 
docu_length = 0 #initialize length of 200 line document 


file_number = 1
fileName = "file"+str(file_number)
toWrite = open(fileName,'w')


for line in orig_file:
    if not line.startswith("Sentence"):
        data = line.split("\t")     #split line on tab in order to access separate cells of information
        row = data[0]
        sentence = data[1]
        mrna=data[2]
        mir=mrna.split("|")
        if(count < 5):      #loop through every 200 lines at a time 
            toWrite.write(row)
            this_length = len(line)
            docu_length = docu_length + this_length #Update docu_length 
            #result = getPosition(sentence,mir)
            count +=1
        else:
            toWrite.close()
            docu_length = 0 #Reset at zero for next 200 lines to begin
            this_length = len(line)
            docu_length = docu_length + this_length #update docu_length
            count =1
            file_number += 1
            fileName = "file"+str(file_number)
            toWrite = open(fileName,'w')
            toWrite.write(row)
            count +=1





