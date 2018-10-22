
# coding: utf-8

# In[2]:


import pandas as pd


# In[5]:


# import csv file
bank_data = "Resources/budget_data.csv"


# In[6]:


budget_data_pd = pd.read_csv(bank_data)
budget_data_pd.head()


# In[26]:


# count total months
date_count = len(budget_data_pd["Date"])

print("Total Months: ", date_count)


# In[28]:


# TOtal net profit/losses
net_amount = sum(budget_data_pd["Profit/Losses"])
print ("Total: $", net_amount)


# In[49]:


# Find greatest increase in profits
max_profit = max(budget_data_pd["Profit/Losses"])
print("Greatest increase in profits: $", max_profit)


# In[51]:


# Find greatest decrease in losses
max_loss = min(budget_data_pd["Profit/Losses"])
print("Greatest decrease in profits: $", max_loss)

