class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict = {}

        for item in strs:
            wrd = "".join(sorted(item))
            if wrd not in anag_dict:
                anag_dict[wrd] = [item]
            else:
                anag_dict[wrd].append(item)

        return list(anag_dict.values())