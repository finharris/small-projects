class isPalindrome:
    def isPalindrome(self, word):
        wordList = list(word)
        wordList.reverse()
        
        condensed = ''
        for c in wordList:
            condensed += c
        
        if condensed == word:
            return True
        else:
            return False