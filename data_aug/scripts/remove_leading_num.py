import csv
import sys

subgroup = sys.argv[1]

filename = subgroup + ".txt"
f = open(filename)
out = open(filename + "_out.txt", 'a')
contents = f.read()
contents = contents.split('\n')
for each in contents:
	each = each.lstrip('0123456789., ')
	out.write(each)
	out.write('\n')
out.close()
f.close()
