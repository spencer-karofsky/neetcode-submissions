class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # 2 pointer
        for i, word, in enumerate(words):
            for j, ch in enumerate(word):
                if j >= len(words) or i >= len(words[j]) or words[j][i] != ch:
                    return False
        return True
