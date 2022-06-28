import pandas as pd
import csv
import re

filename = '<Insert Filename Here>'

def tsvToOpenCRAVAT():
    """
    Writes a copy of the tsv file into another tsv file, 'opencravat_output.tsv', 
    that contains just the 'HGVSG' column

    Then takes that tsv file and create a new tsv file, 'openCRAVAT_input.tsv' containing the valid columns
    to perform the CRAVAT analysis
    """
    with open(filename,'r',newline='') as fin,open('opencravat_output.tsv','w',newline='') as fout:
        reader = csv.DictReader(fin,delimiter='\t')
        writer = csv.DictWriter(fout,delimiter='\t',fieldnames=['HGVSG'],extrasaction='ignore')
        writer.writeheader()
        for row in reader:
            writer.writerow(row)

    with open('opencravat_output.tsv','r',newline='') as fin,open('openCRAVAT_input.tsv','w',newline='') as fout:
        reader = csv.DictReader(fin,delimiter='\t')
        writer = csv.writer(fout,delimiter='\t')
        writer.writerow(['Chr', 'Position', 'Mutation_Strand', 'Ref_base', 'Alt_base'])

        
        for i, row in enumerate(reader):

            match = re.match(r'(\d+):g\.(\d+)(.)>(.)' , row['HGVSG'])
            if match is not None:
                groups = match.groups()
                Chr = groups[0]
                Position = groups[1]
                Ref_Base = groups[2]
                Alt_Base = groups[3]

                
                # Chr = Pos = Strand = Ref = Alt = ""
          
                writer.writerow([Chr, Position, '+', Ref_Base, Alt_Base])

def tsvToOpenCRAVAT_AgeFilter():
    """
    Filters out all of the possible mutations with an age associated with it. Writes out a new
    tsv file, 'openCRAVAT_input_age.tsv', containing all of the valid CRAVAT inputs with the
    age filter
    """
    with open(filename,'r',newline='') as fin,open('output.tsv','w',newline='') as fout:
        reader = csv.DictReader(fin,delimiter='\t')
        writer = csv.DictWriter(fout,delimiter='\t',fieldnames=['HGVSG', 'Age'],extrasaction='ignore')
        writer.writeheader()
        for row in reader:
            writer.writerow(row)

    with open('opencravat_output.tsv','r',newline='') as fin,open('openCRAVAT_input_age.tsv','w',newline='') as fout:
        reader = csv.DictReader(fin,delimiter='\t')
        writer = csv.writer(fout,delimiter='\t')
        writer.writerow(['Chr', 'Position', 'Mutation_Strand', 'Ref_base', 'Alt_base'])

        
        for i, row in enumerate(reader):

            match1 = re.match(r"^(?!\s*$).+", row['Age'])

            match = re.match(r'(\d+):g\.(\d+)(.)>(.)' , row['HGVSG'])
            if match1 is not None:
                if match is not None:
                    groups = match.groups()
                    Chr = groups[0]
                    Position = groups[1]
                    Ref_Base = groups[2]
                    Alt_Base = groups[3]

                    
                    # Chr = Pos = Strand = Ref = Alt = ""
            
                    writer.writerow([Chr, Position, '+', Ref_Base, Alt_Base])

def AgeRangeFilter():
    """
    Filters out the total age applicable mutations to certain age ranges and writes them to a tsv file
    with the valid CRAVAT input columns
    """
    # run tsvToOpenCRAVAT_AgeFilter() first
    #change cravat input file name to the right age range
    with open('opencravat_output.tsv','r',newline='') as fin,open('<Insert Filename with an Age Range Here>','w',newline='') as fout:
            reader = csv.DictReader(fin,delimiter='\t')
            writer = csv.writer(fout,delimiter='\t')
            writer.writerow(['Chr', 'Position', 'Mutation_Strand', 'Ref_base', 'Alt_base'])

            
            for i, row in enumerate(reader):

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

                            
                            # Chr = Pos = Strand = Ref = Alt = ""
                    
                            writer.writerow([Chr, Position, '+', Ref_Base, Alt_Base])

### Adjust which functions you want to run

# tsvToOpenCRAVAT()
# tsvToOpenCRAVAT_AgeFilter()
AgeRangeFilter()