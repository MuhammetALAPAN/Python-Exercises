"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""

"""

Author: Muhammet ALAPAN

Explanation:
    My general approach for solution is: Removing inner parentheses for each type with recursive function and checking for
if list is 'None' or not.

"""


class Solution:
    def is_valid(self, s: str) -> bool:
        if not s:  # Checking for if s is None or not
            return True
        elif len(s) == 1:
            return False
        else:
            s_list = list(s)
            for i in range(len(s_list)):
                # I faced with a for loop error such as at the last recursive function, for my_test_case2 loop iterated
                # as 0,1,2 and 4 so i put a condition as below.
                if i > len(s_list) - 2:  # also there is no checking need for last index of list
                    break
                if s_list[i] == '(' and s_list[i + 1] == ')':
                    s_list.pop(i)  # removing parentheses pair
                    s_list.pop(i)
                    if self.is_valid("".join(s_list)):  # calling recursive function with popped version of list
                        return True
                elif s_list[i] == '{' and s_list[i + 1] == '}':
                    s_list.pop(i)  # removing parentheses pair
                    s_list.pop(i)
                    if self.is_valid("".join(s_list)):  # calling recursive function with popped version of list
                        return True
                elif s_list[i] == '[' and s_list[i + 1] == ']':
                    s_list.pop(i)  # removing parentheses pair
                    s_list.pop(i)
                    if self.is_valid("".join(s_list)):  # calling recursive function with popped version of list
                        return True
            return False


# Test Cases
s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "{[]}"
s6 = "["
s7 = "(("
my_test_case1 = "(){[([])]}({})[]{{}}"
my_test_case2 = "(){[([])}({})[]{{}}"
my_test_case3 = "{[}"
obj = Solution()
print(obj.is_valid(s7))
