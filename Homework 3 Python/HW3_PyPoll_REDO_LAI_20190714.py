#!/usr/bin/env python
# coding: utf-8

# ## PyPoll
# • In this challenge, you are tasked with helping a small, rural town modernize its vote- counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by- one, but unfortunately, his 
# concentration isn't what it used to be.)
# 
# • You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: 
# Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# 
# o The total number of votes cast
# o A complete list of candidates who received votes 
# o The percentage of votes each candidate won
# o The total number of votes each candidate won
# o The winner of the election based on popular vote.
# 
# • As an example, your analysis should look similar to the one below:
# • Election Results
# • -------------------------
# • Total Votes: "3521001"
# • -------------------------
# • Khan: 63.000% (2218231)
# • Correy: 20.000% (704200)
# • Li: 14.000% (492940)
# • O'Tooley: 3.000% (105630)
# • -------------------------
# • Winner: Khan
# • -------------------------
# 
# • In addition, your final script should both print the analysis to the terminal and export a
# text file with the results.

# In[116]:


# Import dependencies
import csv
import os


# In[117]:


file = os.path.join("election_data.csv")


# In[118]:


# Create lists
candidates = []
vote_counts = []
percentages = []
number_votes = 0


# In[124]:


with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader,None)
    
    for row in csvreader:
        
        # Count up votes and candidate
        candidate = row[2]
        number_votes = number_votes + 1
        # Wanted to try and do a print statement here, but didn't want to loop print,
        # so I tried making print statement outside of loop, but it messed up the rest of 
        # of my indentation.
        
        # Tally up votes of candidates and create a complete list
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] += 1
        else:
            candidates.append(candidate)
            vote_counts.append(1)
print("Counted and bucketed")


# In[121]:


print(number_votes)
print(candidates)
print(vote_counts)


# In[122]:


# Determine vote percentage
# Khan
khan_percent = vote_counts[0]/number_votes *100
print(round(khan_percent))
percentages.append(round(khan_percent))
# Correy
correy_percent = vote_counts[1]/number_votes *100
print(round(correy_percent))
percentages.append(round(correy_percent))
# Li
li_percent = vote_counts[2]/number_votes *100
print(round(li_percent))
percentages.append(round(li_percent))
# O'Tooley
otooley_percent = vote_counts[3]/number_votes *100
print(round(otooley_percent))
percentages.append(round(otooley_percent))


# In[123]:


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(number_votes))
print("-------------------------")
print("Khan: " + str(round(khan_percent)) + "%" + " (" + str(vote_counts[0]) + ")")
print("Correy: " + str(round(correy_percent)) + "%" + " (" + str(vote_counts[1]) + ")")
print("Li: " + str(round(li_percent)) + "%" + " (" + str(vote_counts[2]) + ")")
print("O'Tooley: "+ str(round(otooley_percent)) + "%" + " (" + str(vote_counts[3]) + ")")
print("-------------------------")
print("Winner: Khan")


# In[115]:


# Clean up and create output csv
cleaned_csv = zip(vote_counts, percentages, candidates)

# Set variable for output file
output_file = os.path.join("PyPoll_WinnerFile.csv")

# Open output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    
    # Write the header row
    writer.writerow(["Total Votes", "Candidate", "Vote Percentage"])
    
    # Write in zipped rows
    writer.writerows(cleaned_csv)


# In[ ]:




