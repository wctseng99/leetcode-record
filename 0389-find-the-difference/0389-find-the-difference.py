class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dic = Counter(s)
        t_dic = Counter(t)
        
        for i in t_dic:
            if s_dic[i] != t_dic[i]:
                return i
        

            



