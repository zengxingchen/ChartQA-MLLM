
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the dataframe from the provided data points
data = {
    'Minutes': [
        30, 35, 35, 40, 40, 45, 45, 45, 50, 50, 50, 50, 55, 55, 55, 55, 55,
        60, 60, 60, 60, 60, 60, 65, 65, 65, 65, 65, 65, 65, 70, 70, 70, 70,
        70, 75, 75, 75, 75, 80, 80, 80, 85, 85, 90
    ]
}
df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(8, 12))

# Plot a vertical histogram with a modified color scheme and adjusted band width
sns.histplot(data=df, x='Minutes', binwidth=5, color='#e74c3c')

# Customize the appearance of the plot
plt.title('Distribution of Daily Workout Duration', pad=20)
plt.xlabel('Minutes')
plt.ylabel('Frequency')

# Show the plot
plt.show()