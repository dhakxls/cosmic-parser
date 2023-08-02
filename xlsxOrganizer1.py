import pandas as pd

# Gene test
name = 'FILENAME_HERE.xlsx'

df = pd.read_excel(name, sheet_name='Original copy') # can also index sheet by name or fetch all sheets
primarytissue = df[' PRIMARY_SITE'].tolist()

df = pd.read_excel(name, sheet_name='Original copy')
histology = df[' PRIMARY_HISTOLOGY'].tolist()

df = pd.read_excel(name, sheet_name='Original copy')
mutationdesc = df[' MUTATION_DESCRIPTION'].tolist()

df = pd.read_excel(name, sheet_name='Original copy')
fathmm = df[' FATHMM_PREDICTION'].tolist()

df = pd.read_excel(name, sheet_name='Original copy')
mutationfrequency = df[' MUTATION_AA'].tolist()

#count the amount of repeats in a list for each element
def unique(mylist):
    # dg variagle to just see if the list can be printed. Testing checkpoint
    # dg = pd.DataFrame(mylist)
        # print(dg)

    unique_dg = df.pivot_table(index=[mylist], aggfunc='size')
    print(unique_dg)

print(" ")
print("These are the type of tissues plus their amount affected: ")
print(" ")
unique(primarytissue)

print(" ")
print("These are the type of histology plus their amount affected: ")
print(" ")
unique(histology)

print(" ")
print("These are the type of mutation description plus their amount affected: ")
print(" ")
unique(mutationdesc)

print(" ")
print("These are the type of FATHMM prediction plus their amount: ")
print(" ")
unique(fathmm)

print(" ")
print("These are the frequencies of mutations: ")
print(" ")
unique(mutationfrequency)
