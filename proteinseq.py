import sys
fname = "small-genome.fasta" if len(sys.argv) < 2  else str(sys.argv[1])
#print ("File Name: %s" % fname)

x = open(fname,"r")
a = x.read()

# skip the first line from fasta file
b = a.split('\n',1)[1]
seq = b.replace("\n","")

#seq = "ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA"

text = ""

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


# print (dict["ATG"])
for i in range(0, len(seq), 3): 
  trp = seq[i:i+3]
  if (len(trp) == 3): 
    text += (dict[seq[i:i+3]])
print(text)
