
import matplotlib.pyplot as plt
import pandas as pd

# Provided data
data = [
    {'Week': '2023-03-W1', 'Fruits': 500, 'Vegetables': 600, 'Herbs': 150, 'Bakery': 400, 'Dairy': 350, 'Meats': 300},
    {'Week': '2023-03-W2', 'Fruits': 550, 'Vegetables': 610, 'Herbs': 160, 'Bakery': 420, 'Dairy': 365, 'Meats': 320},
    {'Week': '2023-03-W3', 'Fruits': 600, 'Vegetables': 620, 'Herbs': 170, 'Bakery': 450, 'Dairy': 380, 'Meats': 340},
    {'Week': '2023-03-W4', 'Fruits': 640, 'Vegetables': 630, 'Herbs': 180, 'Bakery': 480, 'Dairy': 390, 'Meats': 360},
    {'Week': '2023-04-W1', 'Fruits': 680, 'Vegetables': 650, 'Herbs': 190, 'Bakery': 500, 'Dairy': 400, 'Meats': 380},
    {'Week': '2023-04-W2', 'Fruits': 720, 'Vegetables': 670, 'Herbs': 200, 'Bakery': 530, 'Dairy': 420, 'Meats': 400},
    {'Week': '2023-04-W3', 'Fruits': 760, 'Vegetables': 690, 'Herbs': 210, 'Bakery': 550, 'Dairy': 430, 'Meats': 420},
    {'Week': '2023-04-W4', 'Fruits': 800, 'Vegetables': 710, 'Herbs': 220, 'Bakery': 570, 'Dairy': 450, 'Meats': 440},
    {'Week': '2023-05-W1', 'Fruits': 850, 'Vegetables': 730, 'Herbs': 230, 'Bakery': 590, 'Dairy': 470, 'Meats': 460},
    {'Week': '2023-05-W2', 'Fruits': 900, 'Vegetables': 750, 'Herbs': 240, 'Bakery': 610, 'Dairy': 480, 'Meats': 480},
    {'Week': '2023-05-W3', 'Fruits': 950, 'Vegetables': 770, 'Herbs': 250, 'Bakery': 630, 'Dairy': 490, 'Meats': 500},
    {'Week': '2023-05-W4', 'Fruits': 1000, 'Vegetables': 800, 'Herbs': 260, 'Bakery': 650, 'Dairy': 500, 'Meats': 520}
]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Setting Week as index
df.set_index('Week', inplace=True)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Columns to plot
columns = df.columns.tolist()

# Colors for each column
colors = ["#FF9999", "#FFCC99", "#FFFF99", "#CCFF99", "#99FF99", "#99FFCC"]

# Plot stacked area chart
df.plot(kind='area',
        stacked=True,
        ax=ax,
        color=colors)

# Adding title and labels
plt.title('Sales Data by Product Category Over Time')
plt.xlabel('Week')
plt.ylabel('Units Sold')

# Adding legend
plt.legend(loc='upper left')

# Adding grid
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Adding vertical line delimiters between months
for i in range(1, len(df.index), 4):
    plt.axvline(i + 0.5, color='grey', linestyle='--', linewidth=1.0)

# Rotate the x-ticks to show the weeks more clearly
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()