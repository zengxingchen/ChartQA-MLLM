
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'City': [
        'New York', 'Chicago', 'Berlin', 'Boston', 'London', 'Tokyo', 
        'Paris', 'Los Angeles', 'Barcelona', 'Seoul', 'Madrid', 
        'Moscow', 'Sydney', 'Rome', 'Shanghai', 'Athens', 
        'Beijing', 'Vienna', 'Mumbai', 'Amsterdam', 'Singapore', 
        'Dubai', 'Cape Town', 'Buenos Aires'
    ],
    'Participants': [
        50000, 45000, 42000, 30000, 40000, 38000, 
        35000, 34000, 33000, 32000, 31000, 
        30000, 29000, 28000, 27000, 26000, 
        25000, 24000, 23000, 22000, 21000, 
        20000, 19000, 18000
    ]
}
df = pd.DataFrame(data)

# Set the figure size and style
sns.set(style="whitegrid")
plt.figure(figsize=(12, 10))

# Create a horizontal bar plot with custom color scheme and bar height
barplot = sns.barplot(
    y="City",
    x="Participants",
    data=df,
    palette=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF7',
        '#F7FF33', '#FF5733', '#33FF57', '#3357FF', '#FF33A8',
        '#33FFF7', '#F7FF33', '#FF5733', '#33FF57', '#3357FF',
        '#FF33A8', '#33FFF7', '#F7FF33', '#FF5733', '#33FF57',
        '#3357FF', '#FF33A8', '#33FFF7', '#F7FF33'
    ],
    ci=None
)

# Customize the appearance
barplot.set_title('Top Marathon Cities by Number of Participants in 2021', fontsize=16, pad=20)
barplot.bar_label(barplot.containers[0], fmt='%.0f', fontsize=10)
barplot.set(xlabel="Number of Participants", ylabel="City")

# Adjust the bar width
for bar in barplot.containers[0]:
    bar.set_height(0.5)

# Show the plot
plt.tight_layout()
plt.show()