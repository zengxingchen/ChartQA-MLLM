
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Week': 'Week 1', 'Coffee Sales (Units)': 350, 'Tea Sales (Units)': 180, 'Smoothie Sales (Units)': 70},
    {'Week': 'Week 2', 'Coffee Sales (Units)': 420, 'Tea Sales (Units)': 190, 'Smoothie Sales (Units)': 85},
    {'Week': 'Week 3', 'Coffee Sales (Units)': 390, 'Tea Sales (Units)': 200, 'Smoothie Sales (Units)': 80},
    {'Week': 'Week 4', 'Coffee Sales (Units)': 450, 'Tea Sales (Units)': 210, 'Smoothie Sales (Units)': 90},
    {'Week': 'Week 5', 'Coffee Sales (Units)': 470, 'Tea Sales (Units)': 230, 'Smoothie Sales (Units)': 95},
    {'Week': 'Week 6', 'Coffee Sales (Units)': 480, 'Tea Sales (Units)': 220, 'Smoothie Sales (Units)': 100},
    {'Week': 'Week 7', 'Coffee Sales (Units)': 500, 'Tea Sales (Units)': 240, 'Smoothie Sales (Units)': 110},
    {'Week': 'Week 8', 'Coffee Sales (Units)': 520, 'Tea Sales (Units)': 245, 'Smoothie Sales (Units)': 115},
    {'Week': 'Week 9', 'Coffee Sales (Units)': 530, 'Tea Sales (Units)': 250, 'Smoothie Sales (Units)': 120},
    {'Week': 'Week 10', 'Coffee Sales (Units)': 540, 'Tea Sales (Units)': 260, 'Smoothie Sales (Units)': 130},
    {'Week': 'Week 11', 'Coffee Sales (Units)': 560, 'Tea Sales (Units)': 270, 'Smoothie Sales (Units)': 140},
    {'Week': 'Week 12', 'Coffee Sales (Units)': 570, 'Tea Sales (Units)': 280, 'Smoothie Sales (Units)': 150}
]

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Creating a melted version of the DataFrame to work better with seaborn
df_melted = df.melt('Week', var_name='Product', value_name='Sales')

# Set up the aesthetics for the seaborn plot
sns.set_theme(style="whitegrid")

# Create the lineplot with diversified visual encoding
plt.figure(figsize=(10, 6))
lineplot = sns.lineplot(
    data=df_melted,
    x='Week',
    y='Sales',
    hue='Product',
    style='Product',
    markers=True,
    dashes=False,
    palette='tab10',
    markersize=10
)

# Improving the aesthetics
plt.xticks(rotation=45)
plt.title("Product Sales Over 12 Weeks")
plt.xlabel("Week")
plt.ylabel("Sales (Units)")
lineplot.legend(title='Product Sales', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.tight_layout()
plt.show()