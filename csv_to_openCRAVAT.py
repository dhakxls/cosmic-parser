import csv
import re

filename = '<Insert Filename Here>'

def csv_2_tsv():
    """
    Writes a copy of the csv file into a tsv file
    """
    with open(filename,'r') as csvin, open('tsv_input.tsv', 'w', newline='') as tsvout:
        csvin = csv.reader(csvin)
        tsvout = csv.writer(tsvout, delimiter='\t')

        for row in csvin:
            tsvout.writerow(row)

def tsv_2_HGVSG():
    """
    Writes a copy of the 'tsv_input.tsv' file into another tsv file, 'tsv_output.tsv',
    containing just everything in the ' HGVSG' column.
    """
    with open('tsv_input.tsv','r',newline='') as fin,open('tsv_output.tsv','w',newline='') as fout:
        reader = csv.DictReader(fin,delimiter='\t')
        writer = csv.DictWriter(fout,delimiter='\t',fieldnames=[' HGVSG'],extrasaction='ignore')
        writer.writeheader()
        for row in reader:
            writer.writerow(row)

def HGVSG_2_CRAVAT():
    """
    Writes the new CRAVAT input file from the 'tsv_output.tsv' file. Contains 5 columns.
    """
    with open('tsv_output.tsv','r',newline='') as fin,open('openCRAVAT_input.tsv','w',newline='') as fout:
        reader = csv.DictReader(fin,delimiter='\t')
        writer = csv.writer(fout,delimiter='\t')
        writer.writerow(['Chr', 'Position', 'Mutation_Strand', 'Ref_base', 'Alt_base'])
        
        for i, row in enumerate(reader):

            match = re.match(r'(\d+):g\.(\d+)(.)>(.)' , row[' HGVSG'])
            if match is not None:
                groups = match.groups()
                Chr = groups[0]
                Position = groups[1]
                Ref_Base = groups[2]
                Alt_Base = groups[3]
            
                
                # Chr = Pos = Strand = Ref = Alt = ""
            
                writer.writerow([Chr, Position, '+', Ref_Base, Alt_Base])


def csv_2_CRAVAT():
    csv_2_tsv()
    tsv_2_HGVSG()
    HGVSG_2_CRAVAT()

csv_2_CRAVAT()




