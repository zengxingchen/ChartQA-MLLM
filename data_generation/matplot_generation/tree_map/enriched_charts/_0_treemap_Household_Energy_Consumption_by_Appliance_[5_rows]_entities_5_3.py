
import matplotlib.pyplot as plt
import pandas as pd
import squarify # treemap library

# Data: Job postings in various cities for different job types
data = {
    "City": ["San Francisco", "San Francisco", "San Francisco", "New York", "New York", "New York",
             "Seattle", "Seattle", "Seattle", "Austin", "Austin", "Austin", 
             "Boston", "Boston", "Boston", "Chicago", "Chicago", "Chicago"],
    "Job Type": ["Software Developer", "Data Analyst", "DevOps Engineer", "Software Developer",
                 "Data Analyst", "DevOps Engineer", "Software Developer", "Data Analyst",
                 "DevOps Engineer", "Software Developer", "Data Analyst", "DevOps Engineer",
                 "Software Developer", "Data Analyst", "DevOps Engineer", "Software Developer",
                 "Data Analyst", "DevOps Engineer"],
    "Number of Postings": [300, 120, 90, 280, 130, 110, 200, 100, 80, 180, 90, 70, 160, 80, 60, 220, 110, 85]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group data by Job Type
grouped_data = df.groupby("Job Type").sum().reset_index()

# Define color list
colors = ["#6e7f80", "#536872", "#708090", "#5f9ea0", "#4f6a7f", "#5c8399", "#468b8f", "#3e7f7e", "#2f7f7f"]

# Plot
plt.figure(figsize=(12, 8))
squarify.plot(sizes=grouped_data['Number of Postings'], label=grouped_data['Job Type'], alpha=0.8, color=colors)
plt.title('Tech Job Postings by Type in Major Cities')
plt.axis('off')
plt.show()