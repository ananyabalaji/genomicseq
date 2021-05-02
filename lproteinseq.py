import sys
fname = "small-genome.fasta" if len(sys.argv) < 2  else str(sys.argv[1])
#print ("File Name: %s" % fname)

x = open(fname,"r")
a = x.read()

# skip the first line from fasta file
b = a.split('\n',1)[1]
seq = b.replace("\n","")

array = []
proSeq = ""
text = ""
endIndx = []



dict = {
"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L", 
"CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L", 
"ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M", 
"GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V", 
"TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", 
"CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P", 
"ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T", 
"GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A", 
"TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*", 
"CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"H", 
"AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
"GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E", 
"TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W", 
"CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", 
"AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R", 
"GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"}



for y in range(0,3,1):
        begIndex = y
        # print (dict["ATG"])
        for i in range(y, len(seq), 3):
                #print(dict[seq[i:i+3]])
                if((i+3) <= len(seq)):
                        text += (dict[seq[i:i+3]] )
                        if (dict[seq[i:i+3]] == "*"):
#                               print(i+3)
                                endIndx.append(i+3)
                                array.append(text)
                                text = ""
      
        #print(array)
        for i in range (len(array)):
                if (len(array[i]) > 100):
                        print(array[i])
                        bgn = endIndx[i] - 3*len(array[i])
#                        print("Start: " + str(bgn))
#                        print("End: " + str(endIndx[i]))
#                       print(seq[bgn:endIndx[i]])
#                        print("Length: " + str(len(array[i])))

        array = []
        endIndx = []
        text = ""
