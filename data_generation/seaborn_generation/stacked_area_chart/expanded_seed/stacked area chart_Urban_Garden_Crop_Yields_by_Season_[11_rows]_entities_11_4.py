
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Your data loaded into a DataFrame
data = [
    {'Season': 'Spring 2021', 'Tomatoes (kg)': 15, 'Zucchini (kg)': 0, 'Lettuce (kg)': 10, 'Carrots (kg)': 0, 'Peas (kg)': 5},
    {'Season': 'Summer 2021', 'Tomatoes (kg)': 30, 'Zucchini (kg)': 25, 'Lettuce (kg)': 15, 'Carrots (kg)': 0, 'Peas (kg)': 10},
    {'Season': 'Fall 2021', 'Tomatoes (kg)': 20, 'Zucchini (kg)': 15, 'Lettuce (kg)': 20, 'Carrots (kg)': 10, 'Peas (kg)': 5},
    {'Season': 'Winter 2021', 'Tomatoes (kg)': 0, 'Zucchini (kg)': 0, 'Lettuce (kg)': 15, 'Carrots (kg)': 12, 'Peas (kg)': 2},
    {'Season': 'Spring 2022', 'Tomatoes (kg)': 18, 'Zucchini (kg)': 0, 'Lettuce (kg)': 12, 'Carrots (kg)': 0, 'Peas (kg)': 7},
    {'Season': 'Summer 2022', 'Tomatoes (kg)': 35, 'Zucchini (kg)': 28, 'Lettuce (kg)': 18, 'Carrots (kg)': 0, 'Peas (kg)': 12},
    {'Season': 'Fall 2022', 'Tomatoes (kg)': 23, 'Zucchini (kg)': 18, 'Lettuce (kg)': 22, 'Carrots (kg)': 13, 'Peas (kg)': 6},
    {'Season': 'Winter 2022', 'Tomatoes (kg)': 0, 'Zucchini (kg)': 0, 'Lettuce (kg)': 17, 'Carrots (kg)': 15, 'Peas (kg)': 3},
    {'Season': 'Spring 2023', 'Tomatoes (kg)': 20, 'Zucchini (kg)': 0, 'Lettuce (kg)': 14, 'Carrots (kg)': 0, 'Peas (kg)': 8},
    {'Season': 'Summer 2023', 'Tomatoes (kg)': 40, 'Zucchini (kg)': 30, 'Lettuce (kg)': 20, 'Carrots (kg)': 0, 'Peas (kg)': 15},
    {'Season': 'Fall 2023', 'Tomatoes (kg)': 25, 'Zucchini (kg)': 20, 'Lettuce (kg)': 25, 'Carrots (kg)': 14, 'Peas (kg)': 7}
]

# Create DataFrame from the data
df = pd.DataFrame(data)
# Set the 'Season' column as the index for plotting
df.set_index('Season', inplace=True)

# We will use Seaborn to set the visual aesthetics
sns.set_theme(style="whitegrid")

# Define a color palette
palette = sns.color_palette("husl", len(df.columns))

# Stacked area plot
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(kind='area', stacked=True, ax=ax, color=palette)

# Customize the plot with Seaborn's styling
sns.despine(left=True, bottom=True)

# Adding title and labels
plt.title('Seasonal Production of Vegetables (kg)')
plt.ylabel('Production (kg)')
plt.xlabel('Season')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()