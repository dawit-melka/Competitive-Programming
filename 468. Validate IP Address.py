class Solution:
    def valid_IPv4_Part(self, part):
        if not (1 <= len(part) <= 3) or not part.isnumeric():
            return False
        if len(part) > 1 and part[0] == "0":
            return False
        return 0 <= int(part) <= 255
        
    def valid_IPv6_Part(self, part):
        if not (1 <= len(part) <= 4):
            return False
        valid_chars = set(["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        for char in part:
            if char not in valid_chars:
                return False
        
        return True
            
    def validIPAddress(self, queryIP: str) -> str:
        if not (7 <= len(queryIP) <= 39):
            return "Neither"
        
        dot_count = queryIP.count(".")
        colon_count = queryIP.count(":")
        
        if dot_count == 3 and colon_count == 0:
            parts = queryIP.split(".")
            if len(parts) != 4:
                return "Neither"
            
            for part in parts:
                if not self.valid_IPv4_Part(part):
                    return "Neither"
            
            return "IPv4"
        
        elif colon_count == 7 and dot_count == 0:
            parts = queryIP.split(":")
            if len(parts) != 8:
                return "Neither"
            
            for part in parts:
                if not self.valid_IPv6_Part(part):
                    return "Neither"
            
            return "IPv6"
        

        return "Neither"

        
