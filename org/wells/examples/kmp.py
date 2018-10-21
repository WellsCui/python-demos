# Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all
# occurrences of pat[] and its permutations (or anagrams) in txt[]. You may assume that n > m.
# Expected time complexity is O(n)
#
# Examples:
#
# 1) Input:  txt[] = "BACDGABCDA"  pat[] = "ABCD"
# Output:   Found at Index 0
# Found at Index 5
# Found at Index 6
# 2) Input: txt[] =  "AAABABAA" pat[] = "AABA"
# Output:   Found at Index 0
# Found at Index 1
# Found at Index 4




def getAnagram(needle):
    length = len(needle);
    if length == 1:
        yield needle
    else:
        for i in range(length):
            for subAnagram in getAnagram(needle[:i] + needle[i + 1:]):
                yield needle[i] + subAnagram


def getAnagramIndices(haystack, needle):
    len1 = len(haystack)
    len2 = len(needle)
    anagrams = list(getAnagram(needle))
    for i in range(len1 - len2):
        if haystack[i:i + len2] in anagrams:
            yield i


def is_included_in(str1, str2):
    _exhausted = object()
    return next((c for c in str1 if c not in str2), _exhausted) == _exhausted


def is_inter_included(str1, str2):
    return is_included_in(str1, str2) and is_included_in(str2, str1)


def getAnagramIndices2(haystack, needle):
    len1 = len(haystack)
    len2 = len(needle)
    return (i for i in range(len1 - len2 + 1) if is_inter_included(haystack[i:i + len2], needle))


# print(list(item for item in getAnagram("ab")))
# print(list(item for item in getAnagramIndices2("abcbabee", "ab")))


def getAnagram_KMP(txt, pattern):
    partial_matches = []
    pattern_size = len(pattern)
    txt_size = len(txt)
    result = []
    if pattern_size == 0 or pattern_size > txt_size:
        return []
    if pattern_size == txt_size:
        return [0] if txt == pattern else []

    for k in range(txt_size):
        c = txt[k]
        for i in range(len(partial_matches) - 1, -1, -1):
            if pattern[partial_matches[i][1] + 1] == c:
                partial_matches[i][1] += 1
                if partial_matches[i][1] == (pattern_size - 1):
                    result.append(partial_matches[i][0])
                    partial_matches.pop(i)
            else:
                partial_matches.pop(i)
        if pattern[0] == c:
            if pattern_size == 1:
                result.append(k)
            else:
                partial_matches.append([k, 0])

    return result

def test_Anagram_KMP():
    print(getAnagram_KMP("abcbabee", "ababcbabee"))
    print(getAnagram_KMP("abcbabee", "abcbabee"))
    print(getAnagram_KMP("abcbabee", ""))
    print(getAnagram_KMP("abcbabee", "ab"))
    print(getAnagram_KMP("abcbabee", "b"))
    print(getAnagram_KMP("aabaabaabcaabaabaabaacabee", "aabaab"))

test_Anagram_KMP()



# 1. Given a binary string (e.g. 01, 101, 011), in each iteration 0 becomes 01 and 1 becomes 10, find kth character in
# the string after nth iteration
# simple approach, time complexity, express time complexity in terms of n only
# efficient approach, explanation, time complexity


def get_pos_indexes(pos, n):
    char_index, r = divmod(pos, 2 ** n)
    j = n - 1
    in_char_indexes = []
    while j > 0:
        k, r = divmod(r, 2 ** j)
        in_char_indexes.append(k)
        j -= 1
    in_char_indexes.append(r)
    return char_index, in_char_indexes


def locate_char(binary_str, n, k):
    char_index, in_char_indexes = get_pos_indexes(k - 1, n)
    char = binary_str[char_index]

    def get_sub_char(c, index):
        if c == '0':
            return '0' if index == 0 else '1'
        else:
            return '1' if index == 0 else '0'

    for in_char_index in in_char_indexes:
        char = get_sub_char(char, in_char_index)
    return char


# print(get_pos_indexes(3, 3))
# print(get_pos_indexes(10, 3))
# print(get_pos_indexes(5, 3))
# print(locate_char('101', 3, 5))
# print(locate_char('101', 3, 13))
# print(locate_char('101', 3, 23))
