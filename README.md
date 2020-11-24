# bwt_fmindex
Burrows–Wheeler Transform and basic FM indexing. Writing these was a learning tool to understand the underlying processes in DNA alignment in tools such as BWA or Bowtie


### bwt.py

bwt_encode function using indices and a suffix array, avoiding in-memory sorting of all rotations
bwt_decode function using LF mapping


### fmindex.py

a simple implementation of FM indexing to do substring queries. Practical use would necessitate compression of encoded string, using a more sparcely calculated Occ table, and improving the algorythm for translating the FM index back into text index. The latter currently does the naive approach of iterating until looping to end-of-string symbol, giving it O(N^2) complexity. Briefly, a better approach would be to have precalculated mappings for certain indices throughout the string and iterating until reaching such index rather than to the end.


sources:
Ferragina, Paolo & Manzini, Giovanni. (2000). Opportunistic Data Structures with Applications.
