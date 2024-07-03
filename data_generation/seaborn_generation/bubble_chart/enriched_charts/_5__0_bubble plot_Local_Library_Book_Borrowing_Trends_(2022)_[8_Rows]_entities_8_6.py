
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the DataFrame from the data above
data = {
    'Sport': ['Running', 'Cycling', 'Swimming', 'Hiking', 'Yoga',
              'Weightlifting', 'Basketball', 'Tennis', 'Soccer', 'Boxing',
              'Rowing', 'Pilates', 'Dancing', 'Skiing', 'Jumping_Rope',
              'Kayaking', 'Rock_Climbing', 'Skateboarding'],
    'Calories_Burned': [500, 400, 600, 350, 200, 450, 550, 500, 600, 700,
                        650, 250, 300, 600, 700, 300, 600, 350],
    'Duration_Minutes': [30, 45, 40, 60, 60, 50, 30, 60, 45, 30,
                         40, 60, 60, 50, 20, 60, 45, 60],
    'Heart_Rate': [150, 130, 140, 120, 100, 160, 155, 145, 155, 170,
                   160, 110, 120, 140, 165, 120, 150, 130]
}

df = pd.DataFrame(data)

# Adjusting the figure size
plt.figure(figsize=(16, 10))

# Creating the bubble chart
sns.scatterplot(data=df, x="Calories_Burned", y="Duration_Minutes", size="Heart_Rate", sizes=(20, 500),
                hue="Heart_Rate", palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", 
                                           "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", 
                                           "#bcbd22", "#17becf"])

# Customizing the appearance
plt.title("Sports & Fitness: Calories Burned, Duration and Heart Rate", fontsize=18)
plt.xlabel("Calories Burned", fontsize=14)
plt.ylabel("Duration (Minutes)", fontsize=14)

# Adjusting legend to avoid covering data points
plt.legend(title="Heart Rate (BPM)", loc='upper right', bbox_to_anchor=(1.25, 1), fontsize=12)

# Showing the final result
plt.show()