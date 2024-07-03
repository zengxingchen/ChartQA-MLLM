
import matplotlib.pyplot as plt
import pandas as pd

# Provided data
data = [
    {'Week': '2023-01-W1', 'Yoga': 40, 'Pilates': 30, 'Zumba': 25, 'Cycling': 35},
    {'Week': '2023-01-W2', 'Yoga': 42, 'Pilates': 28, 'Zumba': 32, 'Cycling': 45},
    {'Week': '2023-01-W3', 'Yoga': 45, 'Pilates': 26, 'Zumba': 30, 'Cycling': 40},
    {'Week': '2023-01-W4', 'Yoga': 50, 'Pilates': 25, 'Zumba': 35, 'Cycling': 42},
    {'Week': '2023-02-W1', 'Yoga': 55, 'Pilates': 30, 'Zumba': 38, 'Cycling': 48},
    {'Week': '2023-02-W2', 'Yoga': 60, 'Pilates': 32, 'Zumba': 37, 'Cycling': 50},
    {'Week': '2023-02-W3', 'Yoga': 58, 'Pilates': 34, 'Zumba': 39, 'Cycling': 53},
    {'Week': '2023-02-W4', 'Yoga': 62, 'Pilates': 36, 'Zumba': 40, 'Cycling': 55},
    {'Week': '2023-03-W1', 'Yoga': 65, 'Pilates': 38, 'Zumba': 42, 'Cycling': 60},
    {'Week': '2023-03-W2', 'Yoga': 70, 'Pilates': 35, 'Zumba': 44, 'Cycling': 65},
    {'Week': '2023-03-W3', 'Yoga': 80, 'Pilates': 37, 'Zumba': 45, 'Cycling': 62},
    {'Week': '2023-03-W4', 'Yoga': 75, 'Pilates': 39, 'Zumba': 50, 'Cycling': 70}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Set the 'Week' column as the index
df.set_index('Week', inplace=True)

# Plotting the line chart with visual encodings using Matplotlib
plt.figure(figsize=(12, 8))

# Yoga: solid line, circular markers, blue color
plt.plot(df.index, df['Yoga'], label='Yoga', linestyle='-', marker='o', color='blue')

# Pilates: dashed line, triangular markers, red color
plt.plot(df.index, df['Pilates'], label='Pilates', linestyle='--', marker='^', color='red')

# Zumba: dash-dot line, square markers, green color
plt.plot(df.index, df['Zumba'], label='Zumba', linestyle='-.', marker='s', color='green')

# Cycling: dotted line, diamond markers, purple color
plt.plot(df.index, df['Cycling'], label='Cycling', linestyle=':', marker='d', color='purple')

# Add additional visual elements to the plot
plt.xlabel('Week')
plt.ylabel('Attendance')
plt.title('Weekly Class Attendance')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
plt.legend()  # Show the legend

# Show grid
plt.grid(True)

# Adjust layout to prevent clipping of ylabel/legend
plt.tight_layout()

# Display the plot
plt.show()