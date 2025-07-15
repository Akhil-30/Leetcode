class Solution(object):
    def reversePrefix(self, word, ch):
        # k=''
        # i=0
        # result=list(word)
        # while i<len(word):
        #     k=word[i]
        #     if k==ch:
        #         break
        #     i+=1
        # if k != ch:
        #     return ''.join(result)
        # l,r=0,i
        # while l<r:
        #     result[l],result[r]=result[r],result[l]
        #     l+=1
        #     r-=1
        # return ''.join(result)
        result=list(word)
        for i in range(len(result)):
            if result[i]==ch:
                l,r=0,i
                while l<r:    
                    result[l],result[r]=result[r],result[l]
                    l+=1
                    r-=1
                return ''.join(result)
        return word  


        