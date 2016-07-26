import requests
import re

#script uses PubTator API in order to access the information of the disease
#that is discussed in each abstract

#takes text from PubTator as input, returns list of all diseases present in abstract
def getDisease(x):
    sampleSearch = re.findall("([A-Za-z0-9- ]+)\tDisease",x)
    unique_disease = list(set(sampleSearch))
    unique = [x.encode('utf-8') for x in unique_disease]
    return unique

#takes list as input, removes non-specific terms "cancer,tumor,disease"
def removeCancer(x):
    remove_cancer = []
    for i in x:
        cancerCheck = bool(re.search("^cancer$|^cancers$",i))
        if cancerCheck == False:
            remove_cancer.append(i)
    return remove_cancer

def removeDisease(x):
    remove_disease = []
    for i in x:
        diseaseCheck = bool(re.search("^disease$|^diseases$",i))
        if diseaseCheck == False:
            remove_disease.append(i)
    return remove_disease

def removeTumor(x):
    remove_tumor = []
    for i in x:
        tumorCheck = bool(re.search("^tumor$|^tumour$|^Tumor$|^Tumors$|^tumours$|^tumors$",i))
        if tumorCheck == False:
            remove_tumor.append(i)
    return remove_tumor


classifiedFile = open("classified_data.txt",'r')

for line in classifiedFile:
    line = line.split('\t')
    pmid = line[0]      #use PubMed ID to search disease type with PubTator API
    sent = line[1]
    groupType = line[2]
    url = "http://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/Disease/"+pmid+"/PubTator/"
    r = requests.get(url)
    text = r.text
    try:
        disease = getDisease(text)
        noCancer = removeCancer(disease)
        noDisease = removeDisease(noCancer)
        noTumor = removeTumor(noDisease)

        
    except:
        pass


classifiedFile.close()
