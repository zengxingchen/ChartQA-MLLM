
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data inspired by average life expectancy in different countries
data = {
    'Country': ['Japan', 'Switzerland', 'Spain', 'Italy', 'Australia', 'Sweden', 
                'Canada', 'Norway', 'Netherlands', 'France', 'Germany', 'United States'],
    'Life_Expectancy_Years': [84.5, 83.4, 83.3, 83.2, 82.9, 82.8, 82.2, 82.1, 81.8, 81.7, 81.2, 78.9]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort data by life expectancy for better visualization
df = df.sort_values('Life_Expectancy_Years')

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 6))

# Plot the data; switching to a vertical bar chart
sns.barplot(
    x="Country", 
    y="Life_Expectancy_Years", 
    data=df,
    palette=['#FF6347', '#FFA07A', '#FFD700', '#ADFF2F', '#7FFF00', '#32CD32', 
             '#20B2AA', '#1E90FF', '#0000FF', '#8A2BE2', '#FF69B4', '#C71585'],
    edgecolor=".2",
    linewidth=1.5
)

# Set the bar width; in the case of 'bar', the bar width is controlled by 'width'
sns.set_context("poster", font_scale=0.8)
ax.bar_label(ax.containers[0], label_type='edge')

# Change the axes to set a more suitable limit and labels
ax.set_ylim(75, 90)
ax.set_ylabel('Life Expectancy (Years)')
ax.set_xlabel('Country')
ax.set_title('Average Life Expectancy in Different Countries')

# Show the plot
plt.tight_layout()
plt.show()