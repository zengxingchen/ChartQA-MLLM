
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a data frame from the provided dataset
data = [
    {'Age Group': '0-12', 'Visitors': 350},
    {'Age Group': '13-18', 'Visitors': 240},
    {'Age Group': '19-25', 'Visitors': 310},
    {'Age Group': '26-35', 'Visitors': 460},
    {'Age Group': '36-50', 'Visitors': 518},
    {'Age Group': '51-65', 'Visitors': 289},
    {'Age Group': 'Over 65', 'Visitors': 195},
    # Exclude the 'Total' row for plotting the area chart
]

# Convert to DataFrame
df = pd.DataFrame(data)

# We'll create an ordered categorical type to ensure that the X-axis follows the correct order
age_order = ['0-12', '13-18', '19-25', '26-35', '36-50', '51-65', 'Over 65']
df['Age Group'] = pd.Categorical(df['Age Group'], categories=age_order, ordered=True)

# Plot the line and fill the area below it
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
plot = sns.lineplot(data=df, x='Age Group', y='Visitors', sort=False, marker="o")

# Filling the area below the line plot
x = plot.get_lines()[0].get_xdata()
y = plot.get_lines()[0].get_ydata()
plt.fill_between(x, y, color="skyblue", alpha=0.4)

# Enhance the plot further with labels and title
plt.title('Visitors by Age Group', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Number of Visitors', fontsize=12)

# Display the plot
plt.show()