
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'StepsTaken': [5000, 7000, 8000, 7500, 6000, 7000, 9000, 8000, 9500, 10500, 11000, 11500, 12000, 13000, 14000, 12500, 13500, 14500, 15000, 15500, 16000, 14000, 15000, 16000, 15500, 14500, 15000, 15500, 16500, 17000, 17500]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 8))
area_chart = sns.lineplot(data=df, x='Date', y='StepsTaken', color='#FF5733')
area_chart.fill_between(df['Date'], df['StepsTaken'], color='#FFC300', alpha=0.5)

# Annotate the highest point
max_steps = df['StepsTaken'].max()
max_day = df['StepsTaken'].idxmax() + 1
plt.text(max_day, max_steps, 'Max Steps\nTaken', horizontalalignment='center', verticalalignment='bottom', color='#C70039')

# Set the title and labels
plt.title("Daily Steps Taken Over a Month", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Steps Taken")

# Display the plot
plt.show()