def index_prod(mylist):
    output = [None] * len(mylist)

    product = 1
    i = 0

    while i < len(mylist):
        output[i] = product
        product *= mylist[i]

        i += 1

    product = 1
    i = len(mylist) - 1

    while i >= 0:
        output[i] *= product
        product *= mylist[i]
        i -= 1

    return output
