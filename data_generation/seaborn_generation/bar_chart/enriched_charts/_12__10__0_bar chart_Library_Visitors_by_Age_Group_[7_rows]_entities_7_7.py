
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Country': ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam'],
    'Total Population (millions)': [1444, 1393, 331, 273, 225, 213, 211, 166, 146, 128, 126, 115, 111, 104, 98],
    'Urban Population (millions)': [1000, 900, 260, 160, 80, 170, 100, 60, 110, 100, 90, 20, 50, 40, 36]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Set the dimensions of the figure
plt.figure(figsize=(14, 8))

# Create the horizontal bar chart
bar_plot = sns.barplot(
    x='Total Population (millions)',
    y='Country',
    data=df,
    palette=['#FF6347', '#FF4500', '#FFD700', '#FF8C00', '#FFA07A', '#FF7F50', '#FFA500', '#FF6347', '#FF4500', '#FFD700', '#FF8C00', '#FFA07A', '#FF7F50', '#FFA500'],
    linewidth=0.9,
    edgecolor='black'
)

# Customize the bar heights
for bar in bar_plot.patches:
    bar.set_height(0.5)

# Set the labels and title
plt.xlabel('Total Population (millions)')
plt.ylabel('Country')
plt.title('Total Population vs Urban Population in Various Countries', pad=20)

# Show the plot
plt.show()