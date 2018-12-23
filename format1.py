#!/usr/bin/env python

city = ["New York", "Newark", "Chicago", "Maima", "Baltimore",
        "New Park", "Texas New City", "Kens Dews", "Portland"]

for index, value in enumerate(city):
    print("Location: {:30}  Miles: {}000".format(value, index))
    print("Location: %-*s Miles: %s000" %(20, value, index))
    print("Location: {}".format(value).ljust(40) + "  Miles: {}0000".format(index))