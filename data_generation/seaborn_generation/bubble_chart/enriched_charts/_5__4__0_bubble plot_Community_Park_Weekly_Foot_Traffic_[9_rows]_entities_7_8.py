
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'Country': ['USA', 'USA', 'China', 'China', 'India', 'India', 'Germany', 'Germany', 'Brazil', 'Brazil', 'France', 'France'],
    'Category': ['Mathematics', 'Science', 'Mathematics', 'Science', 'Mathematics', 'Science', 'Mathematics', 'Science', 'Mathematics', 'Science', 'Mathematics', 'Science'],
    'NumberOfStudents': [120000, 110000, 140000, 130000, 125000, 115000, 90000, 85000, 95000, 88000, 105000, 98000],
    'AverageScore': [78, 85, 88, 82, 76, 79, 80, 83, 72, 75, 77, 81]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(18, 14))
bubble_plot = sns.scatterplot(data=df, x='Country', y='AverageScore', size='NumberOfStudents', hue='Category',
                              sizes=(100, 2000), alpha=0.7, palette=["#1f77b4", "#ff7f0e"])

# Customize legend and axis labels
bubble_plot.legend(title='Category', loc='upper left')
plt.xlabel('Country')
plt.ylabel('Average Score')
plt.title('Average Scores by Category in Different Countries', pad=20)

# Show the plot
plt.show()