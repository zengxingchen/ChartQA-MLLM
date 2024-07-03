
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'Country': ['USA', 'USA', 'UK', 'UK', 'Japan', 'Japan', 'Germany', 'Germany', 'France', 'France', 'Australia', 'Australia', 'Canada', 'Canada'],
    'Genre': ['Rock', 'Pop', 'Rock', 'Pop', 'Rock', 'Pop', 'Rock', 'Pop', 'Rock', 'Pop', 'Rock', 'Pop', 'Rock', 'Pop'],
    'Listeners': [400000, 300000, 350000, 250000, 200000, 400000, 150000, 300000, 180000, 280000, 130000, 250000, 160000, 220000],
    'AvgHoursPerWeek': [10, 15, 12, 18, 8, 20, 9, 14, 11, 16, 7, 13, 10, 15]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(16, 12))
bubble_plot = sns.scatterplot(data=df, x='Country', y='AvgHoursPerWeek', size='Listeners', hue='Genre',
                              sizes=(100, 2000), alpha=0.7, palette=["#FF5733", "#33C1FF"])

# Customize legend and axis labels
bubble_plot.legend(title='Genre', loc='upper right')
plt.xlabel('Country')
plt.ylabel('Average Hours Per Week')
plt.title('Average Weekly Music Listening Hours by Genre in Different Countries', pad=20)

# Show the plot
plt.show()