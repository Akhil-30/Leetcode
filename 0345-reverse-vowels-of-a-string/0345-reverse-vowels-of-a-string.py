class Solution(object):
    def reverseVowels(self, s):
        v1,v2=0,len(s)-1
        vowels=set("aeiouAEIOU")
        result=list(s)
#         while v1<v2:
#             if (result[v1] in vowels) and (result[v2] in vowels):
#                 result[v1],result[v2]=result[v2],result[v1]
#                 v1+=1
#                 v2-=1
#             elif result[v1] not in vowels:
#                 v1+=1
#             elif result[v2] not in vowels:
#                 v2-=1
#         return ''.join(result) 
        while v1<v2:
            while v1<v2 and result[v1] not in vowels:
                v1+=1
            while v1<v2 and result[v2] not in vowels:
                v2-=1
            result[v1],result[v2]=result[v2],result[v1]
            v1+=1
            v2-=1
        return ''.join(result)   