class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)
        curr_gcd = freq[deck[0]]

        for count in freq.values():
            curr_gcd = gcd(curr_gcd, count)

        return curr_gcd > 1
