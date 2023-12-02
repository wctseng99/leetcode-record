class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        freq_count = Counter(chars)
        length = 0
        
        for word in words:
            char_freq = defaultdict(int)
            for char in word:
                char_freq[char] += 1
            
            good = True
            for c, freq in char_freq.items():
                if freq_count[c] < freq:
                    good = False
            
            if good:
                length += len(word)
        
        return length
                    