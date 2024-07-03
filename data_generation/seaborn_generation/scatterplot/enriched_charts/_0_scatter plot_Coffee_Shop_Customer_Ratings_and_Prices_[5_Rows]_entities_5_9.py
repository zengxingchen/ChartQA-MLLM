
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data from the table provided above
data = {
    'Age': [10, 10, 10, 10, 12, 12, 12, 12, 14, 14, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18],
    'Internet_Usage': [5, 6, 4, 7, 10, 8, 9, 11, 14, 12, 13, 15, 18, 16, 19, 17, 20, 21, 22, 23],
    'Test_Score': [85, 87, 82, 90, 78, 80, 73, 75, 65, 70, 68, 62, 55, 60, 53, 58, 50, 48, 45, 43]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(12, 8))
scatter_plot = sns.scatterplot(x='Internet_Usage', y='Test_Score', hue='Age', palette=['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#9400D3'], data=df)

# Customizing the scatterplot
scatter_plot.set_title('Relationship Between Internet Usage and Test Scores by Age')
scatter_plot.set_xlabel('Average Weekly Internet Usage (hours)')
scatter_plot.set_ylabel('Average Test Score (out of 100)')

plt.legend(title='Age Group')
plt.show()