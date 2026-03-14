def proteins(strand):
    strand_dict = {
                    'AUG': 'Methionine',
                  'UUU': 'Phenylalanine',
                  'UUC': 'Phenylalanine',
                  'UUA': 'Leucine',
                  'UUG': 'Leucine',
                  'UCU': 'Serine',
                  'UCC': 'Serine',
                  'UCA': 'Serine',
                  'UCG': 'Serine',
                  'UAU': 'Tyrosine',
                  'UAC': 'Tyrosine',
                  'UGU': 'Cysteine',
                  'UGC': 'Cysteine',
                  'UGG': 'Tryptophan',
                  }
    
    amino_acid = []

    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        if (codon == "UAA" or codon == "UAG" or codon == 'UGA'):
            break
        amino_acid.append(strand_dict[codon])

    return amino_acid
            
            
            
            
        
        
