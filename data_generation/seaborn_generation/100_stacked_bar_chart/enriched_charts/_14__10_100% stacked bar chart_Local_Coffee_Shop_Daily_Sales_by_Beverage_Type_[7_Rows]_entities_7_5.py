
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = [
    {'Day': 'Monday', 'Carbs': '30%', 'Protein': '20%', 'Fats': '15%', 'Vegetables': '10%', 'Fruits': '15%', 'Dairy': '10%'},
    {'Day': 'Tuesday', 'Carbs': '25%', 'Protein': '25%', 'Fats': '20%', 'Vegetables': '8%', 'Fruits': '12%', 'Dairy': '10%'},
    {'Day': 'Wednesday', 'Carbs': '20%', 'Protein': '30%', 'Fats': '15%', 'Vegetables': '10%', 'Fruits': '15%', 'Dairy': '10%'},
    {'Day': 'Thursday', 'Carbs': '22%', 'Protein': '28%', 'Fats': '18%', 'Vegetables': '12%', 'Fruits': '10%', 'Dairy': '10%'},
    {'Day': 'Friday', 'Carbs': '25%', 'Protein': '20%', 'Fats': '20%', 'Vegetables': '15%', 'Fruits': '10%', 'Dairy': '10%'},
    {'Day': 'Saturday', 'Carbs': '28%', 'Protein': '18%', 'Fats': '15%', 'Vegetables': '12%', 'Fruits': '17%', 'Dairy': '10%'},
    {'Day': 'Sunday', 'Carbs': '30%', 'Protein': '20%', 'Fats': '15%', 'Vegetables': '10%', 'Fruits': '15%', 'Dairy': '10%'}
]

# Transform data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert percentage strings to numerical values
for col in df.columns:
    if col != 'Day':
        df[col] = df[col].str.rstrip('%').astype('float') / 100

# Prepare data for 100% stacked bar chart
df.set_index('Day', inplace=True)
df.sort_index(inplace=True)

# Calculate cumulative sum for stacking
cumsum_df = df.cumsum(axis=1)

# Start plotting
fig, ax = plt.subplots(figsize=(10, 14))  # Changed width and height

# Plotting each layer of the stacked bar
colors = ['#FF4500', '#1E90FF', '#FFD700', '#32CD32', '#8A2BE2', '#FF69B4']  # New color scheme
width = 0.8  # Changed the width of the bars

for i, col in enumerate(df.columns):
    ax.bar(df.index, df[col], bottom=cumsum_df[col] - df[col], color=colors[i], edgecolor='white', width=width)

# Customizing the plot
plt.xticks(rotation=0)
plt.yticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xlabel('Day of the Week')
plt.ylabel('Percentage')
plt.title('Daily Nutritional Intake Distribution', pad=20)  # New topic and headline
plt.legend(df.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()