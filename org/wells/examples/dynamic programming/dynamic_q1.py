
# # A-Z map to 1-26, given a numeric string like '15234617823914', find all the alphabetical presentation for the string.
#
#
# def num2alphabet(num):
#     return str(chr(num + 64))
#
#
# def find_alphabetical_presentations(num_str):
#     size = len(num_str)
#     last_2 = ['']
#     last_1 = ['']
#     result = []
#
#     def append_header_to_strings(strings, header):
#         return [num2alphabet(header) + s for s in strings]
#
#     for i in range(size - 1, -1, -1):
#         if i == size - 1:
#             result = [num2alphabet(int(num_str[i]))]
#         else:
#             result = append_header_to_strings(result, int(num_str[i]))
#             if num_str[i] == '1' or (num_str[i] == '2' and num_str[i + 1] <= '6'):
#                 result = result + append_header_to_strings(last_2, int(num_str[i:i+2]))
#         last_2 = last_1
#         last_1 = result
#
#     return result
#
#
# def run_test():
#     test_strings = ['123',
#                     '3245216',
#                     '2457132619']
#
#     for item in test_strings:
#         alphabet_strings = find_alphabetical_presentations(item)
#         print("alphabet_strings:", len(alphabet_strings))
#         print(alphabet_strings)
#
#
# run_test()
#
# #
# # Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in
# # the sequence should be adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should
# # return 15 (sum of 3, 5 and 7).Answer the question in most efficient way.
# #
# # Examples :
# #
# # Input : arr[] = {5, 5, 10, 100, 10, 5}
# # Output : 110
# #
# # Input : arr[] = {1, 2, 3}
# # Output : 4
# #
# # Input : arr[] = {1, 20, 3}
# # Output : 20
#
#
# def get_max_sum(ls):
#     size = len(ls)
#     if size == 0:
#         return 0
#     if size == 1:
#         return ls[0]
#
#     return max(ls[0]+get_max_sum(ls[2:]), get_max_sum(ls[1:]))
#
#
# def get_max_sum_test():
#     print(get_max_sum([5, 5, 10, 100, 10, 5]))
#     print(get_max_sum([1, 20, 3]))
#
#
# get_max_sum_test()

def run(ls):
    size = len(ls)
    result = []
    def check_word(i, j):
        for c in ls[i]:
            if c not in ls[j]:
                return False
        return True

    def check(k):
        for i in range(size):
            if i == k:
                continue
            if check_word(k, i):
                return True
        return False

    for i in range(size):
        if check(i):
            result.append(ls[i])
    return result

print(run(['arts', 'book', 'ring', 'rats', 'star']))