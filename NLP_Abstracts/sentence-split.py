import re



orig_file = open("Q1_selected_PMID.txt",'r')

newFile = open("split_file.txt",'w')
firstLine = "PMID\tType\tSentence\n"
newFile.write(firstLine)

for line in orig_file:
    if not line.startswith("PMID"):
        data = line.split("\t")
        pmid = data[0]
        title = data[1]
        text = data[2]
        split_text = re.split(r'(?<=\.) ',text) #split where there is a period followed by a space
        titleLine = pmid+'\tT\t'+title+'\n'
        newFile.write(titleLine)
        for x in split_text:
            abstractLine = pmid+'\tA\t'+x+'\n'
            newFile.write(abstractLine)



orig_file.close()
newFile.close()
