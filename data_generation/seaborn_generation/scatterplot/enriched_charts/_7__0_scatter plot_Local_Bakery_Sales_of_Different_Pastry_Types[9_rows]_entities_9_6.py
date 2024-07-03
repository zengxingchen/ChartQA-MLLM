
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = """
Sport,Average_Training_Hours,Average_Resting_Heart_Rate
Running,10,60
Swimming,12,58
Cycling,9,62
Soccer,8,65
Basketball,7,66
Tennis,6,64
Weightlifting,5,68
Yoga,4,60
Pilates,4,61
CrossFit,8,64
Martial Arts,9,63
Boxing,10,61
Rowing,11,59
Hiking,6,62
Dance,7,65
Golf,3,70
Rugby,8,66
Baseball,5,67
Volleyball,6,65
Cricket,4,68
Gymnastics,9,60
Triathlon,12,58
Skiing,6,64
Snowboarding,5,65
Surfing,4,63
"""

# Load the dataset into a pandas DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data))

# Create the scatterplot with customized features
plt.figure(figsize=(16, 9))
scatter = sns.scatterplot(
    data=df, 
    x="Average_Training_Hours", 
    y="Average_Resting_Heart_Rate", 
    palette=["#4CAF50", "#FF9800"],
    edgecolor="w", s=100
)

# Customize the plot's title and labels
scatter.set_title('Sports & Fitness: Training Hours vs. Resting Heart Rate', fontsize=20, pad=20)
scatter.set_xlabel('Average Training Hours per Week', fontsize=16)
scatter.set_ylabel('Average Resting Heart Rate (BPM)', fontsize=16)

# Adjust font size for the ticks
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Remove the top and right spines for a cleaner look
sns.despine()

# Show the plot
plt.show()