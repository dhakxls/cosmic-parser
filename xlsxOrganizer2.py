import pandas as pd

def ageHisto():
    # Read the Excel file
    data = pd.read_excel('FILENAME_HERE.xlsx')

    # Define age categories
    bins = [0.9, 10.9, 20.9, 30.9, 40.9, 50.9, 60.9, 70.9, 80.9, 90.9, 100.9]
    labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

    # Categorize age column
    data['Age Category'] = pd.cut(data[' AGE'], bins=bins, labels=labels, right=True)

    # Group by PRIMARY_HISTOLOGY and Age Category and calculate the counts
    grouped_data = data.groupby([' PRIMARY_HISTOLOGY', 'Age Category']).size().reset_index(name='Counts')

    # Sort by PRIMARY_HISTOLOGY and Age Category
    sorted_data = grouped_data.sort_values(by=[' PRIMARY_HISTOLOGY', 'Age Category'])

    # Set display options to show all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    # Print the sorted data
    print(sorted_data)

def ageTissue():
    # Read the Excel file
    data = pd.read_excel('FILENAME_HERE.xlsx')

    # Define age categories
    bins = [0.9, 10.9, 20.9, 30.9, 40.9, 50.9, 60.9, 70.9, 80.9, 90.9, 100.9]
    labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

    # Categorize age column
    data['Age Category'] = pd.cut(data[' AGE'], bins=bins, labels=labels, right=True)

    # Group by PRIMARY_HISTOLOGY and Age Category and calculate the counts
    grouped_data = data.groupby([' PRIMARY_SITE', 'Age Category']).size().reset_index(name='Counts')

    # Sort by PRIMARY_HISTOLOGY and Age Category
    sorted_data = grouped_data.sort_values(by=[' PRIMARY_SITE', 'Age Category'])

    # Set display options to show all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    # Print the sorted data
    print(sorted_data)

# Toggle which function to run
ageTissue()  
# ageHisto()
