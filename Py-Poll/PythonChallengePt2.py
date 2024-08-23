
import csv
from pathlib import Path

# Assign file location with the pathlib library
csv_file_path = Path("/Users/diyasadekar/Downloads/Starter_Code 4/PyPoll/Resources/election_data.csv")

# Declare Variables
total_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

# Open CSV in default read mode with context manager
with open(csv_file_path, newline="", encoding="utf-8") as elections:
    # Store data under the csvreader variable
    csvreader = csv.reader(elections, delimiter=",")
    
    # Skip the header so we iterate through the actual values
    header = next(csvreader)
    
    # Iterate through each row in the CSV
    for row in csvreader:
        # Count the unique Voter ID's and store in variable called total_votes
        total_votes += 1
        
        # Count votes for each candidate
        if row[2] == "Charles Casper Stockham":
            stockham_votes += 1
        elif row[2] == "Diana DeGette":
            degette_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes += 1

# Determine the winner by creating a dictionary from the candidate names and votes
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [stockham_votes, degette_votes, doane_votes]

# Zip them together and create a dictionary
dict_candidates_and_votes = dict(zip(candidates, votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Calculate percentages
stockham_percent = (stockham_votes / total_votes) * 100
degette_percent = (degette_votes / total_votes) * 100
doane_percent = (doane_votes / total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print(f"-------------------------")
print(f"Winner: {key}")
print(f"-------------------------")

# Output file
output_file = Path("/Users/diyasadekar/Election_Results_Summary.txt")

with open(output_file, "w") as file:
    file.write(f"Election Results\n")
    file.write(f"-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"-------------------------\n")
    file.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})\n")
    file.write(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})\n")
    file.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})\n")
    file.write(f"-------------------------\n")
    file.write(f"Winner: {key}\n")
    file.write(f"-------------------------\n")
