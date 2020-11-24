import bwt
import copy


class FM_index():

    def __init__(self, string):
        self.bwt_string = bwt.BWT_encode(string)
        self.Occ_table, self.C_table = FM_index.generate_Occ_C(self.bwt_string)

    @staticmethod
    def generate_Occ_C(bwt_string):
        counts = {}
        Occ_table = []
        for char in bwt_string:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
            Occ_table.append(copy.copy(counts))
        return Occ_table, bwt.generate_C_table(counts)

    def Occ(self, char, index):
        if index < 0:
            return 0
        try:
            return self.Occ_table[index][char]
        except KeyError:
            return 0  # empty entries are 0

    def fm_range(self, substring):
        '''returns a range of FM-indices for matched substrings'''
        left, right = 0, len(self.bwt_string)
        i = len(substring) - 1
        while left < right and i >= 0:
            char = substring[i]
            try:
                left = self.C_table[char] + self.Occ(char, left-1)
                right = self.C_table[char] + self.Occ(char, right-1)
            except KeyError: #if character not in Occ table, there is no match
                return None
            i -= 1
        if left < right: return (left, right)
        else: return None

    def count(self, substring):
        '''count number of matches'''
        try:
            left, right = self.fm_range(substring)
            return right - left
        except:
            return 0

    def locate(self, substring):
        '''returns indices for matched substrings'''
        try:
            start, end = self.fm_range(substring)
            return sorted(map(self.text_index, range(start, end)))
        except:
            return []


    def text_index(self, bwt_index):
        text_index = 0
        while (char := self.bwt_string[bwt_index]) != "$":
            text_index += 1
            bwt_index = self.C_table[char] + self.Occ(char, bwt_index) - 1 
        return text_index

    def decode(self):
        '''similar to bwt.decode() but uses the already calculated Occ table'''
        index = 0
        res = ""
        while (char := self.bwt_string[index]) != "$":
            res = char + res
            index = self.C_table[char] + self.Occ(char, index) - 1
        return res

if __name__ == "__main__":
    string = "SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES"
    substring = "IX"
    string_fmi = FM_index(string)
    print(string)
    print(string_fmi.locate(substring))
    assert string_fmi.decode() == string

    dna = "GATATATGCATATACTT"
    subsequence = "ATAT"
    dna_fmi = FM_index(dna)
    print(dna)
    print(dna_fmi.locate(subsequence))
    assert dna_fmi.decode() == dna


