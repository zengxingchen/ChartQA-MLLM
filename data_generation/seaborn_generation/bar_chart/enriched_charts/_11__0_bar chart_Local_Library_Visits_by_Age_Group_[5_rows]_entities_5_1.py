
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Country': [
        'United States', 'Germany', 'France', 'Italy', 'United Kingdom',
        'Canada', 'Japan', 'South Korea', 'China', 'India',
        'Mexico', 'Brazil', 'Russia', 'Australia', 'Netherlands',
        'Spain', 'Switzerland', 'Belgium', 'Hong Kong', 'Singapore'
    ],
    'Calorie Intake': [
        3750, 3550, 3450, 3200, 3100,
        3050, 2800, 2700, 2600, 2400,
        2300, 2250, 2200, 2150, 2100,
        2050, 2000, 1950, 1900, 1850
    ]
}
df = pd.DataFrame(data)

# Set the figure size and style
sns.set(style="whitegrid")
plt.figure(figsize=(14, 8))

# Create a vertical bar plot with custom color scheme and bar width
barplot = sns.barplot(
    x="Country",
    y="Calorie Intake",
    data=df,
    palette=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1',
        '#A133FF', '#FF8333', '#33A1FF', '#A1FF33', '#FF3388',
        '#88FF33', '#3388FF', '#FF8833', '#33FF88', '#8833FF',
        '#FF3388', '#33A1FF', '#FF5733', '#3357FF', '#FF33A1'
    ],
    ci=None
)

# Customize the appearance
barplot.set_title('Average Daily Calorie Intake by Country (2021)', fontsize=16, weight='bold', pad=20)
barplot.bar_label(barplot.containers[0], fmt='%.0f')
barplot.set(xlabel="Country", ylabel="Calorie Intake (kcal)")

# Adjust the bar width
for bar in barplot.containers[0]:
    bar.set_width(0.6)

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()