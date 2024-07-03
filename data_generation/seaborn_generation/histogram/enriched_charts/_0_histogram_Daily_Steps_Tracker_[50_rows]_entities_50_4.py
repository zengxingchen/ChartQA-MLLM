
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
data_values = [
    23, 34, 45, 56, 67, 78, 89, 100, 56, 67, 78, 89, 100, 111, 122,
    56, 67, 78, 89, 100, 111, 122, 133, 56, 67, 78, 89, 100, 111,
    122, 133, 144, 56, 67, 78, 89, 100, 111, 122, 133, 144, 155,
    56, 67, 78, 89, 100, 111, 122, 133, 144, 155, 166,
    56, 67, 78, 89, 100, 111, 122, 133, 144, 155, 166, 177,
    56, 67, 78, 89, 100, 111, 122, 133, 144, 155, 166, 177, 188,
    56, 67, 78, 89, 100, 111, 122, 133, 144, 155, 166, 177, 188, 199,
    56, 67, 78, 89, 100, 111, 122, 133, 144, 155, 166, 177, 188, 199, 210
]

# Create the dataframe
df = pd.DataFrame(data_values, columns=['Value'])

# Set up the matplotlib figure
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Plot a horizontal histogram with specified bin width and color
sns.histplot(df['Value'], color='#3498db', binwidth=5, kde=False, orientation='horizontal')

# Customize the plot with title, labels, and limits
plt.title('Distribution of Performance Scores')
plt.xlabel('Frequency')
plt.ylabel('Performance Score')

# Show the plot
plt.show()