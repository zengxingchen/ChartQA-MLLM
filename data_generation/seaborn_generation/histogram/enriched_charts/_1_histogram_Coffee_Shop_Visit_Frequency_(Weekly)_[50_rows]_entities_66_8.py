
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generating age data points
age_data = [0, 1, 1, 2, 3, 3, 3, 4, 4, 4, 4]  # This shows the pattern, imagine it continues
age_data += list(np.random.choice(range(5, 101), size=980, replace=True))  # Randomly fill remaining data

# Create the DataFrame
df = pd.DataFrame(age_data, columns=['Age'])

# Set the style
sns.set_style('whitegrid')

# Create the histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, color="#3498db", binwidth=5)

# Customize the plot with title and labels
plt.title('Population Age Distribution', fontsize=15)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Show the plot
plt.show()