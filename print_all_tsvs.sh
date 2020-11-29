#!/usr/bin/env bash

## Compare all to CREMA 
# CBRIG
echo "CBRIG vs CREMA"
./print_tsv.py -o Orthogroups.txt_single_copy -1 CBRIG -2 CREMA -y caenorhabditis_briggsae.PRJNA10731.WBPS15.annotations.gff3_longest_isoforms -z GCA_010183535.1_CRPX506_genomic.gff_longest_isoforms | sort -g -k 6 >CBRIG_CREMA.txt

# CNIGO
echo "CNIGO vs CREMA"
./print_tsv.py -o Orthogroups.txt_single_copy -1 CNIGO -2 CREMA -y caenorhabditis_nigoni.PRJNA384657.WBPS15.annotations.gff3_longest_isoforms -z GCA_010183535.1_CRPX506_genomic.gff_longest_isoforms | sort -g -k 6 >CNIGO_CREMA.txt

# CTROP
echo "CTROP vs CREMA"
./print_tsv.py -o Orthogroups.txt_single_copy -1 CTROP -2 CREMA -y NIC58.braker.gff3_longest_isoforms -z GCA_010183535.1_CRPX506_genomic.gff_longest_isoforms | sort -g -k 6 >CTROP_CREMA.txt

# CWALL
echo "CWALL vs CREMA"
./print_tsv.py -o Orthogroups.txt_single_copy -1 CWALL -2 CREMA -y CWALL.caenorhabditis_wallacei_JU1898_v2.annotations.gff3_longest_isoforms -z GCA_010183535.1_CRPX506_genomic.gff_longest_isoforms | sort -g -k 6 >CWALL_CREMA.txt

# CELEG
echo "CELEG vs CREMA"
./print_tsv.py -o Orthogroups.txt_single_copy -1 CELEG -2 CREMA -y caenorhabditis_elegans.PRJNA13758.WBPS15.annotations.gff3_longest_isoforms -z GCA_010183535.1_CRPX506_genomic.gff_longest_isoforms | sort -g -k 6 >CELEG_CREMA.txt

# CINOP
echo "CINOP vs CREMA"
./print_tsv.py -o Orthogroups.txt_single_copy -1 CINOP -2 CREMA -y caenorhabditis_inopinata.PRJDB5687.WBPS15.annotations.gff3_longest_isoforms -z GCA_010183535.1_CRPX506_genomic.gff_longest_isoforms | sort -g -k 6 >CINOP_CREMA.txt

## Compare selfing/outcrossing sister species 
# CBRIG vs CNIGO
echo "CBRIG vs CNIGO"
./print_tsv.py -o Orthogroups.txt_single_copy -1 CBRIG -2 CNIGO -y caenorhabditis_briggsae.PRJNA10731.WBPS15.annotations.gff3_longest_isoforms -z caenorhabditis_nigoni.PRJNA384657.WBPS15.annotations.gff3_longest_isoforms | sort -g -k 6 >CBRIG_CNIGO.txt

# CTROP vs CWALL
echo "CTROP vs CWALL"
./print_tsv.py -o Orthogroups.txt_single_copy -1 CTROP -2 CWALL -y NIC58.braker.gff3_longest_isoforms -z CWALL.caenorhabditis_wallacei_JU1898_v2.annotations.gff3_longest_isoforms | sort -g -k 6 >CTROP_CWALL.txt

# CELEG vs CINOP 
echo "CELEG vs CINOP"
./print_tsv.py -o Orthogroups.txt_single_copy -1 CELEG -2 CINOP -y caenorhabditis_elegans.PRJNA13758.WBPS15.annotations.gff3_longest_isoforms -z caenorhabditis_inopinata.PRJDB5687.WBPS15.annotations.gff3_longest_isoforms | sort -g -k 6 >CELEG_CINOP.txt
