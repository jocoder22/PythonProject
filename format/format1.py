#!/usr/bin/env python

city = ["New York", "Newark", "Chicago", "Maima", "Baltimore",
        "New Park", "Texas New City", "Kens Dews", "Portland"]

for index, value in enumerate(city):
    print("Location: {0:30}  Miles: {1:6}000 {2:6}".format(value, index+1, "Example I"))
    print("Location: %-*s Miles: %s000  %s" %(20, value, index, "Example II"))
    print("Location: {}".format(value).ljust(40) + "  Miles: {}0000".format(index))
    print("Location: {}\t Miles: {}000".format(value, index).expandtabs(30))


# adding tab ==> \t
print ('Location:10-10-10-10\tRevision: 1'.expandtabs(30))
print("Location: {0:20}  Miles: {1:6}000 {2:15} John".format("value", "index", "Example I"))

electronics = {'Microwave': 230,
              'Cellphone': 780,
               'Printer': 150,
               'Radio': 89}

# print one liner, returns the values of a dict
print('{Microwave} {Radio} {Cellphone} {Printer}'.format(**electronics))
mytuple = '{Microwave} {Radio} {Cellphone} {Printer}'.format(**electronics)
print(mytuple)
print(type(mytuple)) # ==> str