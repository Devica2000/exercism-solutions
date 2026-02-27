def to_rna(dna_strand):
    mapping = {'G': 'C',
               'C': 'G',
               'T': 'A',
               'A': 'U'
              }
    if dna_strand == "":
        return ""

    rna_strand = ""
    for nucleotide in dna_strand:
        if nucleotide in mapping:
            rna_strand += mapping[nucleotide]

    return rna_strand
        
