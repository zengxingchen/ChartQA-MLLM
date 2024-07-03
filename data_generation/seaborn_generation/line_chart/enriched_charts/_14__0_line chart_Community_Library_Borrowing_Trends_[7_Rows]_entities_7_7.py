
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame from provided data
data = {
    'Year': list(range(2000, 2022)),
    'Mental Health Index': [60, 62, 65, 64, 66, 68, 70, 72, 71, 69, 70, 72, 73, 74, 76, 75, 77, 78, 80, 81, 78, 82]
}

df = pd.DataFrame(data)

# Settings for colors and figure size
line_colors = ["#1f77b4"]
plt.figure(figsize=(14, 7))

# Plot the line chart with seaborn
ax = sns.lineplot(x='Year', y='Mental Health Index', data=df, color=line_colors[0])

# Add a title and labels
ax.set_title('Annual Mental Health Index from 2000 to 2021')
ax.set_xlabel('Year')
ax.set_ylabel('Mental Health Index')

# Annotate significant data points
ax.annotate('Financial Crisis', xy=(2009, 69), xytext=(2009, 73),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Pandemic Impact', xy=(2020, 78), xytext=(2020, 82),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

ax.annotate('Recovery', xy=(2021, 82), xytext=(2021, 84),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            ha='center')

# Show the plot
plt.show()