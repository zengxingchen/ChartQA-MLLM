
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example data points for demonstration
# In the actual code, this will consist of all 1,000 data points
data = {
    'Age': [
        21, 22, 19, 19, 20, 21, 20, 23, 24, 22,
        21, 21, 22, 23, 24, 25, 23, 22, 22, 21,
        20, 19, 18, 17, 22, 21, 25, 26, 24, 23,
        30, 28, 27, 29, 28, 27, 26, 24, 25, 26,
        # ... (up to 1,000 data points with individual ages)
    ]
}

# Creating a DataFrame from the data
df = pd.DataFrame(data)

# Set the size of the figure
plt.figure(figsize=(12, 6))

# Plot a horizontal histogram with specific colors and modify the band width
sns.histplot(data=df, x='Age', color='#007ACC', binwidth=1, kde=True, orientation='horizontal')

# Further customization of the plot
plt.title('Age Distribution in a Sample Population')
plt.xlabel('Frequency')
plt.ylabel('Age')
plt.grid(True)

# Show the plot
plt.show()