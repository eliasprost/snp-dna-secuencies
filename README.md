# Snp DNA secuencies script

#### Dependencies
```
pip install -r requirements.txt
```
The script loads the config.txt file, where the file with the sequence indexes and the two .fas files that contain them are specified.
```
sequence_1 = example_sec_1.fas
sequence_2 = example_sec_2.fas
index_file = example_index.xlsx
```
The script compares both sequences nucleotide by nucleotide and count differences between sequences:
```
na = "-" in both sequences.
indel = "-" in one of the two sequences.
id = identical nucleotides in both sequences.
snp = different nucleotides in the sequences.
```
Index file example:

![Image text](https://github.com/eliasprost/snp-dna-secuencies/blob/main/input_index_example.JPG)

### Start
Install dependencies and run the file start.py
### Results
After executing the script, the counters are printed on the screen and an .xlsx file is also generated with the following structure in its name:
```
results_day-month-year-hour-min-sec.xlsx
```
Results file example:

![Image text](https://github.com/eliasprost/snp-dna-secuencies/blob/main/results_example.JPG)
