
import matplotlib.pyplot as plt

# Generate data points
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
sleep_durations = [7.5, 7.2, 7.0, 6.8, 7.1, 7.3, 7.6, 7.4, 7.2, 7.0, 6.9, 7.1]

plt.figure(figsize=(12, 10))  # Change the width and height of the chart

# Create a vertical bar chart with specified bar width and colors
plt.bar(months, sleep_durations, color=[
    '#4B8E4B', '#88C399', '#D1E0D1', '#FFDDC1', '#FFC3A0',
    '#FF9980', '#FF6666', '#FF4C4C', '#CC4C4C', '#B24C4C',
    '#804C4C', '#4C4C4C'], width=0.5)

plt.ylabel('Average Sleep Duration (hours)', fontsize=14)
plt.title('Average Monthly Sleep Duration in 2023', fontsize=16)
plt.ylim(0, 9)  # Adjusted to give some space for readability

plt.tight_layout()
plt.show()