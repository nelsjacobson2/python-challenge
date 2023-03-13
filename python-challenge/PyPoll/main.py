# import pandas
import pandas as pd

# read data into pandas dataframe
election_df = pd.read_csv('/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/031323/python-challenge/PyPoll/Resources/election_data.csv')
election_df.head()

# get total number of votes
total_votes = len(election_df)

# get list of candidates who received votes
candidates = election_df["Candidate"].unique()

# calculate percentage of votes and total number of votes per candidate
votes_by_candidate = election_df["Candidate"].value_counts()
vote_percentages = votes_by_candidate / total_votes * 100

# determine who won
winner = votes_by_candidate.index[0]

#print who won
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes_by_candidate[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


#write results to analysis folder
output_file_path = "/Users/nels.jacobson2/Desktop/Analytics_Class_Folder/031323/python-challenge/PyPoll/Analysis/election_analysis.txt"
with open(output_file_path, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidates:
        file.write(f"{candidate}: {vote_percentages[candidate]:.3f}% ({votes_by_candidate[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")


