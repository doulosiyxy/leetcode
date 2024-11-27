class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]

        dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        integer = []
        for i in range(len(s)):
            if i < len(s) - 1:
                if s[i] in ["V", "X"] and s[i + 1] == "I":
                    integer.append(dict[s[i]] -2)
                elif s[i] in ["L", "C"] and s[i + 1] == "X":
                    integer.append(dict[s[i]]-20)
                elif s[i] in ["D", "M"] and s[i + 1] == "C":
                    integer.append(dict[s[i]]-200)
                else:
                    integer.append(dict[s[i]])
            else:
                integer.append(dict[s[i]])

        return sum(integer)
