
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = [
    {'Age Group': '16-20', 'Average Daily Smartphone Usage (hours)': 3.5, 'Average Daily Steps': 9000},
    {'Age Group': '21-25', 'Average Daily Smartphone Usage (hours)': 4.0, 'Average Daily Steps': 8500},
    {'Age Group': '26-30', 'Average Daily Smartphone Usage (hours)': 3.8, 'Average Daily Steps': 8000},
    {'Age Group': '31-35', 'Average Daily Smartphone Usage (hours)': 3.0, 'Average Daily Steps': 7500},
    {'Age Group': '36-40', 'Average Daily Smartphone Usage (hours)': 2.7, 'Average Daily Steps': 7000},
    {'Age Group': '41-45', 'Average Daily Smartphone Usage (hours)': 2.5, 'Average Daily Steps': 6500},
    {'Age Group': '46-50', 'Average Daily Smartphone Usage (hours)': 2.3, 'Average Daily Steps': 6000},
    {'Age Group': '51-55', 'Average Daily Smartphone Usage (hours)': 2.0, 'Average Daily Steps': 5500},
    {'Age Group': '56-60', 'Average Daily Smartphone Usage (hours)': 1.7, 'Average Daily Steps': 5000},
    {'Age Group': '61-65', 'Average Daily Smartphone Usage (hours)': 1.5, 'Average Daily Steps': 4700},
    {'Age Group': '66-70', 'Average Daily Smartphone Usage (hours)': 1.2, 'Average Daily Steps': 4400},
    {'Age Group': '71-75', 'Average Daily Smartphone Usage (hours)': 1.0, 'Average Daily Steps': 4200}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Create scatterplot with diversified visual encoding
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    data=df,
    x='Average Daily Smartphone Usage (hours)',
    y='Average Daily Steps',
    size='Average Daily Steps',  # Size by daily steps - this will give a different size marker for different step counts
    hue='Age Group',            # Color by age group
    style='Age Group',          # Different marker style for different age groups
    palette='viridis',          # Color palette
    sizes=(50, 300),            # Range of sizes for marker
    alpha=0.7                   # Transparency of markers
)

# Customizing the plot
scatter.set_title('Average Daily Smartphone Usage vs. Average Daily Steps by Age Group')
scatter.set_xlabel('Average Daily Smartphone Usage (hours)')
scatter.set_ylabel('Average Daily Steps')
plt.legend(title='Age Group', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()