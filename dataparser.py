import sys

fileToRead = "stats.txt"
formatSpecified = "-x"

if len(sys.argv) != 3:
    print("ERROR: Invalid arguments\nPlease format command as <input file> -output-type")
    exit()
fileToRead = sys.argv[1]
formatSpecified = sys.argv[2]

infile = open(fileToRead)
lines = infile.read().strip('\r\n').splitlines()
infile.close

numberOfColumns = len(lines[0].split('\t'))
data = [[0]*numberOfColumns for i in range(len(lines))]

for i in range(len(lines)):
    entries = lines[i].split('\t')
    for e in range(len(entries)):
        data[i][e] = (entries[e])
#data is now stored as data[iterable][catagory]

if formatSpecified == "-c":
    #output data as csv file
    outfile = open('./output.csv', 'w')
    for i in range(len(data)):
        for j in range(len(data[i])):
            outfile.write("%s,"%data[i][j])
        outfile.write("\n")
    outfile.close
    
elif formatSpecified == "-j":
    #output data as json file
    outfile = open('./output.json', 'w')
    outfile.write("[\n")
    for i in range(1,len(data)):
        outfile.write("\t{\n")
        for j in range(len(data[i])-1):
            outfile.write("\t\t\"%s\": \"%s\",\n" %(data[0][j], data[i][j]))
        outfile.write("\t\t\"%s\": \"%s\"\n" %(data[0][len(data[i])-1], data[i][len(data[i])-1]))
        outfile.write("\t}")
        if i < len(data)-1:
            outfile.write(",")
        outfile.write("\n")
    outfile.write("]\n")
    outfile.close

elif formatSpecified == "-x":
    #output data as XML file
    outfile = open('./output.xml', 'w')
    outfile.write("<root>\n")
    for i in range(1,len(data)):
        outfile.write("\t<row>\n")
        for j in range(len(data[i])):
            outfile.write("\t\t<%s>%s</%s>\n" %(data[0][j], data[i][j], data[0][j]))
        outfile.write("\t</row>\n")
    outfile.write("</root>")
    outfile.close
