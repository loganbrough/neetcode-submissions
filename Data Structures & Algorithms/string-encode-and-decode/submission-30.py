class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)) + "#" + s)
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i, length = 0, ""
        while i < len(s):
            if s[i] == "#":
                word = ""
                for j in range(i + 1, i + int(length) + 1):
                    word += s[j]
                res.append(word)
                i += (int(length) + 1)
                length = ""
            else:
                length += s[i]
                print(length)
                i += 1
                
    
        return res