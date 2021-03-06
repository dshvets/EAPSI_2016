import re
from pycorenlp import StanfordCoreNLP

#use python wrapper to call StanfordCoreNLP in order to perform POS tagging on miRNA-disease related abstracts

orig_file = open("split_file.txt",'r')
newFile = open("result_POS.txt",'w')
firstLine = "PMID\tType\tSentence\tPOStags\n"
newFile.write(firstLine)

#function looks for all POS + word pairs and combines them into one string
def extractPOS(x):
    sampleSearch = re.findall("([A-Z]+ [A-Za-z]+)",x)
    sampleCapture = ','.join(sampleSearch)
    return sampleCapture

#extract word from POS+word pair
def extractWord(x):
    getWord = re.search("[A-Z]+ ([A-Za-z]+)",x)
    word = getWord.group(1)
    return word

#extract POS from POS+word pair
def getPOSback(x):
    searchPOS = re.search("([A-Z]+) [A-Za-z]+",x)
    capturePOS = searchPOS.group(1)
    return capturePOS

#given a word it searches the original abstract sentence for it to find the biological match
#x = word y = abstract sentence
def searchSentence(x,y):
    findMatch = re.search((r"\b"+re.escape(x)+ r"-[0-9]+"),y)
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
        z = getPOSback(i)
        trueWord = searchSentence(y,abs_sentence)
        newPOSpair = z + " " + trueWord
        newPOS.append(newPOSpair)
    newString = ','.join(newPOS)
    return newString

#Change brackets [] in sentence to () so that POS tagger doesn't crash
def removeBracket(x):
    findBracket = re.search('\[|\]',x)
    if findBracket:
        x = re.sub('\[','(',x)
        x = re.sub('\]',')',x)
        return x
    else:
        return x

#tagger keeps freaking out at numbers in parentheses. this function removes the parentheses
def removeParenth(x):
    findParenth = re.search('\([0-9]+\)',x)
    if findParenth:
        x = re.sub('\(','',x)
        x = re.sub('\)','',x)
        return x
    else:
        return x


if __name__ == '__main__':
    nlp = StanfordCoreNLP('http://localhost:9000')

    for line in orig_file:
        if not line.startswith("PMID"):
            info = line.split('\t')
            pmid = info[0]
            ta = info[1]
            sentence = info[2]
            sentence = sentence.rstrip('\n')
            cleanSentence = removeBracket(sentence)
            extraClean = removeParenth(cleanSentence)
            output =  nlp.annotate(extraClean,properties={
            'annotators':'tokenize,ssplit,pos,depparse,parse',
            'outputFormat' : 'json'})
            try:
                result = output['sentences'][0]['parse']
                getPOS = extractPOS(result)
                fixBioName_POS = bioName(getPOS,sentence)
                newLine = pmid+'\t'+ta+'\t'+sentence+'\t'+fixBioName_POS+'\n'
                newFile.write(newLine)
            except:
                pass



orig_file.close()
newFile.close()
