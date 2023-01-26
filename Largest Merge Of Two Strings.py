class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        index1, index2 = 0, 0
        merge = []
        while index1 < len(word1) or index2 < len(word2):
            if index1 < len(word1) and index2 < len(word2):
                if word1[index1:] >= word2[index2:]:
                    merge.append(word1[index1])
                    index1 += 1
                else:
                    merge.append(word2[index2])
                    index2 += 1
            else:
                merge.append(word1[index1:])
                merge.append(word2[index2:])
                break
                
        return "".join(merge)
