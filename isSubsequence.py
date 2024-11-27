class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        y = []

        if s in t:
            return True
        else:
            for i in range(len(s)):
                if s[i] in t:
                    index = t.index(s[i])
                    y.append(t[index])
                    t = t[index:]
                    t = t.replace(t[0], "0", 1)
                else:
                    return False

            if s == "".join(y):
                return True
            else:
                return False
