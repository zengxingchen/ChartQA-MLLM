
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data from the table provided above
data = {
    'Age': [10, 10, 10, 10, 12, 12, 12, 12, 14, 14, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18, 20, 20, 20, 20],
    'Steps_Per_Day': [3000, 3200, 3100, 3300, 5000, 5200, 5100, 5300, 7000, 7200, 7100, 7300, 9000, 9200, 9100, 9300, 11000, 11200, 11100, 11300, 13000, 13200, 13100, 13300],
    'Wellbeing_Score': [6, 5, 7, 8, 9, 8, 7, 6, 5, 6, 4, 7, 3, 2, 4, 5, 1, 2, 3, 4, 3, 4, 5, 6]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(14, 10))
scatter_plot = sns.scatterplot(x='Steps_Per_Day', y='Wellbeing_Score', hue='Age', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF'], data=df)

# Customizing the scatterplot
scatter_plot.set_title('Impact of Daily Steps on Wellbeing by Age')
scatter_plot.set_xlabel('Average Daily Steps')
scatter_plot.set_ylabel('Wellbeing Score (out of 10)')

plt.legend(title='Age Group', loc='upper right')
plt.show()