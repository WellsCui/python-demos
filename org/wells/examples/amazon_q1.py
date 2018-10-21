# Write a Java code that take a string of parenthesis as input and return if the string is valid or not .
#  The input will have '(' and ')' and also '*' and * serves as wild card and can be used in place of both '(' and ')'
#  or it can be null.
#
# For example,the String (*)(*)(** is a valid String.
#
#     Follow up: What if '[]' and '{}' are also in the string along with '()' and * can be used in place of any of them
#  or can be considered as null?
#
# - ryanray1512 October 16, 2017 in United States | Report Duplicate | Flag


def check_parenthesis(input, pairs):
    state = None
    for c in input:
        if state is None:
            if c in pairs:
                state = c
            else:
                return False
        elif pairs[state] == c:
            state = None
        elif c != '*':
            return False
    return True

def check_parenthesis2(input, parenthesis):
    state = []

    def get_current_parenthesis():
        if len(state) == 0:
            return None
        else:
            return state[-1]

    for c in input:
        current_parenthesis = get_current_parenthesis()

        if current_parenthesis is None:
            if c in parenthesis:
                state.append(c)
            else:
                return False
        elif c in parenthesis:
            state.append(c)
        elif parenthesis[current_parenthesis] == c:
            state.pop()
        elif c != '*':
            return False
    return True

def check_parenthesis_test():
    test_data = [('(*)(*)(**', True),
                 ('(*)(*))', False),
                 ('((', False),
                 ('(]', False),
                 ('{*}]', False),
                 ('[*](*){*}', True)]
    pairs = {'(': ')', '[': ']', '{': '}'}
    for input, expected in test_data:
        print('expected: %s result: %s' % (expected, check_parenthesis(input, pairs)))

def check_parenthesis2_test():
    test_data = [('(*)(*)(**', True),
                 ('(*)(*))', False),
                 ('((', True),
                 ('(]', False),
                 ('{*}]', False),
                 ('[*](*){*}', True),
                 ('((*))', True),
                 ('({*})', True),
                 ('((*)[]{*(*){}[]})', True),
                 ('((*)[]{*(*){}[]])', False),
                 ('((*)[]{*(*){}[]}]', False)

                 ]
    pairs = {'(': ')', '[': ']', '{': '}'}
    for input, expected in test_data:
        print('expected: %s result: %s' % (expected, check_parenthesis2(input, pairs)))


# check_parenthesis2_test()
check_parenthesis2_test()


