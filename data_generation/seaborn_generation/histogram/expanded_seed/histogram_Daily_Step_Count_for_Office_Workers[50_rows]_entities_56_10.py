
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your data as a list of dictionaries
data = [{'Day': 'Monday', 'Steps': 3450}, {'Day': 'Tuesday', 'Steps': 7100}, {'Day': 'Wednesday', 'Steps': 6800},
        {'Day': 'Thursday', 'Steps': 3700}, {'Day': 'Friday', 'Steps': 4030}, {'Day': 'Saturday', 'Steps': 7960},
        {'Day': 'Sunday', 'Steps': 10200}, {'Day': 'Monday', 'Steps': 3210}, {'Day': 'Tuesday', 'Steps': 6890},
        {'Day': 'Wednesday', 'Steps': 6580}, {'Day': 'Thursday', 'Steps': 3500}, {'Day': 'Friday', 'Steps': 3880},
        {'Day': 'Saturday', 'Steps': 8100}, {'Day': 'Sunday', 'Steps': 9700}, {'Day': 'Monday', 'Steps': 3050}]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Create the histogram using Seaborn
plt.figure(figsize=(10, 6))  # Set the figure size
sns.histplot(df['Steps'], kde=True, bins=8, color='skyblue', edgecolor='black')

# Customizing the plot to make it more informative
plt.title('Steps Taken Histogram', fontsize=20)          # Title of the histogram
plt.xlabel('Steps', fontsize=15)                          # X-axis label
plt.ylabel('Frequency', fontsize=15)                      # Y-axis label
plt.xticks(rotation=45)                                   # Rotate x-axis labels
plt.grid(True, which='both', axis='y', linestyle='--')    # Add gridlines

# Show the plot
plt.show()