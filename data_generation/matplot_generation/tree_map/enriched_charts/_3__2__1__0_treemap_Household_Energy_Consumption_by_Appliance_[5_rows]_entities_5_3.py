
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data: Mentions of various scientific disciplines in different cities
data = {
    "City": ["New York", "New York", "New York", "New York", "New York", 
             "San Francisco", "San Francisco", "San Francisco", "San Francisco", "San Francisco",
             "Seattle", "Seattle", "Seattle", "Seattle", "Seattle", 
             "Austin", "Austin", "Austin", "Austin", "Austin", 
             "Boston", "Boston", "Boston", "Boston", "Boston", 
             "Chicago", "Chicago", "Chicago", "Chicago", "Chicago", 
             "Miami", "Miami", "Miami", "Miami", "Miami", 
             "Los Angeles", "Los Angeles", "Los Angeles", "Los Angeles", "Los Angeles"],
    "Category": ["Astronomy", "Biology", "Chemistry", "Physics", "Geology", 
                 "Astronomy", "Biology", "Chemistry", "Physics", "Geology", 
                 "Astronomy", "Biology", "Chemistry", "Physics", "Geology", 
                 "Astronomy", "Biology", "Chemistry", "Physics", "Geology", 
                 "Astronomy", "Biology", "Chemistry", "Physics", "Geology", 
                 "Astronomy", "Biology", "Chemistry", "Physics", "Geology", 
                 "Astronomy", "Biology", "Chemistry", "Physics", "Geology", 
                 "Astronomy", "Biology", "Chemistry", "Physics", "Geology"],
    "Number of Mentions": [350, 270, 180, 220, 160, 
                           320, 290, 200, 250, 180, 
                           300, 260, 190, 230, 170, 
                           310, 240, 210, 200, 190, 
                           280, 250, 220, 210, 180, 
                           290, 240, 230, 220, 200, 
                           260, 230, 210, 200, 170, 
                           300, 270, 240, 230, 210]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group data by Category
grouped_data = df.groupby("Category").sum().reset_index()

# Define color list
colors = ["#FF5733", "#C70039", "#900C3F", "#581845", "#FFC300", "#FF5733", "#C70039", "#900C3F", 
          "#581845", "#FFC300", "#FF5733", "#C70039", "#900C3F", "#581845", "#FFC300", "#FF5733", 
          "#C70039", "#900C3F", "#581845", "#FFC300", "#FF5733", "#C70039", "#900C3F", "#581845", 
          "#FFC300"]

# Plot
plt.figure(figsize=(20, 15))
squarify.plot(sizes=grouped_data['Number of Mentions'], label=grouped_data['Category'], alpha=0.8, color=colors)
plt.title('Mentions of Scientific Disciplines in Major Cities', fontsize=20, pad=40)
plt.axis('off')
plt.show()