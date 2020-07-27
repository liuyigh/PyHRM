# PyHRM
High Resolution Melt Analysis in Python

I am surprised that no free software is available to do such simple data analysis. So with some opensource spirit, I decide to write my own and share it with fellow scientists.

You can view this ipython notebook demo here:

https://github.com/liuyigh/PyHRM/blob/master/PyHRM.ipynb

The PyHRM.py file is a script you can run in Spyder or your favorite IDE instead of a Jupyter Notebook.

## FAQ

### Clustering not working.

When you get noisy data, the k-means is not going to magically salvage it. Try these:

* Do your PCR with touch down protocol, it greatly improves data quality, like magic!
* Make sure you get rid off empty wells, failed wells (look at your melting curve peaks), obvious outliers
* Make sure you choose the best temp range ± 5 degree C around melting temp usually works the best.
* For subtle differences, your eyes can be better at pattern recognition than k-means. Use the provided code to plot it with `plot.ly`. You can look at individual lines on plot.ly to make your own judgement.
* Reduce heat block variation by running only 1 target gene in symatrically arranged wells.

## How sensitive is pyHRM?

I am able to reliably detect:
* nfkb1-/- genetyping: WT vs HET vs KO; using original regular PCR primer
* an amplicon in nfkb2 gene that have single point T->G mutation: WT vs HET vs KO
* an amplicon in nfkb2 gene that have 4 base pair "TCCA" loss mutation: WT vs HET vs KO

## Reagents

I normally use Bio-Rad SsoAdvanced™ Universal SYBR® Green Supermix. Lately, I tried PowerUp SYBR Green Master Mix from Thermo / Life Technologies. I found the PowerUp mix:

* give better melting cureve differences when it works
* may not work for certain amplicons
* less efficient (higher Ct)

So it may be worth to try a couple of SYBR reagents for trouble shooting.

## qPCR protocol

Do your PCR with **touch down** protocol, it greatly improves data quality, like magic!

## Basics: HRM - High Resolution Melt Analysis

[Kapa BioSystems HRM Guide](http://www.kapabiosystems.com/document/introduction-high-resolution-melt-analysis-guide/)

## Other Software

* Precision Melt from Bio-Rad: $3,455
* GenEx: EUR€595 - 2,495
* Life Technologies: $794, 1 license
* [uAnalyze](https://dna.utah.edu/uv/uanalyze.html): Does not support Bio-Rad CFX platforms
