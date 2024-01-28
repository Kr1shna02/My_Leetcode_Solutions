class Solution(object):
    def check_first(self, word):
        first_row = "qwertyuiopQWERTYUIOP"
        count = 0
        for i in range(len(word)):
            if word[i] in first_row:
                count += 1
        return count == len(word)

    def check_second(self, word):
        second_row = "asdfghjklASDFGHJKL"
        count = 0
        for i in range(len(word)):
            if word[i] in second_row:
                count += 1
        return count == len(word)

    def check_third(self, word):
        third_row = "zxcvbnmZXCVBNM"
        count = 0
        for i in range(len(word)):
            if word[i] in third_row:
                count += 1
        return count == len(word)

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for i in range(len(words)):
            can_be = self.check_first(words[i]) or self.check_second(words[i]) or self.check_third(words[i])
            if can_be:
                result.append(words[i])
        print(result)
        return result
