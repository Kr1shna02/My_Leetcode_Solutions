import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphanumeric_list = list(string.ascii_letters + string.digits)
        result=""
        for i in range(len(s)):
            if s[i] in alphanumeric_list:
                if s[i].isupper():
                    temp=s[i].lower()
                    result+=temp
                else:
                    result+=s[i]
        Reversed=""
        for i in range(len(result)):
            Reversed+=result[len(result)-i-1]
        return Reversed==result