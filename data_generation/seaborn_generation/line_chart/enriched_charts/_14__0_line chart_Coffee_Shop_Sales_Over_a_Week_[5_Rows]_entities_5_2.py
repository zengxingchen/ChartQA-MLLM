
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Calories": [2200, 2000, 2100, 2300, 1900, 2500, 2400]
}

df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(12, 8)) # Changed width & height
sns.lineplot(x="Day", y="Calories", data=df, marker='o', color="#1E90FF") # Changed color

# Adding annotations
for i in range(df.shape[0]):
    plt.text(df.Day[i], df.Calories[i] + 50, f"{df.Calories[i]} kcal", horizontalalignment='center')

# Set the title
plt.title("Daily Caloric Intake Over One Week", pad=20)

plt.show()