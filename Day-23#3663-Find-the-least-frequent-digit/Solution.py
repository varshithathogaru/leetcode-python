class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s=str(n)
        return int(min(set(s),key=lambda d:(s.count(d),int(d))))
        
