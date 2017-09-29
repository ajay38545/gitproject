d = dict()

d['xyz'] = 123
d['abc'] = 345

print d
print d.keys()
print d.values()

for i in d:
    print "%s %d" %(i, d[i])
for index, value in enumerate(d):
    print index, value , d[value]

print 'xyz' in d

del d['xyz']

print "xyz" in d
