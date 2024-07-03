
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_hours = [30, 28, 35, 40, 45, 50, 55, 53, 48, 42, 37, 33]

colors = ['#1F77B4', '#AEC7E8', '#FF7F0E', '#FFBB78', '#2CA02C', '#98DF8A', '#D62728', '#FF9896', '#9467BD', '#C5B0D5', '#8C564B', '#C49C94']

plt.figure(figsize=(10, 8))
bar_height = 0.7
plt.barh(months, average_hours, color=colors, height=bar_height)

plt.title('Average Monthly Study Hours in a Year', pad=20)
plt.xlabel('Average Hours')
plt.ylabel('Month')

plt.xlim([0, max(average_hours) + 10])

plt.tight_layout()
plt.show()