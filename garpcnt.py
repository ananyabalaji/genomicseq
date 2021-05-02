import sys
fname = "Rotavirus Protein [completed].txt" if len(sys.argv) < 2  else str(sys.argv[1])
#print ("File Name: %s" % fname)

x = open(fname,"r")
a = x.read()
# skip the first line from fasta file
b = a.replace("*","")
seq = b.replace("\n","")

counter = {}

#seq = "GARPKKKAAA"

counter['G'] = 0
counter['A'] = 0
counter['R'] = 0
counter['P'] = 0

numOfChar = 0

for index in range(len(seq)):
                if (seq[index] in counter):
                    counter[seq[index]] = counter[seq[index]] + 1
                numOfChar+=1
d = {}
for keys in counter: 
	d[keys] = str(counter[keys]) 
	print(keys, d[keys])


#print(",".join(d.keys()), end=',PctGARP,Filename\n')
#print(",".join(d.values()), end=',')

#GARP Content Calc
garp = counter['G'] + counter['A'] + counter['R'] + counter['P']
content = (float(garp)/numOfChar)*100

#print("GARP content:" + str(content) + "%")
print(str(content) + "%" + "," + fname)
