
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data = {
    "Average_Weekly_Exercise_Hours": [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set style
sns.set_style('whitegrid')

# Increase the figure size and adjust histogram width (bin width)
plt.figure(figsize=(12, 8))
sns.histplot(df['Average_Weekly_Exercise_Hours'], color="#e74c3c", binwidth=1)

# Tweak the title and labels
plt.title('Distribution of Average Weekly Exercise Hours', fontsize=16)
plt.xlabel('Exercise Hours', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Visualize the plot
plt.show()