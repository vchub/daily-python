class Solution:
    # def checkValidString(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     cnt, star_cnt = (0, 0)
    #
    #     for ch in s:
    #         if cnt + star_cnt < 0:
    #             return False
    #         elif ch == '*':
    #             star_cnt += 1
    #         elif ch == '(':
    #             cnt += 1
    #         elif ch == ')':
    #             cnt -= 1
    #
    #     print(cnt, star_cnt)
    #
    #     if cnt + star_cnt < 0:
    #         return False
    #     elif cnt <= star_cnt:
    #         return True
    #     else:
    #         return False
    #

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo = hi = 0

        for ch in s:
            lo += 1 if ch == '(' else -1
            hi += 1 if ch != ')' else -1

            if hi < 0: return False
            lo = max(lo, 0)

        return lo == 0
