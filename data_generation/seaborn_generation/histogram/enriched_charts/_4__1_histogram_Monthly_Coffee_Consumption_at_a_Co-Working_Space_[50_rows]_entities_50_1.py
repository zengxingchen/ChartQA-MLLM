
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data (daily calories consumed over a month)
data = {
    "Calories": [
        2000, 2100, 1800, 1900, 2000, 1950, 2200, 2300, 2400, 2100, 2050, 2100, 2150, 2250, 
        2300, 2350, 2500, 2600, 2400, 2350, 2200, 2100, 2150, 2050, 1900, 1800, 1850, 1950, 
        2000, 2100
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 10))

# Create a horizontal histogram with specified bin width, color, and other properties
sns.histplot(df['Calories'], bins=14, color='#2ca02c', kde=False, binwidth=50, orientation='horizontal')

# Set title and labels for the plot
plt.title("Monthly Distribution of Daily Calorie Intake", pad=20)
plt.xlabel("Frequency")
plt.ylabel("Calories")

# Show the plot
plt.show()