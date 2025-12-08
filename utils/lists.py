def merge_ranges(ranges: list[list[int] or tuple[int]]):
    """
    Reduce number of ranges by merging them together if they overlap

    :param ranges: list of possibly overlapping ranges
    :return:
    """

    # non-overlapping ranges
    new_ranges = []
    for r in ranges:
        # store indexes of overlapping ranges
        overlaps = []

        # find overlapping ranges
        for nr in new_ranges:
            if (  # lower band already included in new ranges
                    nr[0] <= r[0] <= nr[1] <= r[1] or
                    # both bands already in one new range
                    (nr[0] <= r[0] <= nr[1] and nr[0] <= r[1] <= nr[1]) or
                    # upper band already included in new ranges
                    nr[1] >= r[1] >= nr[0] >= r[0] or
                    # both bands overlap new range
                    r[0] <= nr[0] <= nr[1] <= r[1]
            ):
                overlaps.append(new_ranges.index(nr))

        # determine new lower and upper bands
        lower = min([new_ranges[o][0] for o in overlaps] + [r[0]])
        upper = max([new_ranges[o][1] for o in overlaps] + [r[1]])

        # remove overlapping ranges
        overlaps.sort(reverse=True)
        for m in overlaps:
            new_ranges.pop(m)

        # add new range
        new_ranges.append([lower, upper])

    return new_ranges


def transpose(array: list[list]):
    """
    Transposes a 2D list

    Example:
    [[1,2,3],
     [4,5,6],
     [7,8,9]]

    Returns:
    [[1,4,7],
     [2,5,8],
     [3,6,9]]

    :param array: 2D list
    :return:
    """
    return [list(row) for row in list(zip(*array))]
