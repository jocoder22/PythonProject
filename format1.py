#!/usr/bin/env python

city = ["New York", "Newark", "Chicago", "Maima", "Baltimore",
        "New Park", "Texas New City", "Kens Dews", "Portland"]

for index, value in enumerate(city):
    print("Location: {0:30}  Miles: {1:6}000 {2:20}".format(value, index+1, "Example I"))
    print("Location: %-*s Miles: %s000  %s" %(20, value, index, "Example II"))
    print("Location: {}".format(value).ljust(40) + "  Miles: {}0000".format(index))
    print("Location: {}\t Miles: {}000".format(value, index).expandtabs(30))

print ('Location:10-10-10-10\tRevision: 1'.expandtabs(30))
print("Location: {0:20}  Miles: {1:6}000 {2:15} John".format("value", "index", "Example I"))