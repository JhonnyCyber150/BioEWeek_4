# Week 3 and 4 Assigment: **Using Git**

### LLM used for this task
### ChatGPT 4o mini.
The LLM was used to address specific questions after code a basic script and help to overcome some problem during the pushing to the git repository. First, I developed a basic version, and then I consulted ChatGPT to optimize or enhance its efficiency while ensuring the accuracy of the results. This iterative process helped improve the code and enhance its overall performance. 

## To create this Git Repository

Follow this instructions 

## Step 1
### Install Biopython in the terminal

`pip install biopython`

Successfully installed biopython-1.84 numpy-2.0.2


## Step 2
### Initialize git repository 

```bash
mkdir BioEWeek_4
cd BioEWeek_4
```

+ git init
+ git remote add origin (https://github.com/JhonnyCyber150/BioEWeek_4.git)
+ git branch -m master main

--- 
# Question 1

### Extracting Open Readin Frames (ORFs) from FASTA file 

```bash
touch gene_finder.py README.md
nano gene_finder.py
git add gene_finder.py README.md
git commit -m "added gene_finder.py"
```
```bash
python gene_finder.py genome.fasta > output1.txt
```
```bash
git add output1.txt
git commit -m "add output1.txt"
```
--- 
# Question 2
### Extracting ORFS from a fasta file including reverse 

```bash
nano gene_finder_reverse.py
```
```bash
python gene_finder genome.fasta > output2.txt
```

```bash
git add gene_finder_reverse.py output2.txt 
git commit -m "added gene_finder_reverse.py"
```
---- 
# Question 3

### Open Reading Frame problem on Rosalind (Problem 72)

```bash
touch RosalindProblem72.py
nano RosalindProblem72.py
````
Create the code and run

```bash
python RosalindProblem72.py Rosalind_Problem72.fasta
```
OUTPUT:
Output_Proteins.txt

```bash
git add RosalindProblem72.py
git commit -m "add RosalindProblem72.py"
```

```bash
git add Rosalind_Problem72.fasta Output_Proteins.txt  Proteins_with_headers.txt
git commit -m "add Result Rosalind Problem 72"
```

    Note: downloand the fasta file from Rosalind Problem 72 and upload the result 

--- 
# Question 4
### FInd all Open Reading Frames in the 14 bacterial genomes that you dowload from NCBI

```bash
find /home/caichoj/ncbi_dataset -type f -name "*GCF*.fna" | while read genome; do python gene_finder_reverse.py "$genome"; done > all_open_reading_frames.txt
```

``` bash
ls

all_open_reading_frames.txt
```
New file called "all_open_reading_frames.txt"

A frame of the content in "all_open_reading_frames.txt"
```bash
>ORF_432_474_+
ATGCGGCTCGATGAGGGCGTCAATTTCATTGATTTTTTCTAA
>ORF_1044_1056_+
ATGTTAAAATAG
>ORF_1893_1920_+
ATGGCCCAGCGATTAAAACGGATTTAG
>ORF_1962_2007_+
ATGGTTTCTCCAATCGGCTCAAAAAAATGGCTTTCAAAATTATAA
...
```
--- 
# Question 5
### Filter by length: discard short ORFs that are unlikely to be functional genes
(e.g., less than 100 codons, but make the length a parameter of your tool).

```bash
nano gene_finder_filtered.py
```

```bash
python gene_finder_filtered.py all_open_reading_frames.txt -l 100 > output_filtered.fasta
less -l

-rw-r--r-- 1 caichoj g-caichoj 141619281 Sep 30 20:32 output_filtered.fasta
```


New output file has been created with filtered data

A frame of the content in: output_filtered.fasta
```bash
>ORF
ATGCAATTATGTGTCGCATTGGATTTAGAAAAAAAAGAGGACAATCTTTCTTTATTGCAAGAATTGAAGGGCTTAGATTTATGGGCTAAGGTGGGGCTTAGATCTTTTATAAGAGACGGGGCTGTTTTTTTAGATGAAATCAGAAAGATTGATGAAAATTTTAAG
>ORF
ATGGCAAATGCCGCACTAGAATGCGCGAAATTAGACATTGACATGCTCACCGTGCATTTAAGCAGCGCTAAAAGCGCGCTAACAGCTTTAATGCAACGCCTGAACGCTCTTAAAAAACGCCCCTTGATTATGGGCGTGAGCGCTTTAACCAGCTTTAGCGAAGAG>
>ORF
ATGCTCACCGTGCATTTAAGCAGCGCTAAAAGCGCGCTAACAGCTTTAATGCAACGCCTGAACGCTCTTAAAAAACGCCCCTTGATTATGGGCGTGAGCGCTTTAACCAGCTTTAGCGAAGAGGAATTTTTGATGGTGTATAACGCCCCTTTAAAAACTCAAGCG>
....
```

```bash
git add gene_finder_filtered.py
git commit -m "added gene_finder_filtered.py"
```
--- 
# Question 6
### Look for is a ribosome binding site which is usually located 4-20bp upstream of the start coding. Scan upstream of the predicted start codon

```bash
nano gene_finder_RBS.py
```

```bash
python gene_finder_RBS.py output_filtered.fasta -u 20 -r AGGAGG > output_RBS.text
ls -l
```
A new file has been created that contains the output with RBS

```bash
-rw-r--r-- 1 caichoj g-caichoj    289059 Sep 30 20:57 output_RBS.text
```

A frame of the content in: output_RBS.text

```bash
>ORF
>ORF
ATGAAAACAGGAGGGAATGACCCCTACCAATTAATGGTGAATACCAAAAACACCGGCGAAGACAACCGAGTCTATTTTGGCTCACACCTCCAATCCACGCTCACTAACAAAAACGCCCTTTCTTTGGGGGTTGATGGGAGCGGAAAAAGTGAAGTGAGTTTGAAT>
>ORF
ATGCCAACTGATAAGGAGGGCGATTTTATTGATCCTAAAGAACAAGAAGAAAGCCTTGAAAATATTTTTTCTTCACTCAATGATTTTCAAGAAAAGACAGACGCAAACGCTCAAAAAAATGAGCAAAAAAATGAGCAAGAAGAAGAGCAAAGGCGTTTAAAAGAA>
>ORF
ATGAAAGGAGGCGTGGGGGCGTTTTTGAGCGCGAGTTTAAATTTTAACCCTAAAACCCCTTTTTTGCTTTCTATTTTACTCACAAGCGATGAAGAAGGGCCAGGGATTTTTGGCACTAGGCTTATGTTAGAAAAACTCAAAGAAAAAGATTTGCTGCCTCATATG>
....
```

```bash
git add gene_finder_RBS.py output_RBS.txt 
git commit -m "added gene_finder_RBS.py"
```
--- 
 # Save on gitHub Repository
* git push -u origin main

