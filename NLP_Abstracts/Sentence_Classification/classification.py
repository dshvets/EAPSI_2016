from textblob.classifiers import NaiveBayesClassifier

#Use Naive Bayes Classifier (from NLTK & textBlob) to classify each abstract sentence
#Into one of four relational groups (Involvement,Association,Is-A,Found-In)

#Train classifier with training data set 
train = open("training_data.tsv",'r')
cl = NaiveBayesClassifier(train, format="tsv")
train.close()

testing = open("testing_data.txt",'r')
classify = open("classified_data.txt",'w')

for line in testing:
    line = line.rstrip('\n')
    line = line.split('\t')
    pmid = line[0]
    sent = line[1]
    try:
        classify_result = cl.classify(sent)  #classify the sentence into one of four groups
        newLine = pmid+'\t'+sent+'\t'+classify_result+'\n'
        classify.write(newLine)
    except:
        pass
    #prob_dist = cl.prob_classify(line)  Might use this later for a future network graph.
    #assoc = round(prob_dist.prob("assoc"),2) For now will just use the highest probability match for each sentence.
    #found = round(prob_dist.prob("found"),2)
    #isA = round(prob_dist.prob("is"),2)
    #involve = round(prob_dist.prob("involve"),2)
    #newLine = line+'\tAssociation\t'+str(assoc)+'\tFoundIn\t'+str(found)+'\tIsA\t'+str(isA)+'\tInvolve\t'+str(involve)+'\n'


testing.close()
classify.close()
