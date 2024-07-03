
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'Country': ['USA', 'USA', 'China', 'China', 'India', 'India', 'Germany', 'Germany', 'Brazil', 'Brazil', 'France', 'France', 'Japan', 'Japan', 'Australia', 'Australia'],
    'Category': ['MentalHealth', 'PhysicalHealth', 'MentalHealth', 'PhysicalHealth', 'MentalHealth', 'PhysicalHealth', 'MentalHealth', 'PhysicalHealth', 'MentalHealth', 'PhysicalHealth', 'MentalHealth', 'PhysicalHealth', 'MentalHealth', 'PhysicalHealth', 'MentalHealth', 'PhysicalHealth'],
    'NumberOfParticipants': [150000, 160000, 130000, 140000, 145000, 135000, 90000, 95000, 100000, 105000, 110000, 115000, 120000, 125000, 105000, 110000],
    'AverageScore': [75, 80, 85, 88, 78, 82, 83, 79, 76, 81, 77, 84, 86, 89, 82, 85]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(20, 16))
bubble_plot = sns.scatterplot(data=df, x='Country', y='AverageScore', size='NumberOfParticipants', hue='Category',
                              sizes=(100, 2000), alpha=0.7, palette=["#4c72b0", "#55a868"])

# Customize legend and axis labels
bubble_plot.legend(title='Category', loc='upper right')
plt.xlabel('Country')
plt.ylabel('Average Score')
plt.title('Average Scores by Category in Health & Psychology Across Countries', pad=30)

# Show the plot
plt.show()