#You are tasked with helping a small, rural town modernize its vote-counting process. 
#You will be give a set of poll data called election_data.csv. 
#The dataset is composed of three columns: Voter ID, County, and Candidate.
#Import important modules
import os
import csv
import codecs


#Open and read database file
csvpath = os.path.join("Resources", "election_data.csv")

voter_id = []
county = []
candidate = []

with open(csvpath, newline='', encoding='utf8') as csvfile:

    #Read and pull data
    csvreader = csv.reader(csvfile, delimiter=',')

    # Then store the contents of the date and profit/loss columns.
    for row in csvreader:
        
            voter_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
        
    del voter_id[0]
    del county[0]
    del candidate[0]

    
#The total number of votes cast
vote_count = len(voter_id)


#A complete list of candidates who received votes
candidate_list = []

for name in candidate:
    
    if name not in candidate_list:
        candidate_list.append(name)

        
#The total number of votes and the percentage of votes each candidate won
k_vote = 0
c_vote = 0
l_vote = 0
o_vote = 0


for vote in candidate:
    if vote == 'Khan':
        k_vote = k_vote + 1
        
    elif vote == 'Correy':
        c_vote = c_vote + 1
        
    elif vote == 'Li':
        l_vote = l_vote + 1
        
    elif vote == "O'Tooley":
        o_vote = o_vote + 1
        
candidate_vote = [k_vote, c_vote, l_vote, o_vote]
candidate_per = []

for i in candidate_vote:
    
    per = round((i/vote_count)*100, 4)
    candidate_per.append(per)

    
#The winner of the election based on popular vote.
count = 0
int_candidate = candidate_vote[0]
winner = candidate_list[0]

for j in candidate_vote:
    
    if j> int_candidate:
        winner = candidate_list[count]
        int_candidate = j
    else:
        count = count + 1

        
#Print results to terminal
c = 0

print('Election Results')
print('----------------------------')
print(f'Total Votes: {vote_count}')
print('----------------------------')
for j in candidate_list:
    print(f'{candidate_list[c]}: {candidate_per[c]}% ({candidate_vote[c]})')
    c = c + 1 
print('----------------------------')
print(f'Winner: {winner}')
print('----------------------------')
Election Results
----------------------------
Total Votes: 3521001
----------------------------
Khan: 63.0% (2218231)
Correy: 20.0% (704200)
Li: 14.0% (492940)
O'Tooley: 3.0% (105630)
----------------------------
Winner: Khan
----------------------------


#Print results to text file
info = zip(candidate_list, candidate_per, candidate_vote)

# save the output file path
output_file = os.path.join("election_results.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Election Results"])
    writer.writerow(["Total Votes", vote_count])
    writer.writerow(["Candidate", 'Percentage of Votes (%)', 'Total Number of Votes'])
    writer.writerows(info)
    writer.writerow(["Winner", winner])