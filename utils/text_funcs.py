def split_string(text):
    """
    Splits the input string into a list of lists, where each inner list
    represents a split of the string into equal-length substrings

    example:
    split_string('123456')
        [['1', '2', '3', '4', '5', '6'],
         ['12', '34', '56'],
         ['123', '456'],
         ['123456']]
    """
    text_len = len(text)
    all_splits = []

    # find divisors of strings' length
    divisors = []
    for i in range(1, text_len + 1):
        if text_len % i == 0:
            divisors.append(i)

    # split string
    for part_len in divisors:
        split_row = [text[i:i + part_len] for i in range(0, text_len, part_len)]
        all_splits.append(split_row)

    return all_splits


def split_string_dict(text):
    """
    split_string but instead returns dict, where the key is the length of the substring
    and the value is the list of those substrings

    example:
    split_string_dict('123456')
        {1: ['1', '2', '3', '4', '5', '6'],
         2: ['12', '34', '56'],
         3: ['123', '456'],
         6: ['123456']}
    :param text:
    :return:
    """
    return {len(split[0]): split for split in split_string(text)}
