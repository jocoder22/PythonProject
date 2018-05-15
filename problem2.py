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


def calc_overlap(coord1, dim1, coord2, dim2):

    greater = max(coord1, coord2)
    lower = min(coord1 + dim1, coord2 + dim2)

    if greater >= lower:
        return (None, None)

    overlap = lower - greater

    return (greater, overlap)


