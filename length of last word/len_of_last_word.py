class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted_words = s.strip().split(" ")
        length = len(splitted_words[-1])
        print(length)