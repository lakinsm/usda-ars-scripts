#!/usr/bin/env python3

import sys
import glob
from Bio import Entrez


def multi_gb_to_fasta(in_dir):
    for file in glob.glob(in_dir + '/*'):
        with open(file, 'r') as f:
            records = Entrez.parse(f)
            for record in records:
                acc = record['GBSeq_accession-version']
                for feature in record['GBSeq_feature-table']:
                    gene = None
                    product = None
                    transl = None
                    if 'GBFeature_quals' in feature:
                        quals = feature['GBFeature_quals']
                    else:
                        continue
                    for qual in quals:

                        if qual['GBQualifier_name'] == 'gene':
                            gene = qual['GBQualifier_value']
                        elif qual['GBQualifier_name'] == 'product':
                            product = qual['GBQualifier_value']
                        elif qual['GBQualifier_name'] == 'translation':
                            transl = qual['GBQualifier_value']
                        else:
                            continue
                    if gene and product and transl:
                        sys.stdout.write('>{} ~~~{}~~~{}\n{}\n'.format(
                            acc,
                            gene,
                            product,
                            transl
                        ))
                    elif product and transl and not gene and product != 'hypothetical protein':
                        sys.stdout.write('>{} ~~~~~~{}\n{}\n'.format(
                            acc,
                            product,
                            transl
                        ))


if __name__ == "__main__":
    multi_gb_to_fasta(sys.argv[1])
