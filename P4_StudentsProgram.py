#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Percentage of students who got less than 60 marks

from scipy.stats import norm
import numpy as np
# Given information
mean = 78
std_dev = 25
total_students = 100
score = 60
# Calculate z-score for 60
z_score = (score - mean) / std_dev
# Calculate the probability of getting a score less than 60
prob = norm.cdf(z_score)
# Calculate the percentage of students who got less than 60 marks
percent = prob * 100
# Print the result
print("Percentage of students who got less than 60 marks:", round(percent, 2), "%")


# In[7]:


# Percentage of students who got more than 70 marks

from scipy.stats import norm
import numpy as np
# Given information
mean = 78
std_dev = 25
total_students = 100
score = 70
# Calculate z-score for 70
z_score = (score - mean) / std_dev
# Calculate the probability of getting a more than 70
prob = norm.cdf(z_score)
# Calculate the percentage of students who got more than 70 marks
percent = (1-prob) * 100
print("Percentage of students who got more than 70 marks: ", round(percent, 2), " %")


# In[8]:


# Percentage of students who got more than 75 and less than 85

from scipy.stats import norm
import numpy as np
# Given information
mean = 78
std_dev = 25
total_students = 100
min_score = 75
max_score = 85
# Calculate z-score for 75
z_min_score = (min_score - mean) / std_dev
# Calculate z-score for 85
z_max_score = (max_score - mean) / std_dev
# Calculate the probability of getting less than 70
min_prob = norm.cdf(z_min_score)
# Calculate the probability of getting less than 85
max_prob = norm.cdf(z_max_score)
percent = (max_prob-min_prob) * 100
print("Percentage of students who got marks between 75 and 85 is", round(percent, 2), "%")


# In[ ]:




