
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Your data as a list of dictionaries
data = [
    {'Year': 2019, 'Adults Attendance (thousands)': 12, 'Children Attendance (thousands)': 9, 'Total Books Loaned (thousands)': 40, 'Library Events Attendance': 2.0},
    {'Year': 2020, 'Adults Attendance (thousands)': 7, 'Children Attendance (thousands)': 5, 'Total Books Loaned (thousands)': 28, 'Library Events Attendance': 1.0},
    {'Year': 2021, 'Adults Attendance (thousands)': 8, 'Children Attendance (thousands)': 6, 'Total Books Loaned (thousands)': 33, 'Library Events Attendance': 1.5},
    {'Year': 2022, 'Adults Attendance (thousands)': 10, 'Children Attendance (thousands)': 7, 'Total Books Loaned (thousands)': 38, 'Library Events Attendance': 3.0},
    {'Year': 2023, 'Adults Attendance (thousands)': 11, 'Children Attendance (thousands)': 8, 'Total Books Loaned (thousands)': 42, 'Library Events Attendance': 2.5}
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# We will use 'Year' for the x-axis, so it needs to be of type string to plot properly
df['Year'] = df['Year'].astype(str)

# Create a bubble chart
plt.figure(figsize=(10,8))
bubble_plot = sns.scatterplot(
    data=df,
    x='Year', 
    y='Total Books Loaned (thousands)',
    size='Library Events Attendance', 
    sizes=(20, 1000),  # Control the range of bubble sizes
    hue='Adults Attendance (thousands)',  # Color bubbles based on adults attendance
    style='Children Attendance (thousands)',  # Different markers for children attendance
    palette='viridis',  # Color palette for 'hue'
    legend='full'
)

# Adjust the legend for bubble sizes
h, labs = bubble_plot.get_legend_handles_labels()
bubble_plot.legend(h[0:5] + h[6:], labs[0:5] + labs[6:], title='Legends')

# Additional customizations
plt.title('Library Data Visualization (Bubble chart)')
plt.xlabel('Year')
plt.ylabel('Total Books Loaned (thousands)')
plt.grid(True)
plt.show()