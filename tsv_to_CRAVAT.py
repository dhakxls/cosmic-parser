import pandas as pd
import csv
import re

filename = '<Insert Filename Here>'

def tsvToCRAVAT():
    """
    Writes a copy of the tsv file into another tsv file, 'cravat_output.tsv', 
    that contains just the 'HGVSG' column

    Then takes that tsv file and create a new tsv file, 'CRAVAT_input.tsv' containing the valid columns
    to perform the CRAVAT analysis
    """
    with open(filename,'r',newline='') as fin,open('cravat_output.tsv','w',newline='') as fout:
        reader = csv.DictReader(fin,delimiter='\t')
        writer = csv.DictWriter(fout,delimiter='\t',fieldnames=['HGVSG' , 'Primary site'],extrasaction='ignore')
        writer.writeheader()
        for row in reader:
            writer.writerow(row)

    with open('cravat_output.tsv','r',newline='') as fin,open('CRAVAT_input.tsv','w',newline='') as fout:
        reader = csv.DictReader(fin,delimiter='\t')
        writer = csv.writer(fout,delimiter='\t')
        writer.writerow(['UID_#', 'Chr', 'Position', 'Mutation_Strand', 'Ref_base', 'Alt_base', 'Primary site'])

        
        for UID, row in enumerate(reader):

            match = re.match(r'(\d+):g\.(\d+)(.)>(.)' , row['HGVSG'])
            if match is not None:
                groups = match.groups()
                Chr = groups[0]
                Position = groups[1]
                Ref_Base = groups[2]
                Alt_Base = groups[3]

                Site = row['Primary site']
                # Chr = Pos = Strand = Ref = Alt = ""
          
                writer.writerow([UID, Chr, Position, '+', Ref_Base, Alt_Base, Site])

def tsvToCRAVAT_AgeFilter():
    """
    Filters out all of the possible mutations with an age associated with it. Writes out a new
    tsv file, 'CRAVAT_input_age.tsv', containing all of the valid CRAVAT inputs with the
    age filter
    """
    with open(filename,'r',newline='') as fin,open('cravat_output.tsv','w',newline='') as fout:
        reader = csv.DictReader(fin,delimiter='\t')
        writer = csv.DictWriter(fout,delimiter='\t',fieldnames=['HGVSG' , 'Primary site', 'Age'],extrasaction='ignore')
        writer.writeheader()
        for row in reader:
            writer.writerow(row)

    with open('cravat_output.tsv','r',newline='') as fin,open('CRAVAT_input_age.tsv','w',newline='') as fout:
        reader = csv.DictReader(fin,delimiter='\t')
        writer = csv.writer(fout,delimiter='\t')
        writer.writerow(['UID_#', 'Chr', 'Position', 'Mutation_Strand', 'Ref_base', 'Alt_base', 'Primary site'])

        
        for UID, row in enumerate(reader):

            match1 = re.match(r"^(?!\s*$).+", row['Age'])

            match = re.match(r'(\d+):g\.(\d+)(.)>(.)' , row['HGVSG'])
            if match1 is not None:
                if match is not None:
                    groups = match.groups()
                    Chr = groups[0]
                    Position = groups[1]
                    Ref_Base = groups[2]
                    Alt_Base = groups[3]

                    Site = row['Primary site']
                    Age = row['Age']
                    # Chr = Pos = Strand = Ref = Alt = ""
            
                    writer.writerow([UID, Chr, Position, '+', Ref_Base, Alt_Base, Site, Age])

def AgeRangeFilter():
    """
    Filters out the total age applicable mutations to certain age ranges and writes them to a tsv file
    with the valid CRAVAT input columns
    """
    # run tsvToCRAVAT_AgeFilter() first
    #change cravat input file name to the right age range
    with open('cravat_output.tsv','r',newline='') as fin,open('<Insert Filename with an Age Range Here>','w',newline='') as fout:
            reader = csv.DictReader(fin,delimiter='\t')
            writer = csv.writer(fout,delimiter='\t')
            writer.writerow(['UID_#', 'Chr', 'Position', 'Mutation_Strand', 'Ref_base', 'Alt_base', 'Primary site'])

            
            for UID, row in enumerate(reader):

                match1 = re.match(r"^(?!\s*$).+", row['Age'])
                
                match = re.match(r'(\d+):g\.(\d+)(.)>(.)' , row['HGVSG'])

                if match1:
                    matchnum = float(match1.group())
                # change number to whatever age you want the range to be in
                if matchnum > 100.0:
                        
                        if match is not None:
                            groups = match.groups()
                            Chr = groups[0]
                            Position = groups[1]
                            Ref_Base = groups[2]
                            Alt_Base = groups[3]

                            Site = row['Primary site']
                            # Chr = Pos = Strand = Ref = Alt = ""
                    
                            writer.writerow([UID, Chr, Position, '+', Ref_Base, Alt_Base, Site])


# tsvToCRAVAT()
# tsvToCRAVAT_AgeFilter()
AgeRangeFilter()