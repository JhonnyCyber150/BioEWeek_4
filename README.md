# Week 4 Assigment 

Follow this instructions for this instructions

## Step 1
### Install Biopython in the terminal

`pip install biopython`

Successfully installed biopython-1.84 numpy-2.0.2


## Step 2
### Initialize git repository 

```bash
mkdir BioEWeek_4
cd BioEWeek_4
git init
touch gene_finder.py README.md
```

# Question 1

### Extracting Open Readin Frames (ORFs) from FASTA file 

```bash
nano gene_finder.py
git add gene_finder.py README.md
git commit -m "added gene_finder.py"
```
```bash
python gene_finder.py genome.fasta
```

# Question 2
### Extracting ORFS from a fasta file including reverse 

```bash
nano gene_finder_reverse.py
git add gene_finder_reverse.py README.md
git commit -m "added gene_finder_reverse.py"
```
```bash
python gene_finder genome.fasta
```

# Question 3

### Open Reading Frame problem on Rosalind (Problem 72)

# Question 4
### FInd all Open Reading Frames in the 14 bacterial genomes that you dowload from NCBI

```bash
find /home/caichoj/ncbi_dataset -type f -name "*GCF*.fna" | while read genome; do python gene_finder_reverse.py "$genome"; done > all_open_reading_frames.txt
```

``` bash
ls

all_open_reading_frames.txt
```
New file called "all_open_reading_frames.txt" all_open_reading_frames.txt


# Question 5
### Find all Open Reading Frame in the 14 genomes and discard short ORFS that are unlikely to be functional genes 

(e.g., less than 100 codons, but make the length a parameter of your tool).

```bash
nano gene_finder_filtered.py
```

```bash
python gene_finder_filtered.py all_open_reading_frames.txt -l 100 > output_filtered.fasta
less -l
-rw-r--r-- 1 caichoj g-caichoj 759648949 Sep 29 01:26 output_filtered.fasta
```
```bash
git add gene_finder_filtered.py
git commit -m "added gene_finder_filtered.py"
```

New output file has been created with filtered data

# Question 6
Look for is a ribosome binding site which is usually located 4-20bp upstream of the start coding. Scan upstream of the predicted start codon

```bash
nano gene_finder_RBS.py
```

```bash
python gene_finder_RBS.py output_filtered.fasta -u 20 -r AGGAGG > output_RBS.text

less -l
-rw-r--r-- 1 caichoj g-caichoj     36439 Sep 29 01:49 output_RBS.text

```
output_RBS.text file has been created

```bash
git add gene_finder_RBS.py
git commit -m "added gene_finder_RBS.py"
```


