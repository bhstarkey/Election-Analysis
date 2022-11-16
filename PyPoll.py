# Steps to get data we need
# 1. Get total number of votes cast
# 2. List all candidates who received votes
# 3. The percent of votes each candidate received
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import CSV to work with csv file and OS to interact with the operating system
# (dependencies)
import csv
import os
# Assign a variable for the file to load and the path
# File to read from
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign filename variable to a direct/indirect file path to file
# File to save to
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Use with statement to open function to write to file
#with open(file_to_save, "w") as txt_file:

# Open the election results and read the file
# : means indent next line, VSC does this automatically
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Print the header row
    headers = next(file_reader)
    print(headers)