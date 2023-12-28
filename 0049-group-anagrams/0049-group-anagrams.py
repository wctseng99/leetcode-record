class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            sorted_str = "".join(sorted(i))
            anagrams[sorted_str].append(i)
        return anagrams.values()
                