import csv
from pymongo import Connection
from itertools import izip

# connect to mongo
connection = Connection("192.168.1.200", 27017)
db = connection.contacts
gcol = db.gcontacts


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
                data[key] = keyval.decode("utf-8", "replace")
                counts[key] = counts.get(key, 0) + 1
    print "About to insert into Mongo:"
    print data
    print "Inserted"
    gcol.insert(data)
    out += [data]
print out

print "totals:"
print counts


