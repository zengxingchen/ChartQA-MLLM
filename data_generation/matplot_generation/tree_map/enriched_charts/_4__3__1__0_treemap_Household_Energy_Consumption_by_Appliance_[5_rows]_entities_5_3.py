
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "City": ["New York", "New York", "New York", "San Francisco", "San Francisco", "San Francisco",
             "Seattle", "Seattle", "Seattle", "Austin", "Austin", "Austin", 
             "Boston", "Boston", "Boston", "Chicago", "Chicago", "Chicago",
             "Miami", "Miami", "Miami", "Los Angeles", "Los Angeles", "Los Angeles",
             "New York", "San Francisco", "Seattle", "Austin", "Boston", "Chicago",
             "Miami", "Los Angeles", "New York", "San Francisco", "Seattle", 
             "Austin", "Boston", "Chicago", "Miami", "Los Angeles"],
    "Category": ["Startups", "Marketing", "Finance", "Startups", "Marketing", "Finance",
                 "Startups", "Marketing", "Finance", "Startups", "Marketing", "Finance",
                 "Startups", "Marketing", "Finance", "Startups", "Marketing", "Finance",
                 "Startups", "Marketing", "Finance", "Startups", "Marketing", "Finance",
                 "Consulting", "Consulting", "Consulting", "Consulting", "Consulting", "Consulting",
                 "Consulting", "Consulting", "E-Commerce", "E-Commerce", "E-Commerce", 
                 "E-Commerce", "E-Commerce", "E-Commerce", "E-Commerce", "E-Commerce"],
    "Number of Mentions": [320, 280, 150, 350, 290, 180, 200, 150, 120, 210, 170, 130,
                           190, 160, 110, 230, 190, 140, 180, 140, 100, 240, 200, 170,
                           180, 190, 140, 160, 150, 170, 130, 210, 300, 320, 250, 270,
                           260, 280, 230, 310]
}

df = pd.DataFrame(data)

grouped_data = df.groupby("Category").sum().reset_index()

colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#FF8C33", "#57FF33", "#33FF8C",
          "#A833FF", "#5733FF", "#FF33D4", "#D4FF33", "#33FFD4", "#A8FF33", "#FFA833",
          "#FF3384", "#3384FF", "#84FF33", "#33FF84", "#FFA857", "#57FFA8", "#A8FFA8",
          "#84A8FF", "#3384A8", "#A857FF"]

plt.figure(figsize=(18, 14))
squarify.plot(sizes=grouped_data['Number of Mentions'], label=grouped_data['Category'], alpha=0.8, color=colors)
plt.title('Business Activity Mentions in Major Cities', fontsize=20, pad=30)
plt.axis('off')
plt.show()