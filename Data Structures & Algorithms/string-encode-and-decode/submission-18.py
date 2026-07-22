class Solution:
    def encode(self, strs: List[str]) -> str:
        s = []
        for string in range(len(strs)): #O(m) where m is len(strs)
            if len(strs) > 0:
                s = ".".join(strs)
        return str(s)

    def decode(self, s: str) -> List[str]:
        spacenum = 0
        element = 0
        if s == str([]):
            return []
        else:
            for l in s: #O(m)
                if l == ".":
                    spacenum += 1
            decoded_s = ["" for i in range(spacenum+1)]

            for l in s: 
                if l == ".":
                    element += 1
                    continue
                decoded_s[element] += l
            
            return decoded_s