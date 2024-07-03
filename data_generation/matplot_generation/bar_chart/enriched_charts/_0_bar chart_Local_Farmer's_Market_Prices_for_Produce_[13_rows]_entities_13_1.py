
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Age Group": ["16-24", "25-34", "35-44", "45-54", "55-64", "65+"],
    "Facebook": [2.5, 2.1, 1.9, 1.5, 1.0, 0.8],
    "Twitter": [0.9, 0.8, 0.7, 0.6, 0.5, 0.4],
    "Instagram": [3.2, 2.8, 2.3, 1.9, 1.5, 1.2],
    "LinkedIn": [0.2, 0.3, 0.5, 0.8, 1.0, 1.3]
}

df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15  # width of the bars

# Position of bars on x-axis
indices = df.index
r1 = range(len(indices))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

# Make the plot
ax.barh(r1, df['Facebook'], color='#1B9E77', edgecolor='white', height=bar_width, label='Facebook')
ax.barh(r2, df['Twitter'], color='#D95F02', edgecolor='white', height=bar_width, label='Twitter')
ax.barh(r3, df['Instagram'], color='#7570B3', edgecolor='white', height=bar_width, label='Instagram')
ax.barh(r4, df['LinkedIn'], color='#E7298A', edgecolor='white', height=bar_width, label='LinkedIn')

# Add labels
ax.set_xlabel('Average Daily Hours', fontsize=15)
ax.set_ylabel('Age Group', fontsize=15)
ax.set_title('Average Daily Hours Spent on Social Media Platforms by Age Group', fontsize=18)

# Add xticks on the middle of the group bars
ax.set_yticks([r + bar_width for r in range(len(r1))])
ax.set_yticklabels(df['Age Group'])
ax.invert_yaxis()  # labels read top-to-bottom

# Create legend & Show graphic
ax.legend()
plt.tight_layout()
plt.show()