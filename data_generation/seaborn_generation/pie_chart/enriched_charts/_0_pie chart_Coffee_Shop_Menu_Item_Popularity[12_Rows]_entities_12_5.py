
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {
    'Brand': [
        'Toyota', 'Volkswagen', 'Ford', 'Honda', 'Nissan',
        'Hyundai', 'Kia', 'BMW', 'Mercedes-Benz', 'Audi'
    ],
    'Market Share': [
        24, 18, 15, 12, 11, 8, 6, 3, 2, 1
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Colors for each brand
colors = [
    '#FFD700', '#C0C0C0', '#CD7F32', '#8E44AD', '#3498DB',
    '#1ABC9C', '#2ECC71', '#F39C12', '#D35400', '#7F8C8D'
]

# Create pie chart
plt.figure(figsize=(10, 8))  # Set the size of the figure
plt.pie(
    df['Market Share'],
    labels=df['Brand'],
    autopct='%1.1f%%',  # Display the percentage value
    startangle=140,
    colors=colors  # Use specific color codes for each slice
)

# Set the title of the chart
plt.title('Car Brand Market Share in 2023')

# Show the chart
plt.show()