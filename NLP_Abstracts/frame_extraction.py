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
    final_array =[]
    pos_index = ""
    cut_off = len(x) - 5
    for i in range(0,cut_off,2):
        next_i = i + 2
        final_i = i + 4
        sample_triplet = x[i] + ',' + x[next_i] + ',' + x[final_i]    #sample frame to be compared to array containing POS tags of interest
        sample_double = x[i] + ',' + x[next_i]
        if sample_double in match_array:
            word_double = x[i+1]+','+x[next_i+1]
            double_add = [sample_double, word_double]
            final_array.append(double_add)
        if sample_triplet in match_array:
            word_triplet = x[i+1]+','+x[next_i+1] +',' + x[final_i+1]
            triplet_add = [sample_triplet,word_triplet]
            final_array.append(triplet_add)
    return final_array


for line in orig_file:
    if not line.startswith("PMID"):
        data = line.split('\t')
        pos = data[3]
        pos = pos.rstrip('\n')
        pos_string = pos.replace(" ",",")
        pos_array = pos_string.split(',')
        result = matchFrame(pos_array)
        if not result:
            pass
        else:
            for x in result:
                x_string = '\t'.join(x)
                x_string = x_string + '\n'
                newFile.write(x_string)

orig_file.close()
newFile.close()
