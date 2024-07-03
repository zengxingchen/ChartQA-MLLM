
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data: City ratings for adventure and culture
data = {
    'City': [
        'London', 'Berlin', 'Paris', 'Madrid', 'Rome',
        'Amsterdam', 'Brussels', 'Vienna', 'Oslo',
        'Stockholm', 'Copenhagen', 'Lisbon', 'Prague',
        'Warsaw', 'Athens', 'Helsinki', 'Dublin',
        'Zurich', 'Barcelona', 'Munich'
    ],
    'Adventure Score': [
        85, 88, 92, 80, 95,
        89, 86, 91, 83,
        90, 87, 85, 89,
        84, 92, 86, 90,
        87, 88, 90
    ],
    'Culture Score': [
        90, 85, 95, 88, 93,
        87, 84, 89, 86,
        92, 91, 88, 90,
        87, 89, 85, 88,
        89, 91, 93
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set the width and height of the plot
plt.figure(figsize=(16, 12))

# Create Seaborn scatterplot
sns.scatterplot(
    x='Adventure Score', y='Culture Score',
    hue='City', palette=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF6',
        '#FFAA33', '#AA33FF', '#FF3333', '#33FFAA', '#AAFF33',
        '#FF33AA', '#33AAFF', '#AAFFAA', '#33FF33', '#FFAAFF',
        '#AAFF33', '#FFAA33', '#FF33AA', '#33AAFF', '#FF33FF'
    ],
    data=df,
    s=120  # Marker size
)

# Add labels and title
plt.xlabel('Adventure Score')
plt.ylabel('Culture Score')
plt.title('City Ratings for Adventure and Culture', pad=20)

# Display plot
plt.show()