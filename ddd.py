s0=[]
with open('students_utf8.csv') as f:
    for line in f.readlines():
        s=line.strip().split(',')
        s0.append(s)
z=s0[0]
import csv
with open('new.csv', 'w', newline='') as csvfile:
    filewriter=csv.writer(csvfile, delimiter=',',
    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(z)
    for x in range(len(s0)-1,-1,-1):
        filewriter.writerow(s0[x])

