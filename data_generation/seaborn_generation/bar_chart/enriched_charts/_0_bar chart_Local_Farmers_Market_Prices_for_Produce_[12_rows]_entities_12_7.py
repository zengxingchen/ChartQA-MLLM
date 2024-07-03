
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data = {
    'Category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'],
    'Value': [23, 45, 56, 78, 34, 65, 49, 68, 91, 54, 80, 61, 88, 74, 52]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 8))
sns.barplot(x='Value', y='Category', data=df, palette=["#FF5733", "#33FF57", "#3357FF", "#F033FF", "#33FFF3", "#FFC733", "#FF3333", "#3FFF33", "#FF33FF", "#335FFF", "#33FFC7", "#FFF333", "#FF3399", "#C7FF33", "#5733FF"], linewidth=1.5)

# Customize the chart
plt.title('Category vs. Value Distribution')
plt.xlabel('Value')
plt.ylabel('Category')
plt.grid(axis='x')

# Show the plot
plt.show()