import re

#Script for splitting inputfile into 200 line resulting files, with one file representing a document of text. Final files include start and stop of miRNA within the document.

#Regex function to search for miRNA/trigger word in the sentence and obtain the start and end position
#Input x is the sentence, y is an array including the miRNA(or trigger word) of interest
def getPosition(x,y):
    y=list(set(y)) #Get only unique miRNA from list
    dict = {}   #dictionary to store miRNA name and positions within sentence
    for i in y:
        pos_array=[]
        regex = r"\b"+re.escape(i)+r"\b"
        for match in re.finditer(regex,x):
            s=match.start()
            e=match.end() -1
            start_end=[s,e]
            pos_array.append(start_end)
        dict[i] = pos_array
    return dict


#Regex function to search for all instances of disease position in sentence
#x is sentence, y is disease name
def getDisease(x,y):
    disease_array=[]
    for match in re.finditer(y,x):
        s=match.start()
        e=match.end() -1
        se = [s,e]
        disease_array.append(se)
    return disease_array


#Open original file for reading
#If file is .XLSX, convert it to .txt (tab-separated file)
#Vim into tab delimited file and type :%s/\r/\r/g in order to check that set list has correct new line characters in original file
orig_file = open("practice.txt","r")

count = 1 #initialize count of every 200 line document
docu_length = 0 #initialize length of 200 line document
file_number = 1   #initialize first file number
fileName = "file"+str(file_number)
toWrite = open(fileName,'w')
firstLine = "Row#\tStart\tEnd\tType\tName\n"
toWrite.write(firstLine)

for line in orig_file:
    if not line.startswith("Sentence"):
        data = line.split("\t")     #split line on tab in order to access separate cells of information
        row = data[0]
        sentence = data[1]
        mrna=data[2]
        mir=mrna.split("|")
        trig=data[3]
        trigger=trig.split("|")
        disease = data[4]
        if(count < 5):      #loop through every 200 lines at a time
            this_length = len(sentence)
            result = getPosition(sentence,mir)
            for key in result:
                array_position = result[key]
                for pos in array_position:
                    start = docu_length + pos[0]
                    end = docu_length + pos[1]
                    newLine = row,start,end,"miRNA",key
                    toWrite.write('\t'.join(map(str,newLine))+'\n')

            trig_result = getPosition(sentence,trigger)

            for trig_key in trig_result:
                trig_value = trig_result[trig_key]
                for trig_pos in trig_value:
                    start = docu_length + trig_pos[0]
                    end = docu_length + trig_pos[1]
                    newLine = row,start,end,"Trigger Word",trig_key
                    toWrite.write('\t'.join(map(str,newLine))+'\n')

            docu_length = docu_length + this_length     #update docu_length
            count +=1
        else:
            toWrite.close()
            docu_length = 0 #Reset at zero for next 200 lines to begin
            this_length = len(sentence)
            count =1
            file_number += 1
            fileName = "file"+str(file_number)
            toWrite = open(fileName,'w')
            toWrite.write(firstLine)
            result = getPosition(sentence,mir)
            for key in result:
                array_position = result[key]
                for pos in array_position:
                    start = docu_length + pos[0]
                    end = docu_length + pos[1]
                    newLine = row,start,end,"miRNA",key
                    toWrite.write('\t'.join(map(str,newLine))+'\n')

            trig_result = getPosition(sentence,trigger)
            for trig_key in trig_result:
                trig_value = trig_result[trig_key]
                for trig_pos in trig_value:
                    start = docu_length + trig_pos[0]
                    end = docu_length + trig_pos[1]
                    newLine = row,start,end,"Trigger Word",trig_key
                    toWrite.write('\t'.join(map(str,newLine))+'\n')



            docu_length = docu_length + this_length
            count +=1
