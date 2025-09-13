# http://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels_freq = {}
        freq = {}

        vowels = ["a", "e", "i", "o", "u"]

        for i in range(len(s)):
            freq_dict = vowels_freq if s[i] in vowels else freq

            if not s[i] in freq_dict:
                freq_dict[s[i]] = 1
            else:
                freq_dict[s[i]] += 1

        a = freq[max(freq, key=freq.get)] if len(freq) != 0 else 0
        b = vowels_freq[max(vowels_freq, key=vowels_freq.get)] if len(vowels_freq) != 0 else 0

        return a + b

        
