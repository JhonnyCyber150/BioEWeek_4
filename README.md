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
python gene_finder.py ecoli.fna > output_problem1.txt

```
```bash
git add output1.txt ecoli.fna
git commit -m "output_problem1.txt"
```
--- 
# Question 2
### Extracting ORFS from a fasta file including reverse 

```bash
nano gene_finder_reverse.py
```
```bash
python gene_finder_reverse.py ecoli.fna > output_problem2.txt
```

```bash
git add gene_finder_reverse.py output_problem2.txt 
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

find /home/caichoj/ncbi_dataset -type f -name "*GCF*.fna" -exec python gene_finder_reverse_trans3.py {} all_ORFs.txt \;
```

``` bash
ls -l

all_ORFs.txt
```
New file called "all_ORFs.txt"

```
[caichoj@login509-02-l BioEWeek_4]$ ls -lh all_ORFs.txt
-rw-r--r-- 1 caichoj g-caichoj 60M Oct  2 20:59 all_ORFs.txt

[caichoj@login509-02-r BioEWeek_4]$ wc -l all_ORFs.txt
765037 all_ORFs.txt
```


--- 
# Question 5
### Filter by length: discard short ORFs that are unlikely to be functional genes
(e.g., less than 100 codons, but make the length a parameter of your tool).

```bash
nano gene_finder_filtered.py
```

```bash
find /home/caichoj/ncbi_dataset -type f -name "*GCF*.fna" -exec python gene_finder_filtered.py {} output_filtered.txt -l 100 \;

less -l

output_filtered.txt
```


New output file has been created with filtered data: 45MB

```
[caichoj@login509-02-r BioEWeek_4]$ ls -lh output_filtered.txt
-rw-r--r-- 1 caichoj g-caichoj 45M Oct  2 17:35 output_filtered.txt


[caichoj@login509-02-r BioEWeek_4]$ wc -l output_filtered.txt
162136 output_filtered.txt
```` 

```bash
git add gene_finder_filtered.py output_filtered.txt
git commit -m "added gene_finder_filtered.py"
```
--- 
# Question 6
### Look for is a ribosome binding site which is usually located 4-20bp upstream of the start coding. Scan upstream of the predicted start codon

```bash
nano gene_finder_RBS.py
```

```bash
 find /home/caichoj/ncbi_dataset -type f -name "*GCF*.fna" -exec python gene_finder_RBS2.py {} output_RBS.txt -l 100 \;
```
A new file has been created that contains the output with RBS

```bash
output_RBS.text
```
```
[caichoj@login509-02-l BioEWeek_4]$ ls -lh output_RBS.txt
-rw-r--r-- 1 caichoj g-caichoj 7.9K Oct  2 20:35 output_RBS.txt

[caichoj@login509-02-l BioEWeek_4]$ wc -l output_RBS.txt
26 output_RBS.txt
``` 

```bash
git add gene_finder_RBS.py output_RBS.txt 
git commit -m "added gene_finder_RBS.py"
```
--- 
 # Save on gitHub Repository
* git push -u origin main

