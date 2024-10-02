import argparse
from Bio import SeqIO
from Bio.Seq import Seq

def find_ORF(sequence):
    ORFs = set ()
    n = len(sequence)
    for strand, seq in [(+1, sequence), (-1, sequence.reverse_complement())]:
        for frame in range(3):
            for start in range(frame, n, 3):
                if seq[start:start+3] == 'ATG':
                    for end in range(start + 3, n, 3):
                        if seq[end:end+3] in ['TAA', 'TAG', 'TGA']:
                            ORF = seq[start:end+3]
                            ORFs.add((start, end+3, strand, ORF))
                            break
    return ORFs

def main(input_file):
    for record in SeqIO.parse(input_file, "fasta"):
        sequence = record.seq
        ORFs = find_ORF(sequence)

        for start, end, strand, orf in ORFs:
            strand_symbol = '+' if strand == 1 else '-'
            print(f">ORF_{start}_{end}_{strand_symbol}")
            print(orf)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find ORFs in a FASTA file")
    parser.add_argument("input_file", help="Input FASTA file")
    args = parser.parse_args()

    main(args.input_file)
