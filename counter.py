import pandas as pd
import numpy as np
import csv

# Get input file path and output file name
input = raw_input('Input file path relative to this script (must be .csv): ')
output = raw_input('Name of output file (must be .csv): ')
# Read data from CSV using Pandas
data = pd.read_csv(input)
# Prepare CSV to write to
outfile = open(output,'a')
outwriter = csv.writer(outfile)
# Loop over columns
for column in data:
    # Get column counts of each string into new Pandas series
    colcounts = data[column].value_counts()
    # Create new Python array to add to
    # This will output as a row in the new CSV
    # The row should start with the category name which is currently held in the column variable
    array = [column]
    # Loop over each count
    # This will ignore blanks, should have five items for each
    for row in colcounts.iteritems():
        # Format string (Example: "The Register-Guard (123)")
        company = "{0} ({1})".format(row[0], row[1])
        # Append string to array
        # Each company will append from most votes to least
        array.append(company)
    # Write full row of category name and the five options with votes to output CSV
    outwriter.writerow(array)
