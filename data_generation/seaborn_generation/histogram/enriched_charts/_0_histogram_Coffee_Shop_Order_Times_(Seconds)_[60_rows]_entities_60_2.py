
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Constructing dataframe from given data
data = {
    'value': [
        12.4, 13.2, 15.4, 14.7, 18.5, 20.1, 21.5, 21.7, 22.3, 23.5,
        25.4, 26.8, 28.2, 29.6, 30.1, 31.7, 33.5, 34.2, 35.8, 36.4,
        37.2, 39.5, 40.1, 41.7, 42.3, 44.5, 45.2, 45.8, 47.3, 48.5,
        49.1, 50.7, 52.4, 53.6, 54.2, 56.5, 57.1, 58.3, 59.5, 61.2,
        62.8, 64.4, 65.1, 66.5, 68.2, 69.5, 70.7, 72.3, 73.4, 74.2,
        74.6, 75.1, 76.5, 78.2, 79.6, 81.2, 82.5, 83.7, 84.4, 85.2,
        86.5, 87.3, 88.1, 89.7, 91.2, 92.8, 94.4, 95.6, 97.1, 98.3,
        99.5, 100.2, 101.7, 103.5, 105.2, 106.8, 108.4, 109.7, 111.3,
        112.8, 114.5
    ]
}

df = pd.DataFrame(data)

# Set the style of seaborn
sns.set(style="whitegrid")

# Enlarging the plot
plt.figure(figsize=(10, 6))

# Creating the histogram with modifications
sns.histplot(data=df, x='value', color="#3498db", binwidth=2.0, kde=False, orientation='horizontal')

# Additional modifications: set the title and labels
plt.title('Frequency Distribution of Measurement Values')
plt.xlabel('Frequency')
plt.ylabel('Value (units)')

# Show the plot
plt.show()