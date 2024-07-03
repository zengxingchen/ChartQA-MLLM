
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'RevenueGenerated': [100, 150, 120, 180, 160, 140, 200, 220, 210, 230, 190, 250, 240, 270, 260, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 8))
area_chart = sns.lineplot(data=df, x='Date', y='RevenueGenerated', color='#2ca02c')
area_chart.fill_between(df['Date'], df['RevenueGenerated'], color='#98df8a', alpha=0.5)

# Annotate the highest point
max_revenue = df['RevenueGenerated'].max()
max_day = df['RevenueGenerated'].idxmax() + 1
plt.text(max_day, max_revenue, 'Max Revenue\nGenerated', horizontalalignment='center', verticalalignment='bottom', color='#d62728')

# Set the title and labels
plt.title("Daily Revenue Generated Over a Month", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Revenue Generated (in $)")

# Display the plot
plt.show()