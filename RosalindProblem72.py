import argparse
from Bio import SeqIO
from Bio.Seq import Seq

def find_ORFs(sequence):
    ORFs = []
    n = len(sequence)

    for strand, seq in [(+1, sequence), (-1, sequence.reverse_complement())]:
        for frame in range(3):
            for start in range(frame, n, 3):
                if seq[start:start+3] == 'ATG':  # Codón de inicio
                    for end in range(start + 3, n, 3):
                        if seq[end:end+3] in ['TAA', 'TAG', 'TGA']:  # Codones de parada
                            ORF = seq[start:end+3]
                            ORFs.append(ORF)  # Solo almacenar el ORF
                            break
    return ORFs

def main(input_file):
    proteins = []
    unique_proteins = set()

    for record in SeqIO.parse(input_file, "fasta"):
        sequence = record.seq
        ORFs = find_ORFs(sequence)

        for idx, orf in enumerate(ORFs):
            protein = orf.translate()  # Traducción del ORF a proteína
            if protein:  # Solo agregar proteínas no vacías
                protein_str = str(protein).rstrip('*')  # Eliminar el asterisco final
                proteins.append(f">Protein_{idx + 1}\n{protein_str}")
                unique_proteins.add(protein_str)  # Usar la versión sin asterisco

    # Guardar el primer archivo con los encabezados
    with open('Output_Proteins_with_headers.txt', 'w') as f:
        f.write('\n'.join(proteins))

    # Guardar el segundo archivo con proteínas únicas
    with open('Output_Proteins.txt', 'w') as f:
        for protein in unique_proteins:
            f.write(f"{protein}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find Open Reading Frames (ORFs) in a given FASTA file.")
    parser.add_argument("input_file", help="Path to the input FASTA file.")
    args = parser.parse_args()
    main(args.input_file)

