# PyHRM version 1.1 (russian adaptation)
## North-Eastern Federal University in Yakutsk, Molecular Medicine and Human Genetics lab, Department of Proteomics and Gene Editing 

High Resolution Melt Analysis in Python 

Demo is on duty.

The PyHRM.py can be run in Jupyter Notebook.

contributed by https://github.com/liuyigh/PyHRM

# Proteomics and Gene Editing
## Proteomics and Gene Editing
### Proteomics and Gene Editing
#### Proteomics and Gene Editing
##### Proteomics and Gene Editing
###### Proteomics and Gene Editing

# Issues solved in v1.1

## 1. Issues with delimiter on Russian CFX data
### - delimiter set to ";"

## 2. Data type for pandas
### - data type changed from "object" to "float"

## 3. Issues with dots 
### - comma is used as a decimal separator on Russian data sets instead of a point

## FAQ

### Clustering not working.

When you get noisy data, the k-means is not going to magically salvage it. Try these:

* Do your PCR with touch down protocol, it greatly improves data quality, like magic!
* Make sure you get rid off empty wells, failed wells (look at your melting curve peaks), obvious outliers
* Make sure you choose the best temp range ± 5 degree C around melting temp usually works the best.
* For subtle differences, your eyes can be better at pattern recognition than k-means. Use the provided code to plot it with `plot.ly`. You can look at individual lines on plot.ly to make your own judgement.
* Reduce heat block variation by running only 1 target gene in symatrically arranged wells.

## Reagents

We are used SYBR Green reagents on our samples folder.

## qPCR protocol

PCR protocal is developing. There are evidence that incresing melting temperature around 5-10 C on PCR will make better performance on data (https://pubmed.ncbi.nlm.nih.gov/29717053/)

## Other Software

* Precision Melt from Bio-Rad: $3,455
* GenEx: EUR€595 - 2,495
* Life Technologies: $794, 1 license
* [uAnalyze](https://dna.utah.edu/uv/uanalyze.html): Does not support Bio-Rad CFX platforms, but if change csv file to tabular delimiter it should work fine
* There is another HRM script on R to be investigated https://pavloh.shinyapps.io/hrmR/ also on GitHub https://github.com/pavlohrab/hrmR
