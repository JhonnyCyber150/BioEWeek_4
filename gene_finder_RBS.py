import argparse
from Bio import SeqIO

def main(input_file, min_length, upstream_range, rbs_sequence):
    records = list(SeqIO.parse(input_file, "fasta"))
    for record in records:
        sequence = record.seq
        sequence_short = sequence[:upstream_range]

        if rbs_sequence in sequence_short:
            print(">ORF")
            print(sequence)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find ORFs in a FASTA file with length and RBS filtering")
    parser.add_argument("input_file", help="Input FASTA file")
    parser.add_argument("-l", "--min_length", type=int, default=100,
                        help="Minimum ORF length in codons (default: 100)")
    parser.add_argument("-u", "--upstream_range", type=int, default=20,
                        help="Number of base pairs upstream to search for RBS (default: 20)")
    parser.add_argument("-r", "--rbs_sequence", type=str, default="AGGAGG",
                        help="Ribosome Binding Site sequence to search for (default: AGGAGG)")
    args = parser.parse_args()

    main(args.input_file, args.min_length, args.upstream_range, args.rbs_sequence)
