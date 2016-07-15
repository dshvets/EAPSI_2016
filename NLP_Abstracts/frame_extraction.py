import re

#script for extracting the six association patterns from the abstracts that have been POS tagged
orig_file = open("small_pos.txt",'r')
newFile = open("frame_patterns.txt",'w')
firstLine = "Pattern\tText\n"
newFile.write(firstLine)

#array containing the POS tags of interest from the miRiaD paper
match_array = ["VBD,VBN,IN","VBZ,VBN,IN","NNS,IN","VBZ,IN","VBZ,TO","VBZ,JJ,IN","VBZ,DT,NN,IN"]

#take as input array of POS tag-word pairs
#returns an array of arrys which contains results
def matchFrame(x):
    pos_index = ""
    cut_off = len(x) - 5
    for i in range(0,cut_off,2):
        next_i = i + 2
        final_i = i + 4
        pos_index = pos_index + str(i) + ','
        sample_triplet = x[i] + ',' + x[next_i] + ',' + x[final_i]    #sample frame to be compared to array containing POS tags of interest
        sample_double = x[i] + ',' + x[next_i]
        if sample_double in match_array:
            print("double")
            print(sample_double)
        if sample_triplet in match_array:
            print("triplet")
            print(sample_triplet)
    pos_index = pos_index[:-1]
    #return pos_index






for line in orig_file:
    if not line.startswith("PMID"):
        data = line.split('\t')
        pos = data[3]
        pos = pos.rstrip('\n')
        pos_string = pos.replace(" ",",")
        pos_array = pos_string.split(',')
        result = matchFrame(pos_array)
        print result




orig_file.close()
newFile.close()
