import csv
from itertools import izip

reader = csv.reader(open("contacts.csv", "rb"), csv.excel)

row = reader.next()
keys = row

out = []
counts = {}
for row in reader:
    property = iter(row)
    data = {}
    for key in keys:
        keyval = property.next()
        if "Priority" != key:
            if len(keyval) > 0:
                data[key] = keyval
                counts[key] = counts.get(key, 0) + 1
    out += [data]
print out
print counts


