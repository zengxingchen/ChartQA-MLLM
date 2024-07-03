
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = [
    {'Age Group': '0-12', 'Number of Visits (per month)': 450},
    {'Age Group': '13-18', 'Number of Visits (per month)': 350},
    {'Age Group': '19-30', 'Number of Visits (per month)': 470},
    {'Age Group': '31-50', 'Number of Visits (per month)': 390},
    {'Age Group': '51+', 'Number of Visits (per month)': 320}
]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Create a bar plot
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(
    x='Age Group', 
    y='Number of Visits (per month)', 
    data=df, 
    palette="viridis", # Diversified color palette
    edgecolor="black"  # Add edgecolor to the bars for better distinction
)

# Adding annotations to each bar
for p in bar_plot.patches:
    bar_plot.annotate(format(p.get_height(), '.1f'), 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha = 'center', 
                      va = 'center', 
                      xytext = (0, 9), 
                      textcoords = 'offset points')

# Customizing the axes and title
plt.title('Number of Visits per Month by Age Group', fontsize=15)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Number of Visits (per month)', fontsize=12)

# Show the plot with a tight layout
plt.tight_layout()

# Display the plot
plt.show()