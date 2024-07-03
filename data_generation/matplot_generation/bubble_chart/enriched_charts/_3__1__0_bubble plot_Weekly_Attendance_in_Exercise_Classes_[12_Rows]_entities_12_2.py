
import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Define the table data as pandas DataFrame
data = {
    "Age Group": ["10-20", "10-20", "10-20", "10-20",
                  "21-30", "21-30", "21-30", "21-30",
                  "31-40", "31-40", "31-40", "31-40",
                  "41-50", "41-50", "41-50", "41-50",
                  "51-60", "51-60", "51-60", "51-60",
                  "60+", "60+", "60+", "60+"],
    "Food Type": ["Fruits", "Vegetables", "Meat", "Dairy",
                  "Fruits", "Vegetables", "Meat", "Dairy",
                  "Fruits", "Vegetables", "Meat", "Dairy",
                  "Fruits", "Vegetables", "Meat", "Dairy",
                  "Fruits", "Vegetables", "Meat", "Dairy",
                  "Fruits", "Vegetables", "Meat", "Dairy"],
    "Average Weekly Consumption (lbs)": [4, 5, 3, 6,
                                          6, 7, 5, 4,
                                          5, 8, 6, 5,
                                          3, 6, 4, 5,
                                          4, 5, 3, 4,
                                          5, 6, 2, 3],
    "Number of Participants": [200000, 220000, 180000, 250000,
                               300000, 320000, 290000, 270000,
                               270000, 280000, 260000, 250000,
                               210000, 230000, 220000, 240000,
                               190000, 200000, 180000, 210000,
                               150000, 160000, 130000, 140000]
}

df = pd.DataFrame(data)

# Step 2: Prepare the color mapping
food_colors = {
    'Fruits': '#FF6F61',
    'Vegetables': '#6B8E23',
    'Meat': '#D2691E',
    'Dairy': '#4682B4'
}

# Step 3: Generate the bubble chart
plt.figure(figsize=(18, 12))  # Changed width and height reasonably
for food in df['Food Type'].unique():
    subset = df[df['Food Type'] == food]
    plt.scatter(
        subset['Age Group'], 
        subset['Average Weekly Consumption (lbs)'], 
        s=subset['Number of Participants'] / 1000,  # Bubble sizes
        alpha=0.6,
        color=food_colors[food],
        label=food
    )

# Step 4: Chart formatting and topic/headline changes
plt.title('Average Weekly Consumption of Various Foods by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Weekly Consumption (lbs)')
plt.legend(title='Food Type', loc='upper left')
plt.grid(True)
plt.show()