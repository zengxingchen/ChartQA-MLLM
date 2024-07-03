
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data: Mentions of various categories in different cities
data = {
    "City": ["New York", "New York", "New York", "San Francisco", "San Francisco", "San Francisco",
             "Seattle", "Seattle", "Seattle", "Austin", "Austin", "Austin", 
             "Boston", "Boston", "Boston", "Chicago", "Chicago", "Chicago",
             "Miami", "Miami", "Miami", "Los Angeles", "Los Angeles", "Los Angeles"],
    "Category": ["Concerts", "Theater", "Opera", "Concerts",
                 "Theater", "Opera", "Concerts", "Theater",
                 "Opera", "Concerts", "Theater", "Opera",
                 "Concerts", "Theater", "Opera", "Concerts",
                 "Theater", "Opera", "Concerts", "Theater",
                 "Opera", "Concerts", "Theater", "Opera"],
    "Number of Mentions": [350, 300, 180, 340, 290, 200, 220, 170, 150, 230, 190, 140, 210, 180, 160, 260, 230, 190, 200, 170, 140, 280, 240, 200]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group data by Category
grouped_data = df.groupby("Category").sum().reset_index()

# Define color list
colors = ["#FF5733", "#C70039", "#900C3F", "#581845", "#FFC300", "#FF5733", 
          "#DAF7A6", "#FFC300", "#FF5733", "#C70039", "#900C3F", "#581845", 
          "#DAF7A6", "#FFC300", "#FF5733", "#C70039", "#900C3F", "#581845", 
          "#DAF7A6", "#FFC300", "#FF5733", "#C70039", "#900C3F", "#581845"]

# Plot
plt.figure(figsize=(20, 14))
squarify.plot(sizes=grouped_data['Number of Mentions'], label=grouped_data['Category'], alpha=0.8, color=colors)
plt.title('Mentions of Music & Performing Arts Topics in Major Cities', fontsize=20, pad=30)
plt.axis('off')
plt.show()