
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the dataframe from the provided data points
data = {
    'Beats_Per_Minute': [
        60, 65, 70, 70, 75, 75, 75, 80, 80, 80, 80, 85, 85, 85,
        85, 85, 90, 90, 90, 90, 90, 90, 95, 95, 95, 95, 95, 95,
        95, 100, 100, 100, 100, 100, 105, 105, 105, 105, 110,
        110, 110, 115, 115, 120
    ]
}
df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(8, 10))

# Plot a vertical histogram with a modified color scheme and adjusted band width
sns.histplot(data=df, x='Beats_Per_Minute', binwidth=5, color='#e74c3c')

# Customize the appearance of the plot
plt.title('Distribution of Beats Per Minute in Music Tracks')
plt.ylabel('Frequency')
plt.xlabel('Beats Per Minute (BPM)')

# Show the plot
plt.show()