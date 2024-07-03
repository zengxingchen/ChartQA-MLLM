
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the given table data
data = {
    'StudentID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    'Daily Hours Studied': [1.5, 0.5, 2.0, 3.5, 4.0, 1.2, 2.5, 3.8, 0.8, 4.5, 2.8, 3.0, 3.3, 1.8, 0.3, 1.0, 3.2, 4.8, 2.3, 0.7, 1.7, 2.7, 3.1, 4.1, 1.1, 2.6, 3.9, 0.9, 4.6, 3.4, 1.9, 0.4, 1.6, 2.9, 4.7, 2.2, 3.7, 1.4, 2.1, 3.6],
    'Test Score': [65, 45, 75, 90, 92, 58, 80, 88, 50, 95, 82, 85, 87, 70, 40, 60, 86, 98, 78, 48, 62, 79, 84, 93, 57, 81, 89, 51, 96, 88, 71, 44, 63, 83, 97, 77, 87, 66, 76, 91]
}
df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(14, 10))

# Plot the relationship between Daily Hours Studied and Test Score with a custom color scheme
scatter = sns.scatterplot(
    x='Daily Hours Studied',
    y='Test Score',
    data=df,
    palette=['#4CAF50', '#FF9800', '#2196F3', '#9C27B0'],
    s=100 # Set the size of markers
)

# Customize the chart with a new headline and format
scatter.set_title('Correlation Between Daily Study Hours and Test Scores', fontsize=20, pad=20)
scatter.set_xlabel('Daily Hours Studied', fontsize=16)
scatter.set_ylabel('Test Score', fontsize=16)

# Show the chart
plt.show()