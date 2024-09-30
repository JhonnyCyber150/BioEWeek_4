import argparse
from Bio import SeqIO
from Bio.Seq import Seq


def main(input_file, min_length):
    for record in SeqIO.parse(input_file, "fasta"):
        sequence = record.seq
        if len(sequence) < min_length*3:
            continue

        
        print(f">ORF")
        print(sequence)
       
        
       

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find ORFs in a FASTA file")
    parser.add_argument("input_file", help="Input FASTA file")
    parser.add_argument("-l", "--min_length", type=int, default=100, 
                        help="Minimum ORF length in codons (default: 100)")
    args = parser.parse_args()

    main(args.input_file, args.min_length)
