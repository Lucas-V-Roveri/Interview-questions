class Solution(object):
    def isPalindrome(self, x):


        number = str(x)
        if (number == number[::-1]):
            return(True)