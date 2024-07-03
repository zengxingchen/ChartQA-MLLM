
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
age_data = {
    "age": [
        24, 22, 23, 22, 25, 26, 24, 24, 27, 28, 29, 23, 24, 25, 26,
        # ... (continue writing all the remaining data points) ...
        96, 97, 98, 99
    ]
}

# Create DataFrame
df = pd.DataFrame(data=age_data)

# Set the style and color palette
sns.set(style="whitegrid")
palette = ["#4772FF", "#FF6E47", "#47FFD4", "#FFD247", "#8E47FF"]

# Create the histogram chart
plt.figure(figsize=(14, 8))
sns.histplot(df['age'], kde=False, color="#3498db", bins=30, binwidth=1, orientation='horizontal')

# Additional styling options
plt.title('Age Distribution Among Participants')
plt.xlabel('Frequency')
plt.ylabel('Age')
plt.xlim(0, None)

# Save or show the figure
plt.savefig('age_distribution.png')
plt.show()