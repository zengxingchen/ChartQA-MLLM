
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the DataFrame from the data above
data = {
    'Sport': ['Soccer', 'Basketball', 'Tennis', 'Cricket', 'Rugby', 'Golf', 'Swimming', 'Athletics', 
              'Cycling', 'Boxing', 'Wrestling', 'Volleyball', 'Baseball', 'Ice Hockey', 
              'Table Tennis', 'Badminton', 'Gymnastics', 'Rowing', 'Skiing', 'Skateboarding'],
    'Participants': [265, 450, 87, 125, 88, 82, 500, 100, 60, 70, 80, 200, 75, 85, 300, 150, 120, 50, 45, 60],
    'Events': [8000, 1500, 2000, 2500, 1800, 2200, 1200, 2100, 1500, 1300, 1100, 1700, 1400, 1600, 1100, 1000, 900, 600, 700, 800],
    'Popularity': [4500, 3000, 2500, 3200, 2700, 2800, 3100, 2900, 2600, 2300, 2200, 2400, 2500, 2700, 2100, 2000, 2200, 1800, 1900, 2000]
}

df = pd.DataFrame(data)

# Adjusting the figure size
plt.figure(figsize=(18, 12))

# Creating the bubble chart
sns.scatterplot(data=df, x="Participants", y="Events", size="Popularity", sizes=(100, 1000),
                hue="Popularity", palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
                                           "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"])

# Customizing the appearance
plt.title("Popularity of Sports: Participants, Events, and Popularity", fontsize=20, pad=20)
plt.xlabel("Number of Participants (in millions)", fontsize=16)
plt.ylabel("Number of Events", fontsize=16)

# Adjusting legend to avoid covering data points
plt.legend(title="Popularity (in millions)", loc='upper right', bbox_to_anchor=(1.15, 1), fontsize=14)

# Showing the final result
plt.show()