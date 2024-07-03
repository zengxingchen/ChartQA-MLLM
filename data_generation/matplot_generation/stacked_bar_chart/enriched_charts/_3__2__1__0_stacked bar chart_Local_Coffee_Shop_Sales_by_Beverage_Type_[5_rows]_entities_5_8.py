
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
math_scores = [12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000]
science_scores = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000]
history_scores = [9000, 9500, 10000, 11000, 12000, 12500, 13000, 14000, 15000, 16000]
art_scores = [7000, 8000, 8500, 9000, 9500, 10000, 11000, 12000, 13000, 14000]

# Plot
fig, ax = plt.subplots(figsize=(12, 8))  # Change the figure size

bar_width = 0.35  # Change the bar width for a vertical bar chart

bar_math = ax.bar(years, math_scores, width=bar_width, color='#1f77b4', label='Math')
bar_science = ax.bar(years, science_scores, width=bar_width, bottom=math_scores, color='#ff7f0e', label='Science')
bar_history = ax.bar(years, history_scores, width=bar_width, bottom=[i+j for i,j in zip(math_scores, science_scores)], color='#2ca02c', label='History')
bar_art = ax.bar(years, art_scores, width=bar_width, bottom=[i+j+k for i,j,k in zip(math_scores, science_scores, history_scores)], color='#d62728', label='Art')

# Add some text for labels, title, and custom y-axis tick labels, etc.
ax.set_ylabel('Total Scores')
ax.set_title('Annual Student Performance by Subject', pad=20)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

# Add numerical labels
for bars in [bar_math, bar_science, bar_history, bar_art]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Show the figure
plt.tight_layout()
plt.show()