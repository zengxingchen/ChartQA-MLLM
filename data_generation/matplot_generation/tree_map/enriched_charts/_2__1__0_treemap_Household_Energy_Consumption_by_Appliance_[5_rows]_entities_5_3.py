
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data: Mentions of various categories in different cities
data = {
    "City": ["New York", "New York", "New York", "San Francisco", "San Francisco", "San Francisco",
             "Seattle", "Seattle", "Seattle", "Austin", "Austin", "Austin", 
             "Boston", "Boston", "Boston", "Chicago", "Chicago", "Chicago",
             "Miami", "Miami", "Miami", "Los Angeles", "Los Angeles", "Los Angeles"],
    "Category": ["Mental Health", "Physical Health", "Nutrition", "Mental Health",
                 "Physical Health", "Nutrition", "Mental Health", "Physical Health",
                 "Nutrition", "Mental Health", "Physical Health", "Nutrition",
                 "Mental Health", "Physical Health", "Nutrition", "Mental Health",
                 "Physical Health", "Nutrition", "Mental Health", "Physical Health",
                 "Nutrition", "Mental Health", "Physical Health", "Nutrition"],
    "Number of Mentions": [320, 280, 150, 350, 290, 180, 200, 150, 120, 210, 170, 130, 190, 160, 110, 230, 190, 140, 180, 140, 100, 240, 200, 170]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group data by Category
grouped_data = df.groupby("Category").sum().reset_index()

# Define color list
colors = ["#FF6347", "#FFA07A", "#FFD700", "#ADFF2F", "#32CD32", "#66CDAA", "#00CED1", "#4682B4", "#1E90FF", "#9370DB", "#8A2BE2", "#BA55D3", "#FF69B4", "#FF1493", "#DB7093", "#FF4500", "#FF7F50", "#FF6347", "#FFD700", "#ADFF2F", "#32CD32", "#00FA9A", "#00CED1", "#4682B4"]

# Plot
plt.figure(figsize=(16, 12))
squarify.plot(sizes=grouped_data['Number of Mentions'], label=grouped_data['Category'], alpha=0.8, color=colors)
plt.title('Mentions of Health & Psychology Topics in Major Cities', fontsize=18, pad=30)
plt.axis('off')
plt.show()