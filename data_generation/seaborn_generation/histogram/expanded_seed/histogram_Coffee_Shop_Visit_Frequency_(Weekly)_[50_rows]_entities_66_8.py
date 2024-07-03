
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your provided table data
data = [
    {'Customer Age Group': '18-25', 'Visits per Week': 3},
    {'Customer Age Group': '26-35', 'Visits per Week': 5},
    {'Customer Age Group': '36-45', 'Visits per Week': 2},
    {'Customer Age Group': '46-55', 'Visits per Week': 1},
    {'Customer Age Group': '56-65', 'Visits per Week': 4},
    {'Customer Age Group': 'Over 65', 'Visits per Week': 2},
    {'Customer Age Group': '18-25', 'Visits per Week': 6},
    {'Customer Age Group': '26-35', 'Visits per Week': 3},
    {'Customer Age Group': '36-45', 'Visits per Week': 0},
    {'Customer Age Group': '46-55', 'Visits per Week': 2},
    {'Customer Age Group': '56-65', 'Visits per Week': 3},
    {'Customer Age Group': 'Over 65', 'Visits per Week': 1},
    {'Customer Age Group': '18-25', 'Visits per Week': 2},
    {'Customer Age Group': '26-35', 'Visits per Week': 4},
    {'Customer Age Group': '36-45', 'Visits per Week': 1}
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Initialize a matplotlib figure
plt.figure(figsize=(10, 6))

# Create a diversified histogram using Seaborn
# We will use "hue" for different age groups and a palette to diversify the colors.
sns.histplot(data=df, x='Visits per Week', hue='Customer Age Group', multiple='stack', bins=range(0, df['Visits per Week'].max()+2), palette='viridis', edgecolor='black')

# Adding more details to the plot
plt.title('Histogram of Customer Visits per Week by Age Group')
plt.xlabel('Visits per Week')
plt.ylabel('Count')
plt.legend(title='Customer Age Group')

# Show the plot
plt.show()