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


def Rect_overlap(r1, r2):
    X_lap, w_lap = calc_overlap(r1['x'], r1['w'], r2['x'], r2['w'])
    y_lap, h_lap = calc_overlap(r1['y'], r1['h'], r2['y'], r2['h'])

    if not w_lap or not h_lap:
        print('No overlap!')
        return None

    return {'x': X_lap, 'y': y_lap, 'w': w_lap, 'h': h_lap}
