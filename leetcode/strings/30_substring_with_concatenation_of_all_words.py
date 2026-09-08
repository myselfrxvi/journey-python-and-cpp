from typing import List
from collections import Counter, defaultdict

class Solution:
    def findSubstring(self,s:str,words:List[str])->List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words

        if len(s) < total_len:
            return []

        word_counts = Counter(words)
        res = []

        for offset in range(word_len):
            left = offset
            right = offset
            curr_counts = defaultdict(int)

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_counts:
                    curr_counts[word] += 1

                    while curr_counts[word] > word_counts[word]:
                        left_word = s[left:left + word_len]
                        curr_counts[left_word] -= 1
                        left += word_len

                    if right - left == total_len:
                        res.append(left)
                else:
                    curr_counts.clear()
                    left = right

        return res

        
        