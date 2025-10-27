class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        
        # If str1 + str2 != str2 + str1, then no common divisor string exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the greatest common divisor of lengths
        gcd_len = math.gcd(len(str1), len(str2))
        
        # The GCD string is the prefix of str1 of length gcd_len
        return str1[:gcd_len]
