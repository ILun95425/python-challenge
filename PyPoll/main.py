import os
import csv


filein = r"C:\Users\ilun1\OneDrive\桌面\GitHub\python-challenge\PyPoll\Resources\election_data.csv"


# define required variables

candidatesNvotes= {}
total_votes = 0

with open(filein, 'r') as input_data:
    read = csv.reader(input_data, delimiter= ',')

# skip the header

    header = next(read)

# loop csv
    
    for row in read:
        
        if not row[2] in candidatesNvotes.keys():  
            candidatesNvotes[row[2]] = 1          
                                                                                                     
        else:                                      
            candidatesNvotes[row[2]] += 1

total_votes = sum(candidatesNvotes.values())

candidate_results = {}

for candidate, votes in candidatesNvotes.items():
    vote_percent = votes / total_votes
    candidate_results[candidate] = {'Votes': votes, 'Percentage': vote_percent}

winner = max(candidate_results, key=lambda x: candidate_results[x]['Votes'])

#     for row in read:
#         total_votes += 1
#         candidate = row[2]  
#         if candidate not in candidates:
#             candidates.append(candidate)
#             candidate_results[candidate] = {'Votes': 0, 'Percentage': 0}
#         candidate_results[candidate]['Votes'] += 1


# winner = max(candidate_results, key=lambda x: candidate_results[x]['Votes'])



# print method 2

print("Election Results")
print("---------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------")
for candidate, results in candidate_results.items():
    print(f"{candidate}: {results['Percentage']:.3f}% ({results['Votes']})")
print("---------------------------------")
print(f"Winner: {winner}")
print("---------------------------------")


# output text file method 2

output_folder = r"C:\Users\ilun1\OneDrive\桌面\GitHub\python-challenge\PyPoll"
fileout = os.path.join(output_folder, 'Election Results.txt')

with open(fileout, 'w') as file:
    file.write("Election Results\n")
    file.write("---------------------------------\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("---------------------------------\n")
    for candidate, results in candidate_results.items():
        file.write(f"{candidate}: {results['Percentage']:.3f}% ({results['Votes']})\n")
    file.write("---------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("---------------------------------\n")