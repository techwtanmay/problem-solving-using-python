"""
Problem - https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        s_length = len(s)
        if s_length < 2:
            return s_length
        i = 0
        j = i + 1
        character_hash = {s[i]: i}

        while(i < j and j < s_length):
            if not s[j] in character_hash or character_hash.get(s[j]) < i:
                character_hash[s[j]] = j
            else:
                if (j - i) > max_length:
                    max_length = j - i

                i = character_hash.get(s[j]) + 1
                character_hash[s[j]] = j

            j = j + 1

        if (j - i) > max_length:
            max_length = j - i

        return max_length
    

print(Solution().lengthOfLongestSubstring("au"))