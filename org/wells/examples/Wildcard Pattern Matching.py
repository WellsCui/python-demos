"""
Wildcard Pattern Matching
Given a text and a wildcard pattern, implement wildcard pattern matching algorithm that finds if wildcard pattern is matched with text. The matching should cover the entire text (not partial text).

The wildcard pattern can include the characters ‘?’ and ‘*’
‘?’ – matches any single character
‘*’ – Matches any sequence of characters (including the empty sequence)

For example,

Text = "baaabab",
Pattern = “*****ba*****ab", output : true
Pattern = "baaa?ab", output : true
Pattern = "ba*a?", output : true
Pattern = "a*ab", output : false

"""


def pattern_match(text, pattern):
    postions = [0]
    pattern_size = len(pattern)

    def add_new_positions(c, pos):
        while pattern[pos] == '*':
            pos += 1
        w = pattern[pos]
        if w == '?' or w == c:
            pos += 1
            if pos not in postions:
                postions.append(pos)


    def match_char_in_position(c, pos_index):
        if postions[pos_index] == pattern_size:
            postions.pop(pos_index)
            return False
        w = pattern[postions[pos_index]]
        if w == '*':
            add_new_positions(c, postions[pos_index])
            return True
        elif w == '?' or w == c:
            postions[pos_index] = postions[pos_index] + 1
            return True
        else:
            postions.pop(pos_index)
            return False

    def match_char(c):
        for i in range(len(postions)-1, -1, -1):
            match_char_in_position(c, i)

    for c in text:
        # print("match char %s" % c)
        # print("pattern positions: %s" % postions)
        match_char(c)
        if len(postions) == 0:
            return False

    return len([p for p in postions if p == pattern_size])>0

def test_pattern_match():

    cases = [("baaabab", "*****ba*****ab"),
             ("baaabab", "baaa?ab"),
             ("baaabab", "ba*a?"),
             ("baaabab", "a*ab")
             ]

    for (t, p) in cases:
        print("text: %s, pattern: %s, matched: %s" % (t, p, pattern_match(t, p)))

test_pattern_match()

