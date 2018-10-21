# Find the indices of all anagrams of a given word in a another word.
# For example: Find the indices of all the anagrams of AB in ABCDBACDAB (Answer: 0, 4, 8)


def same_anagrams(str1, str2):
    for c in str1:
        if c not in str2:
            return False
    return True


def find_anagrams(inputs, anagrams):
    a_size = len(anagrams)
    input_size = len(inputs)

    def get_anagrams(index):
        return inputs[index:index+a_size]

    result = []
    if input_size >= a_size:
        for i in range(input_size-a_size+1):
            if same_anagrams(anagrams, get_anagrams(i)):
                result.append(i)

    return result


def find_anagrams_test():
    test_data = [('ABCDBACDAB', 'AB', [0, 4, 8])
                 ]
    for inputs, anagrams, expected in test_data:
        print('expected: %s result: %s' % (expected, find_anagrams(inputs, anagrams)))


find_anagrams_test()