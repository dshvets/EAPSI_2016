import re
from pycorenlp import StanfordCoreNLP

#use python wrapper to call StanfordCoreNLP in order to perform POS tagging on miRNA-disease related abstracts

orig_file = open("example.txt",'r')
newFile = open("POS_tags.txt",'w')
firstLine = "PMID\tType\tSentence\tPOStags\n"
newFile.write(firstLine)

def extractPOS(x):
    sampleSearch = re.findall("([A-Z]+ [A-Za-z]+)",x)
    sampleCapture = ','.join(sampleSearch)
    return sampleCapture

def bioName(word,sentence):


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
            newLine = pmid+'\t'+ta+'\t'+sentence+'\t'+getPOS+'\n'
            newFile.write(newLine)



orig_file.close()
newFile.close()
