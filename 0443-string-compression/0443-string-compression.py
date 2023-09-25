class Solution:
    def compress(self, chars: List[str]) -> int:
        g = groupby(chars)
        ans = ''
        for k, v in g:
            cnt = str(len(list(v)))
            ans += k + (cnt if cnt != '1' else '' )
            
        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)