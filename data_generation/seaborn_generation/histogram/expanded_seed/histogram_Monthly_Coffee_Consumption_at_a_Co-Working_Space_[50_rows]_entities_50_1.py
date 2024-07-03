
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data provided
data = [
    {'Day': 'Day 1', 'Cups of Coffee': 132},
    {'Day': 'Day 2', 'Cups of Coffee': 128},
    {'Day': 'Day 3', 'Cups of Coffee': 115},
    {'Day': 'Day 4', 'Cups of Coffee': 143},
    {'Day': 'Day 5', 'Cups of Coffee': 150},
    {'Day': 'Day 6', 'Cups of Coffee': 108},
    {'Day': 'Day 7', 'Cups of Coffee': 165},
    {'Day': 'Day 8', 'Cups of Coffee': 122},
    {'Day': 'Day 9', 'Cups of Coffee': 137},
    {'Day': 'Day 10', 'Cups of Coffee': 145},
    {'Day': 'Day 11', 'Cups of Coffee': 119},
    {'Day': 'Day 12', 'Cups of Coffee': 121},
    {'Day': 'Day 13', 'Cups of Coffee': 133},
    {'Day': 'Day 14', 'Cups of Coffee': 140},
    {'Day': 'Day 15', 'Cups of Coffee': 155}
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Generate a histogram using seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Cups of Coffee', bins=8, kde=False, color='purple')

# Customize the plot with titles and labels
plt.title('Distribution of Cups of Coffee Consumed Per Day', fontsize=16)
plt.xlabel('Cups of Coffee', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(range(100, 170, 10))
plt.yticks(range(0, 5)) 
plt.grid(True)

# Show the plot
plt.show()