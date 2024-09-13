#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)
df.isna().sum()


# In[2]:


import pandas as pd

# Load the dataset from your local machine
df = pd.read_csv('path_to_your_downloaded_file/villagers.csv')

# Display the dimensions of the dataset
print(df.shape)


# In[3]:


import pandas as pd

# Load the dataset from your local machine
df = pd.read_csv('"C:\Users\adeel\Downloads\villagers.csv"')

# Display the dimensions of the dataset
print(df.shape)


# In[4]:


import pandas as pd

# Load the dataset from your local machine
df = pd.read_csv("C:\Users\adeel\Downloads\villagers.csv")

# Display the dimensions of the dataset
print(df.shape)


# In[5]:


import pandas as pd

# Load the dataset from your local machine
df = pd.read_csv("C:\\Users\\adeel\\Downloads\\villagers.csv")


# Display the dimensions of the dataset
print(df.shape)


# In[6]:


import pandas as pd

# Load the dataset from your local machine
df = pd.read_csv(r"C:\Users\adeel\Downloads\villagers.csv")



# Display the dimensions of the dataset
print(df.shape)


# In[7]:


import pandas as pd

# Load the dataset from the provided URL
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Display the dimensions of the dataset
print(df.shape)


# The definition of an observation could be the specific data that is stored for an individual, while a variable is just the type of data stored for each observation. So in a spreadsheet, observations could represent rows, while variables can represent columns

# In[9]:


import pandas as pd

# Load the dataset from the provided URL
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)

# Display a statistical summary of the numerical columns
df.describe()


# In[10]:


# Display the distribution of values for each non-numerical column
for column in df.select_dtypes(include=['object']).columns:
    print(f"Summary of {column}:")
    print(df[column].value_counts())
    print("\n")


# In[11]:


import pandas as pd

# Load the dataset from the provided URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Display the dimensions of the dataset
print("Dimensions of the dataset:", df.shape)

# Display the summary statistics of the dataset
print("\nSummary statistics of the dataset:")
print(df.describe(include='all'))


# In[12]:


#Here is an example of the discrepancies between the data
import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Display the dimensions of the dataset
print("Dimensions of the dataset:", df.shape)

# Display the summary statistics of the dataset
print("\nSummary statistics of the dataset:")
print(df.describe(include='all'))


# There are discrepancies in the columns analyzed because df.shape counts columns of any datatype while df.describe only counts numerical ones. In terms of the count column df.shape does not provide count of non-null values, while df.describe() does for each column,leading to a discrepancy which can be observed above.

# The main difference between an attribute and method is that an attribute provides information about an object, while methods perform calculations/computations on the object. For example, an attribute can find the datatype of an object, while a method can summarize the data through various steps.
# 

# COPILOT SUMMARY:
# 
# Dataset Dimensions:
# You provided a link to a dataset and wanted to understand its dimensions.
# We attempted to load the dataset from the URL, but encountered an error.
# I suggested loading the dataset locally and provided code to check its dimensions.
# File Path Issue:
# You encountered a SyntaxError due to backslashes in the file path.
# I explained how to fix it using double backslashes, raw strings, or forward slashes.
# File Not Found Error:
# You faced a FileNotFoundError.
# I suggested verifying the file path and provided code to list files in the directory.
# Using URL to Load Dataset:
# You asked about using a URL to load the dataset.
# We tried loading the dataset from the URL again, but encountered another error.
# Understanding Observations and Variables:
# I explained the concepts of observations (rows) and variables (columns) in the context of your dataset.
# Summarizing Columns:
# You asked how to provide simple summaries of the columns.
# I provided code to get statistical summaries for numerical columns and value counts for non-numerical columns.
# Dataset Type:
# You asked if your dataset was numerical or non-numerical.
# I explained how to check the data types of each column using pandas.
# Analyzing Titanic Dataset:
# You provided a link to the Titanic dataset and wanted to analyze its dimensions and summary statistics.
# We attempted to load and analyze the dataset, but encountered an error.
# Attributes vs. Methods:
# You asked about the difference between attributes and methods in pandas.
# I explained that attributes provide information about the object and are accessed without parentheses, while methods perform actions and are called with parentheses.
# 

# Postlecture

# Q6.
# Count: The number of values in a column that are not null.
# Mean: Average of the values in a column.
# Std: The standard deviation which measures the variation of the values, essentially checking how spread out they are.
# Min: The smallest value.
# 25%: The value below which the first quarter of data falls when sorted.
# 50%: The middle value when data is sorted
# 75%: The value below which 75% of data falls when sorted.
# Max: The largest value.

# Q: Provide an example of "the opposite use case" in which using del df['col'] might be preferred over using df.dropna()

# In[19]:


import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, None, 4], 'B': [None, 2, 3, 4], 'C': [1, None, 3, 4]}
df = pd.DataFrame(data)

# Using del df['B']
del df['B']

print(df)


# In the above case, I want to remove a column that is not needed for analysis, so I want to remove it entirely.

# Q: Provide an example of a "use case" in which using df.dropna() might be peferred over using del df['col']

# In[21]:


import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, None, 4], 'B': [None, 2, 3, 4], 'C': [1, None, 3, 4]}
df = pd.DataFrame(data)

# Using df.dropna()
df_cleaned = df.dropna()

print(df_cleaned)


# In the above case, I want to remove rows with missing values so df.dropna() is preferred.

# 

# Q: Discuss why applying del df['col'] before df.dropna() when both are used together could be important
# 
# Ans. Using del df['col'] first can help to remove unimportant/irrelevant columns, instead of removing rows with missing values which would otherwise be complete.

# Q: Remove all missing data from one of the datasets you're considering using some combination of del df['col'] and/or df.dropna() and give a justification for your approach, including a "before and after" report of the results of your approach for your dataset.

# In[22]:


import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, None, 4], 'B': [None, 2, 3, 4], 'C': [1, None, 3, 4]}
df = pd.DataFrame(data)

print("Before:")
print(df)


# In this case I am judging column B as irrelevant for analysis so I will remove it and then drop rows with missing values.

# In[23]:


# Remove irrelevant column
del df['B']

# Drop rows with missing values
df_cleaned = df.dropna()

print("After:")
print(df_cleaned)


# Through this approach, we make sure we only drop rows based on columns relevant for analysis.(losing as little important data as possible)

# Q8:

# The command "df.groupby("col1")["col2"].describe()" does two main things, namely grouping and describing.The first part groups the data by unique values in the column (col1), creating seperate groups for each unique value.It then "describes" in the second part. producing summary statistics such as mean and median for the second column (col2).

# In[25]:


import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataset
print(df.head())


# In[26]:


# adjusted the code from ai to do it differently 
grouped_description = df.groupby("age")["class"].describe()
print(grouped_description)


# In[27]:


# adjusted the code from ai to do it differently 
grouped_description = df.groupby("age")["class"].describe()
grouped_description


# Part 2:
# Q: Assuming you've not yet removed missing values in the manner of question "7" above, df.describe() would have different values in the count value for different data columns depending on the missingness present in the original data. Why do these capture something fundamentally different from the values in the count that result from doing something like df.groupby("col1")["col2"].describe()?
# 
# Ans. 

# The reason lies in the scope of each of these methods. ?df.describe()" looks at the whole data, while "df.groupby("col1")["col2"].describe()" looks at specific groups within the data.The second method finds counts values by only showing how many non missing values are in col2 for each group of col 1, while the first method calculates this for each column.

# Part 3

# In[1]:


import pandas as pd
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)
df.isna().sum()


# In[2]:


url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)
df.isna().sum()


# In[1]:


url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)
df.isna().sum()


# In[2]:


import pandas as pd

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)
df.isna().sum()


# In[4]:


import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

print(df.head())


# In[5]:


import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanics.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataset
print(df.head())


# chatgpt instantly pointed out that url might be incorrect and was easier than google search.

# In[6]:


grouped_description = DF.groupby("age")["class"].describe()
grouped_description


# 

# In[7]:


grouped_description = df.groupby("age")["class"].describe()
grouped_description


# In[8]:


import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url

print(df.head())


# In[ ]:


import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

print(df.head())


# In[9]:


grouped_description = df.groupby("age")["class"].describle()
grouped_description


# In[10]:


grouped_description = df.groupby("age")["class"].describe()
grouped_description


# In[11]:


grouped_description = df.groupby("AGE")["CLASS"].describe()
grouped_description


# In[12]:


print(df.columns)


# In[13]:


grouped_description = df.groupby("age")["class"].describe()
grouped_description


# In[14]:


grouped_description = df.groupby("age")["class].describe()
grouped_description


# In[15]:


grouped_description = df.groupby("age")["class"].describe()
grouped_description


# Answer: In almost all cases, chatgpt was quicker than google, and much easier in some cases. For some of the erros, such as the missing paranthesis (syntax error) or Nameerror, it could be said that both were equally quick.

# Q9: Yes

# Some parts of the chats have been lost but here is the summary

# Sure, here’s a summary of our interactions:
# 
# NameError: pd is not defined:
# You encountered a NameError because the pandas library wasn’t imported.
# Solution: Add import pandas as pd at the beginning of your code.
# HTTPError when loading the Titanic dataset:
# You faced an HTTPError due to a typo in the URL.
# Solution: Correct the URL to https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv.
# NameError: DF is not defined:
# You encountered a NameError because the variable DF wasn’t defined.
# Solution: Use the correct variable name df.
# SyntaxError: ‘(’ was never closed:
# You had a SyntaxError due to an unmatched parenthesis.
# Solution: Ensure every opening parenthesis ( has a corresponding closing parenthesis ).
# AttributeError: ‘SeriesGroupBy’ object has no attribute ‘describle’:
# You faced an AttributeError due to a typo in the method name.
# Solution: Use the correct method name describe().
# KeyError: ‘AGE’ or ‘CLASS’:
# You encountered a KeyError because the column names were case-sensitive.
# Solution: Use the correct column names age and class.
# SyntaxError: unterminated string literal:
# You had a SyntaxError due to an unterminated string literal.
# Solution: Ensure the string "class" is properly closed.
# If you need any more help or have additional questions, feel free to ask! Good luck with your homework assignment
