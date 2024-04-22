#!/usr/bin/env python
# coding: utf-8

# # HR DATA ANALYSIS

# Activities to complete the Project
# Data cleansing involves removing unnecessary columns.
# Giving the columns new names.
# Eliminating redundant entries.
# sanitizing specific columns.
# Eliminate the dataset's NaN values.
# Look for a few more changes if necessary

# # Import required libraries 

# In[1]:


import numpy as np
import pandas as pd


# # Import Data Set

# In[2]:


# Load the dataset
file_path = "C:\\Users\\udayu\\Downloads\\HR Data.csv"
hr_data = pd.read_csv(file_path)


# # data cleaning

# In[5]:


# Data cleansing
# Remove unnecessary columns
columns_to_drop = ['EmployeeCount', 'Over18', 'StandardHours']
hr_data = hr_data.drop(columns=columns_to_drop)
# Eliminate NaN values
hr_data = hr_data.dropna()


# Save the cleaned data to a new CSV file
cleaned_file_path = r"C:\Users\udayu\Downloads\Cleaned_HR_Data.csv"
hr_data.to_csv(cleaned_file_path, index=False)


# In[ ]:





# In[ ]:




