class Solution(object):
    def mergeAlternately(self, word1, word2):
        i=0
        merged=[]
        while i<len(word1) and i<len(word2):
            merged.extend([word1[i],word2[i]])
            i+=1
        merged.extend(word1[i:])
        merged.extend(word2[i:])
        return "".join(merged)

        