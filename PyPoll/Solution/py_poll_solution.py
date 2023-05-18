# Import dependencies
import os
import csv
import collections
from collections import Counter

# Define each variables
candidates = []
votes_per_candidate = []

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join('..', 'Resources', 'election_data.csv')

# Open and Read csv
with open(election_data_csv_path, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header
    csv_header = next(csvfile)

    #print(f"Header: {csv_header}")

    # Read the eacg row of the data after the header
    for row in csv_reader:
        candidates.append(row[2])

    # Sorting the list
    sorted_list = sorted(candidates)

    #sorted_list = sorted(voters_candidates, reverse=True) 
    #sorted_list.sort(reverse=True) 

    # Arrange the sorting list
    arrange_list = sorted_list

    # Count votes per candidate in most common outcome and append to a list
    count_candidate = Counter (arrange_list)
    votes_per_candidate.append(count_candidate.most_common())


    # Calculate the % of votes per candidate
    for item in votes_per_candidate:
     
     first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
     second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
     third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
     
     #print(c.most_common())
     #print(c.values())
     #print(c.keys())
     #print(sum(c.values()))

     
##### Print the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


##### Export the analysis into a text file
election_results = os.path.join('..', 'Solution', 'election_results.text')
with open(election_results,'w') as outfile:
   
   outfile.write("Election Results\n")
   outfile.write("-------------------------\n")
   outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
   outfile.write("-------------------------\n")
   outfile.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
   outfile.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
   outfile.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
   outfile.write("-------------------------\n")
   outfile.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
   outfile.write("-------------------------\n")
