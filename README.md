# bwt_fmindex
Burrows–Wheeler Transform and basic FM indexing. Writing these was a learning tool to understand the underlying processes in DNA alignment in tools such as BWA or Bowtie


### bwt.py

bwt_encode function using indices and a suffix array, avoiding in-memory sorting of all rotations
bwt_decode function using LF mapping


### fmindex.py

a simple implementation of FM indexing to do substring queries. Practical use would necessitate compression of encoded string, using a more sparcely calculated Occ table, and improving the algorythm for translating the FM index back into text index.


sources:
Ferragina, Paolo & Manzini, Giovanni. (2000). Opportunistic Data Structures with Applications.
