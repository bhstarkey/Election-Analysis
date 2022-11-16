# Steps to get data we need
# 1. Get total number of votes cast
# 2. List all candidates who received votes
# 3. The percent of votes each candidate received
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Notes Key
## VC = Vote Count
## CN Candidate Name
## AV = Accrue votes
## PV = Percent votes

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

# VC1. Inititalize a total vote counter
#       Variable must be initialized before file is opened so it is set to zero everytime file is opened before calculations
total_votes = 0

# CN1. Create empty list for candidate names
candidate_options = []

# AV1. Create empty dictionary to store candidate vote counts
candidate_votes = {}


## open(file_to_save, "w") as txt_file:
# Use with statement to open function to write to file
# Open the election results and read the file
# : means indent next line, VSC does this automatically
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Read each row in the CSV File
    for row in file_reader:
        # VC2. Add to the total vote count
        total_votes += 1

        #CN2. Read candidate name from each row
        candidate_name = row[2]
        
        #CN3. If the candidate name has not been added to the list, add it to the list
        if candidate_name not in candidate_options:
             
             # Add it to the list of candidates
             candidate_options.append(candidate_name)

             #AV2. Create key from candidate names and set variable to 0 to start counting votes
             candidate_votes[candidate_name] = 0

        #AV3. Add a vote to that candidates count
        # Moving line out of if statement, allows it to operate in the for loop for each row in the file
        candidate_votes[candidate_name] +=1

# Determine percent of votes each candidate receivec
#PV1. Iterate through all candidate options
for candidate_name in candidate_votes:
            
    #PV2. Retrieve number of votes each candidate received
    votes = candidate_votes[candidate_name]

    #PV3. Calculate the percent votes each candidate received
    vote_percentage = (votes / total_votes) * 100

    #PV4. Print what percent of votes each candidate received
    print(f"{candidate_name} received {vote_percentage:.2f}% of the vote")


# Print the total votes.
# print(candidate_votes)