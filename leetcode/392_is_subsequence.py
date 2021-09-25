class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        word_list = list(s)
        idx = 0
        for tt in t:
            if idx >= len(word_list):
                break

            if tt == word_list[idx]:
                idx += 1

        return idx == len(word_list)


