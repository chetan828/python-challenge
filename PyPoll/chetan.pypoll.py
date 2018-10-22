
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


poll_data = "Resources/election_data.csv"


# In[6]:


vote_data_pd = pd.read_csv(poll_data)
vote_data_pd.head()


# In[7]:


# total number of votes cast
vote_count = len(vote_data_pd["Voter ID"])
print("Election Results")
print("----------------------")
print("Total number of votes cast: ", vote_count)
print("----------------------")


# In[8]:


# list of candidates and votes
vote_data_pd["Candidate"].value_counts()


# In[17]:


khan_vote = 2218231
correy_vote = 704200
li_vote = 492940
otooley_vote = 105630

khan_pct = khan_vote/vote_count*100
correy_pct = correy_vote/vote_count*100
li_pct = li_vote/vote_count*100
otooley_pct = otooley_vote/vote_count*100

print ("Khan:", khan_pct,"%", khan_vote)
print ("Correy:", correy_pct,"%", correy_vote)
print ("Li:", li_pct,"%", li_vote)
print ("O'Tooley:", otooley_pct,"%", otooley_vote)
print ("-----------------------")


# In[31]:


#print winner name
Khan = khan_vote
Correy = correy_vote
Li = li_vote
OTooley = otooley_vote
winner = max(Khan, Correy, Li, OTooley)
if winner == Khan:
    print ("Winner: Khan")
elif winner == Correy:
    print ("Winner: Correy")
elif winner == Li:
    print ("Winner: Li")
elif winner == OTooley:
    print ("Winner: O'Tooley")
                                  

