import re 

#Script for splitting inputfile into 200 line resulting files, with one file representing a document of text. Final files include start and stop of miRNA within the document. 


#Reg-ex function to search for miRNA in the sentence and obtain the start and end position
#Input x is the sentence, y is an array including the miRNA of interest
def getPosition(x,y):
    dict = {}   #dictionary to store miRNA name and positions within sentence 
    for i in y:
        for match in re.finditer(i,x):
            s=match.start()
            e=match.end()
            start_end=[[s,e]]
            if i not in dict:
                dict[i]=start_end
    return dict 
        


#Open original file for reading 
#If file is .XLSX, convert it to .Txt (tab-separated file)
#Check that set list has correct new line characters in original file 
orig_file = open("practice.txt","r")

count = 1 #initialize count of every 200 line document 
for line in orig_file:
    if not line.startswith("Sentence"):
        data = line.split("\t")     #split line on tab in order to access separate cells of information
        sentence = data[1]
        mrna=data[2]
        mir=mrna.split("|")
        if(count < 5):      #loop through every 200 lines at a time 
            print sentence 
            print mir 
            result = getPosition(sentence,mir)
            print result 
            #print count
            count +=1
        else:
            count =1
            #print mir
            #print count 
            count +=1
            #data = line.split("\t")
            #sentence = data[1]
            #mir = data[2]
            #print mir





