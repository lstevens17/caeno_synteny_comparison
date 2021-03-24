#!/usr/bin/env python3
"""
Join two BUSCO full tables into the following format:
REF_ID, Busco_id, Sequence_x, start_x, end_x, Rank_x,
QUERY_ID, Busco_id, Sequence_y, start_y, end_y and Rank_y

Usage:
        join_two_BUSCO_tables.py [--ref FILE] [--query FILE]
                                 [--idref STR] [--idquery STR]
                                  [--out FILE] 

options:
    -r FILE, --ref FILE     Busco full table of reference sample
    -q FILE, --query FILE   Busco full table of query sample
    --idref STR             Reference identifier (e.g. CELEG)
    --idquery STR           Query identifier (e.g. CNIGO)
    -o FILE, --out FILE     filename for resulting table
"""

from docopt import docopt
import pandas as pd
import copy

__author__ = "Pablo Manuel Gonzalez de la Rosa"
__version__ = '0.0.1'


def read_busco(buscofile):
    busco = pd.read_csv(buscofile, index_col=None, comment='#',
                        names=["Busco_id", "Status", "Sequence",
                               "start", "end", "Score", "Length",
                               "OrthoDB_url", "Description"],
                        sep='\t')
    return busco


def add_sco_rank(busco_data):
    busco_data['Rank'] = busco_data.groupby(
        ['Sequence'])['start'].rank(method='dense')
    return busco_data


if __name__ == "__main__":
    args             = docopt(__doc__)
    outFile          = args['--out']
    busco_ref_file   = args['--ref']
    busco_query_file = args['--query']
    idref            = args['--idref']
    idquery          = args['--idquery']


    busco_ref = read_busco(busco_ref_file).query('Status == "Complete"')[["Busco_id",
                      "Sequence", "start", "end"]]

    busco_query = read_busco(busco_query_file).query('Status == "Complete"')[["Busco_id",
                     "Sequence", "start", "end"]]

    busco_ref = add_sco_rank(busco_ref)
    busco_query = add_sco_rank(busco_query)

    ordrd_join_busco = pd.merge(busco_ref, busco_query, how='right',
    on=["Busco_id"]).groupby(["Sequence_x"]).apply(lambda x: x.sort_values(["start_x"],
    ascending = True)).reset_index(drop=True)
    ordrd_join_busco["refString"] = idref
    ordrd_join_busco["queString"] = idquery
    outTable = ordrd_join_busco[["refString", "Busco_id", "Sequence_x", "start_x", "end_x", "Rank_x",
"queString", "Busco_id", "Sequence_y", "start_y", "end_y", "Rank_y"]]
    df_outTable = copy.deepcopy(outTable)
    df_outTable[['start_x', 'end_x', 'Rank_x', "start_y", "end_y", "Rank_y"]] = outTable[[
        'start_x', 'end_x', 'Rank_x', "start_y", "end_y", "Rank_y"]].astype(int).copy()

    df_outTable.to_csv(outFile, sep='\t', header=False, index=False)

