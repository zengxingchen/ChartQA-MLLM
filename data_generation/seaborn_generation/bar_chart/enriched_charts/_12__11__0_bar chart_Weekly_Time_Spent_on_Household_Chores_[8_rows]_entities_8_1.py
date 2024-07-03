
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Exercise Type': ['Yoga', 'Pilates', 'Zumba', 'Swimming', 'Cycling', 'Running', 'Weightlifting', 'Boxing'],
    'AverageCaloriesBurnedPerHour': [240, 290, 370, 500, 600, 700, 300, 800]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 8))  # Width and height modification
sns.barplot(y="Exercise Type", x="AverageCaloriesBurnedPerHour", data=df,
            palette=['#ff6666', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4'])  # Color modification using specific color codes

# Set the height of bars
for bar in plt.gca().patches:
    bar.set_height(0.7)  # Height of bars when horizontal

plt.ylabel('Exercise Type')
plt.xlabel('Average Calories Burned Per Hour')
plt.title('Average Calories Burned Per Hour by Exercise Type', pad=20)
sns.despine(left=True, bottom=True)  # Cleaning up the plot
plt.show()