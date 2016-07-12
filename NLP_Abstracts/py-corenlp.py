import re
from pycorenlp import StanfordCoreNLP

#use python wrapper to call StanfordCoreNLP in order to perform POS tagging on miRNA-disease related abstracts

orig_file = open("example.txt",'r')
newFile = open("POS_tags.txt",'w')
firstLine = "PMID\tType\tSentence\tPOStags\n"
newFile.write(firstLine)

#function looks for all POS + word pairs and combines them into one string
def extractPOS(x):
    sampleSearch = re.findall("([A-Z]+ [A-Za-z]+)",x)
    sampleCapture = ','.join(sampleSearch)
    return sampleCapture


def extractWord(x):
    getWord = re.search("[A-Z]+ ([A-Za-z]+)",x)
    word = getWord.group(1)
    return word

#given a word it searches the original abstract sentence for it to find the biological match
#x = word y = abstract sentence
def searchSentence(x,y):
    findMatch = re.search((re.escape(x)+ r"-[0-9]+"),y)
    if findMatch:
        capture = findMatch.group(0)
        return capture
    else:
        return x


#Takes as input a sentence with each POS tag+word pair separated by a comma and searches for gene/miRNA match in the abstract sentence
def bioName(orig_POS,abs_sentence):
    newPOS = []   #new POS sentence that will have mir changed to mir-45, etc.
    split_POS = orig_POS.split(',')
    for i in split_POS:
        y = extractWord(i)
        trueWord = searchSentence(y,abs_sentence)
        newPOS.append(trueWord)
    newString = ','.join(newPOS)
    return newString 



if __name__ == '__main__':
    nlp = StanfordCoreNLP('http://localhost:9000')

    for line in orig_file:
        if not line.startswith("PMID"):
            info = line.split('\t')
            pmid = info[0]
            ta = info[1]
            sentence = info[2]
            sentence = sentence.rstrip('\n')
            output =  nlp.annotate(sentence,properties={
            'annotators':'tokenize,ssplit,pos,depparse,parse',
            'outputFormat' : 'json'})
            result = (output['sentences'][0]['parse'])
            getPOS = extractPOS(result)
            print getPOS
            testing_POS = bioName(getPOS,sentence)
            print testing_POS
            #newLine = pmid+'\t'+ta+'\t'+sentence+'\t'+testing_POS+'\n'
            #newFile.write(newLine)



orig_file.close()
newFile.close()
