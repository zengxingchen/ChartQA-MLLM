
import matplotlib.pyplot as plt

# Extracting data from the given table
participant_ids = [data['Participant ID'] for data in chart_table_data]
daily_steps = [data[' Daily Steps'] for data in chart_table_data]

# Creating the histogram
plt.figure(figsize=(10, 6))  # specifying the figure size

# Plotting the histogram with diversified visual encoding
n, bins, patches = plt.hist(daily_steps, bins=8, color='skyblue', edgecolor='black')

# Adding extra visualization enhancements
for i in range(len(patches)):
    patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))

# Adding titles and labels
plt.title('Histogram of Daily Steps by Participants', fontsize=15)
plt.xlabel('Daily Steps', fontsize=12)
plt.ylabel('Number of Participants', fontsize=12)

# Adding mean line
mean_steps = sum(daily_steps) / len(daily_steps)
plt.axvline(mean_steps, color='red', linestyle='dashed', linewidth=1)
plt.text(mean_steps + 500, max(n)/2, f'Mean: {mean_steps:.0f}', color='red')

# Adding individual data points on top of the histogram
for (participant_id, steps_taken) in zip(participant_ids, daily_steps):
    plt.text(steps_taken, 0.5, str(participant_id), color='blue', fontweight='bold')

# Show the plot
plt.show()