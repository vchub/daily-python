class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        n = len(s)

        for i in range(int(n / 2)):
            if s[i] != s[n - i - 1]:
                return self.valid(s[i:n - i - 1]) \
                    or self.valid(s[i + 1:n - i])

        return True

    def valid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        n = len(s)

        for i in range(int(n / 2)):
            if s[i] != s[n - i - 1]:
                return False

        return True
