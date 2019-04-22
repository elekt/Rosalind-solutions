

def count_symbols(s):
    count_dict = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }

    for c in s.upper():
        if c in count_dict:
            count_dict[c] += 1

    return count_dict['A'], count_dict['C'], count_dict['G'], count_dict['T']


def dna_to_rna(t):
    rna = ""

    for c in t.upper():
        if c == 'T':
            rna += 'U'
        else:
            rna += c

    return rna


def dna_reverse_component(s):
    sc = ""
    reverse_symbol_dict = {
        "A": 'T',
        "C": 'G',
        "G": 'C',
        "T": 'A'
    }

    for c in s.upper()[::-1]:
        if c in reverse_symbol_dict:
            sc += reverse_symbol_dict[c]

    return sc


print(count_symbols(s="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))