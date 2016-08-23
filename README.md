# Primal Scheme (Web Interface)

Web frontend for primal - a work in progress...

# primal
A primer3 wrapper for designing multiplex primer schemes

Primal is a python package for generating multiplex tiling amplicon schemes for viral sequencing. As opposed to focusing on algorithms to generate the candidate primers i.e. K-mer matching or de Bruijn graphs, Primal uses Primer3 to generate candidate primers from a single reference genome. It then scores the primers based on pairwise alignment to any number of additional reference genome before selecting the best candidates.  It was the method we used to generate the Zika virus scheme used for the ZiBRA project after having limited success using existing methods.

Parameters for primer length and Tm are hardcoded in Primal as we believe they are necessary for successful multiplex PCR. We have sequenced viral genomes of up to 11 kb in length with products generated by two PCR reactions using this method. You can adjust the desired product length to suit your sample type or sequencing platform. For example, using an amplicon length of 400 suits both the MiSeq 2x250 run configuration or MinION. You can also adjust the overlap parameter to set the length of sequence shared by overlapping amplicons.

Input should be a fasta file containing reference genomes representative of the lineages you would expect to find in your samples. The first genome in the fasta file is used to generate the candidates so it is the most important. If you specify a fasta file containing highly divergent genomes Primal is less likely to find universal primers.

Useful links:

http://primer3.sourceforge.net/
http://biomedcentral.com/1471-2105/11/143
http://dx.doi.org/10.1371/journal.pone.0034560
