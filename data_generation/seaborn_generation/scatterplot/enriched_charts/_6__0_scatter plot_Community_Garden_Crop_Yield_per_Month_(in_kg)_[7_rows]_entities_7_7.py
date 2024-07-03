
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data: City fitness details
data = {
    'City': [
        'London', 'Berlin', 'Paris', 'Madrid', 'Rome',
        'Amsterdam', 'Brussels', 'Vienna', 'Oslo',
        'Stockholm', 'Copenhagen', 'Lisbon', 'Prague',
        'Warsaw', 'Athens', 'Helsinki', 'Dublin',
        'Barcelona', 'Milan', 'Zurich', 'Budapest',
        'Sofia', 'Reykjavik', 'Edinburgh'
    ],
    'Average Weekly Exercise Hours': [
        4, 6, 5, 7, 6,
        5, 4, 5, 7,
        6, 6, 8, 5,
        4, 7, 5, 6,
        8, 6, 7, 5,
        4, 6, 5
    ],
    'Fitness Level (%)': [
        70, 75, 72, 80, 78,
        76, 68, 74, 85,
        82, 79, 87, 77,
        71, 83, 75, 73,
        86, 81, 84, 76,
        69, 80, 72
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set the width and height of the plot
plt.figure(figsize=(14, 10))

# Create Seaborn scatterplot
sns.scatterplot(
    x='Average Weekly Exercise Hours', y='Fitness Level (%)',
    hue='City', palette=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1',
        '#FFA133', '#A133FF', '#33A1FF', '#A1FF33', '#33A1A1',
        '#A13333', '#33FFA1', '#A1A133', '#57FF33', '#A133A1',
        '#33FF57', '#A15733', '#5733FF', '#A15757', '#33A157',
        '#FF5733', '#57A133', '#3357A1', '#57A1A1'
    ],
    data=df,
    s=120  # Marker size
)

# Add labels and title
plt.xlabel('Average Weekly Exercise Hours')
plt.ylabel('Fitness Level (%)')
plt.title('Average Weekly Exercise Hours vs. Fitness Level')

# Display plot
plt.show()