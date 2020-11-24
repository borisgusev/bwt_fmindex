def suffix_array(string):
    indices = list(range(len(string)))
    indices.sort(key=lambda x: string[x:])
    return indices


def BWT_encode(string):
    assert "$" not in string  # $ used to mark end of string so cannot appear in said string
    string += "$"
    indices = [index-1 for index in suffix_array(string)]
    return "".join(map(lambda x: string[x], indices))


def BWT_decode(bwt_string):
    ranks, C_table = cumul_count(bwt_string)
    index = 0
    res = ""
    while (char := bwt_string[index]) != "$":
        res = char + res
        index = C_table[char] + ranks[index]
    return res


def cumul_count(bwt_string):
    '''
    returns a list of ranks and a C_table.
    for any valid index, ranks[index] is the number of bwt_string[index] characters in bwt_string[0:index]
    '''
    counts = {}
    ranks = []
    for char in bwt_string:
        if char not in counts:
            counts[char] = 0
        ranks.append(counts[char])
        counts[char] += 1
    return ranks, generate_C_table(counts)


def generate_C_table(counts):
    '''
    takes total counts for each chracter and returns a mapping of each character to the sum of counts of lexicographically smaller characters
    '''
    c_table = {}
    running_sum = 0
    for char, count in sorted(counts.items()):
        c_table[char] = running_sum
        running_sum += count
    return c_table


if __name__ == "__main__":

    string = "abracadabra"
    encoded = BWT_encode(string)
    decoded = BWT_decode(encoded)
    print(string)
    print(encoded)
    print(decoded)
    assert string == decoded
