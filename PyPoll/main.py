import os
import pandas as pd

er= pd.read_csv('PyPoll/Resources/election_data.csv')

total_votes= er['Ballot ID'].nunique()

candidates= er['Candidate'].unique()

candidate_results= {}

for candidate in candidates:
    
    candidate_votes= er[er['Candidate'] == candidate]['Ballot ID'].count()
    percentage= (candidate_votes / total_votes) * 100
    candidate_results[candidate]= {
        'Votes': candidate_votes, 'Percentage': percentage
        }
    
winner= max(candidate_results, key=lambda x: candidate_results[x]['Votes'])


#print



print("Election Results")
print("---------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_results[candidate]['Percentage']:.3f}% ({candidate_results[candidate]['Votes']})")
print("---------------------------------")
print(f"Winner: {winner}")
print("---------------------------------")


#addition

output_file= 'Election Results.txt'

with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("---------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("---------------------------------\n")
    for candidate in candidates:
        file.write(f"{candidate}: {candidate_results[candidate]['Percentage']:.3f}% ({candidate_results[candidate]['Votes']})\n")
    file.write("---------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("---------------------------------\n")