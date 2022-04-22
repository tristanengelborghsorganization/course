"""
Write a function 'longest_common_subsequence' that, given two strings, finds the list of longest common
subsequences (the longest group of characters that occur in both strings, in the same order).
For example, the list of longest common subsequences of 'methodiek' and 'katholiek' is [ 'thoiek' ], since
the letters t, h, o, i, e, k occur in both strings and in the same order.

Note that two strings can have multiple common subsequences. For instance, the longest common subsequences of
'methodiek' and 'ochtendgymnastiek' are the elements in the list [ 'ediek', 'etiek', 'hdiek', 'mtiek', 'odiek', 'tdiek' ]
The order of the elements in the list is of no importance.

If the strings do not have matching characters, the longest common subsequence is an empty string.

Write this function as a RECURSIVE function. This is not enforced by the tests, but you should
implement it like this anyway. On the actual exam, someone will actually look at your implementation
to manually verify that it is indeed written recursively.

Note:
    The file that you submit as your solution should NOT contain ANY syntax errors!
    Solutions with syntax errors yield a score of 0 for this question, even if
    syntax errors occur in function you no longer use (e.g. a helper function that you wanted to define).

Note 2:
    If you upload your solution before the deadline, your implementation will be graded by us. This grade
    is a direct (and automatically calculated) result of the output of a number of test cases (different test
    cases than the ones in this file). Make sure you think about special and edge cases.

TIP:
    You -may- use sets, but do not have to!
    If you don't, you may (but do not have to) use the function "contain_the_same_elements" as defined below.

"""


def longest_common_subsequence(xstr, ystr):  # do not change the signature of this function (i.e. do not change its name, add/remove parameters, ...)
    """
    Given two strings, this function returns the set of longest common subsequences of both strings
    """
    if xstr != ystr:
        common_sequence = ""
        for i in range(len(xstr)):
            if xstr[i] in ystr:
                position = ystr.find(xstr[i])
                common_sequence += ystr[position] + ' '.join([str(item) for item in longest_common_subsequence(xstr[i + 1:], ystr[position + 1:])])
            else:
                common_sequence += ' '.join([str(item) for item in longest_common_subsequence(xstr[i + 1:], ystr)])
            common_sequence += " "
            print(common_sequence)

        longest_sequence = 0
        longest_common_sequence_list = []
        longest_common_sequence_list_no_duplicates = []
        for element in common_sequence.split():
            if len(element) > longest_sequence:
                longest_sequence = len(element)
        for element in common_sequence.split():
            if len(element) == longest_sequence:
                longest_common_sequence_list += [element]
        for element in longest_common_sequence_list:
            if element not in longest_common_sequence_list_no_duplicates:
                longest_common_sequence_list_no_duplicates.append(element)
        if longest_common_sequence_list_no_duplicates != []:
            return longest_common_sequence_list_no_duplicates
        else:
            return [""]
    else:
        return [xstr]




# This function checks if two lists contain the same elements, that is, if all elements
# in list1 are also an element in list2, and vice versa.
#   e.g. contain_the_same_elements(["a"],["a"]) --> True
#   e.g. contain_the_same_elements(["a"],["a", "b"]) --> False
#   e.g. contain_the_same_elements(["a", "b"],["b", "a"]) --> True
#   e.g. contain_the_same_elements(["a", "b", "a"],["b", "a", "b"]) --> True (both contain only the elements "a" and "b")
def contain_the_same_elements (list1, list2):
    return set(list1) == set(list2)


#########################################################################################################

# In this main function, several cases are tested.
# You are of course free to change this function to define your own tests!
def mains():
    woord1 = input("woord1: ")
    woord2 = input("woord2: ")
    print(longest_common_subsequence(woord1, woord2))
def main():

    string1 = ""
    string2 = ""
    expected_result = [""]
    print(f"Testing with input '{string1}' and '{string2}'.")
    result = longest_common_subsequence(string1, string2)
    print(f"Received result: {result}")
    assert contain_the_same_elements(result, expected_result) and len(result) == len(expected_result)
    print("Test succeeded!")

    print("================================================")

    string1 = "a"
    string2 = "a"
    expected_result = ["a"]
    print(f"Testing with input '{string1}' and '{string2}'.")
    result = longest_common_subsequence(string1, string2)
    print(f"Received result: {result}")
    assert contain_the_same_elements(result, expected_result) and len(result) == len(expected_result)
    print("Test succeeded!")

    print("================================================")

    string1 = "ab"
    string2 = "ba"
    expected_result = ["a", "b"]
    print(f"Testing with input '{string1}' and '{string2}'.")
    result = longest_common_subsequence(string1, string2)
    print(f"Received result: {result}")
    assert contain_the_same_elements(result, expected_result) and len(result) == len(expected_result)
    print("Test succeeded!")

    print("================================================")

    string1 = "aap"
    string2 = "beer"
    expected_result = [""]
    print(f"Testing with input '{string1}' and '{string2}'.")
    result = longest_common_subsequence(string1, string2)
    print(f"Received result: {result}")
    assert contain_the_same_elements(result, expected_result) and len(result) == len(expected_result)
    print("Test succeeded!")

    print("================================================")

    string1 = "aapje"
    string2 = "banaan"
    expected_result = ["aa"]
    print(f"Testing with input '{string1}' and '{string2}'.")
    result = longest_common_subsequence(string1, string2)
    print(f"Received result: {result}")
    assert contain_the_same_elements(result, expected_result) and len(result) == len(expected_result)
    print("Test succeeded!")

    print("================================================")

    string1 = "methodiek"
    string2 = "katholiek"
    expected_result = ["thoiek"]
    print(f"Testing with input '{string1}' and '{string2}'.")
    result = longest_common_subsequence(string1, string2)
    print(f"Received result: {result}")
    assert contain_the_same_elements(result, expected_result) and len(result) == len(expected_result)
    print("Test succeeded!")

    print("================================================")


    string1 = "methodiek"
    string2 = "ochtendgymnastiek"
    expected_result = ['ediek', 'etiek', 'hdiek', 'mtiek', 'odiek', 'tdiek']
    print(f"Testing with input '{string1}' and '{string2}'.")
    result = longest_common_subsequence(string1, string2)
    print(f"Received result: {result}")
    assert contain_the_same_elements(result, expected_result) and len(result) == len(expected_result)
    print("Test succeeded!")

    print("================================================")

# DO NOT CHANGE ANYTHING BELOW THIS LINE !!!
if __name__ == "__main__":
    main()