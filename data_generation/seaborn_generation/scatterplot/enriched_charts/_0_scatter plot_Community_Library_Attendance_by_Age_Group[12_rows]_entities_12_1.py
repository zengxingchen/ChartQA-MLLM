
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the given table data
data = {
    'StudentID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'Daily Hours Studied': [1.5, 0.5, 2.0, 3.5, 4.0, 1.2, 2.5, 3.8, 0.8, 4.5, 2.8, 3.0, 3.3, 1.8, 0.3, 1.0, 3.2, 4.8, 2.3, 0.7],
    'Test Score': [65, 45, 75, 90, 92, 58, 80, 88, 50, 95, 82, 85, 87, 70, 40, 60, 86, 98, 78, 48]
}
df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(12, 8))

# Plot the relationship between Daily Hours Studied and Test Score
# with a custom color scheme
scatter = sns.scatterplot(
    x='Daily Hours Studied',
    y='Test Score',
    data=df,
    palette=['#FF5733', '#33FF57', '#3357FF', '#57FF33'],
    s=100 # Set the size of markers
)

# Customize the chart with a new headline and format
scatter.set_title('Relationship Between Daily Hours Studied and Test Score', fontsize=16)
scatter.set_xlabel('Daily Hours Studied', fontsize=14)
scatter.set_ylabel('Test Score', fontsize=14)

# Show the chart
plt.show()