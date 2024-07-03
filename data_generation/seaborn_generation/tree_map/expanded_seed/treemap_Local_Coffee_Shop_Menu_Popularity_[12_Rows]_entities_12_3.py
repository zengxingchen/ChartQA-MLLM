
import matplotlib.pyplot as plt
import squarify

# Our data
data = [
    {'Item': 'Cappuccino', ' Number of Orders (Monthly)': 750, ' Average Prep Time (Seconds)': 60, ' Margin (%)': ' 70%'},
    {'Item': 'Latte', ' Number of Orders (Monthly)': 900, ' Average Prep Time (Seconds)': 45, ' Margin (%)': ' 65%'},
    {'Item': 'Espresso', ' Number of Orders (Monthly)': 1040, ' Average Prep Time (Seconds)': 30, ' Margin (%)': ' 80%'},
    {'Item': 'Americano', ' Number of Orders (Monthly)': 480, ' Average Prep Time (Seconds)': 25, ' Margin (%)': ' 85%'},
    {'Item': 'Mocha', ' Number of Orders (Monthly)': 650, ' Average Prep Time (Seconds)': 70, ' Margin (%)': ' 60%'},
    {'Item': 'Iced Coffee', ' Number of Orders (Monthly)': 570, ' Average Prep Time (Seconds)': 40, ' Margin (%)': ' 75%'},
    {'Item': 'Tea', ' Number of Orders (Monthly)': 230, ' Average Prep Time (Seconds)': 50, ' Margin (%)': ' 80%'},
    {'Item': 'Pastry', ' Number of Orders (Monthly)': 1120, ' Average Prep Time (Seconds)': 5, ' Margin (%)': ' 50%'},
    {'Item': 'Sandwich', ' Number of Orders (Monthly)': 360, ' Average Prep Time (Seconds)': 120, ' Margin (%)': ' 55%'},
    {'Item': 'Salad', ' Number of Orders (Monthly)': 310, ' Average Prep Time (Seconds)': 60, ' Margin (%)': ' 60%'},
    {'Item': 'Juice', ' Number of Orders (Monthly)': 190, ' Average Prep Time (Seconds)': 30, ' Margin (%)': ' 70%'},
    {'Item': 'Smoothie', ' Number of Orders (Monthly)': 410, ' Average Prep Time (Seconds)': 90, ' Margin (%)': ' 65%'}
]

# Preparing the data for the Treemap
labels = [f"{x['Item']}\n{x[' Margin (%)']}" for x in data]
sizes = [x[' Number of Orders (Monthly)'] for x in data]
colors = [x[' Average Prep Time (Seconds)'] for x in data]

# Normalizing the colors to get a continuous range
norm = plt.Normalize(min(colors), max(colors))
colors = [plt.cm.viridis(norm(value)) for value in colors]

# Creating the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Adding color bar
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
plt.colorbar(sm, aspect=10, fraction=0.03, pad=0.04)

# Removing axis for better aesthetics
plt.axis('off')

# Adding a title to the plot
plt.title('Monthly Number of Orders Treemap with Prep Time Color-Coding')

# Showing the plot
plt.show()