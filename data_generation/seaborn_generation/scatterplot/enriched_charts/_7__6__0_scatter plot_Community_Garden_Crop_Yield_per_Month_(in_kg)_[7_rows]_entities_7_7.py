
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data: City travel details
data = {
    'City': [
        'London', 'Berlin', 'Paris', 'Madrid', 'Rome',
        'Amsterdam', 'Brussels', 'Vienna', 'Oslo',
        'Stockholm', 'Copenhagen', 'Lisbon', 'Prague',
        'Warsaw', 'Athens', 'Helsinki', 'Dublin',
        'Barcelona', 'Milan', 'Zurich', 'Budapest',
        'Sofia', 'Reykjavik', 'Edinburgh'
    ],
    'Average Monthly Travel Hours': [
        15, 18, 17, 20, 19,
        16, 14, 17, 22,
        21, 20, 24, 18,
        15, 22, 18, 19,
        23, 20, 21, 16,
        14, 22, 18
    ],
    'Happiness Level (%)': [
        72, 75, 74, 78, 76,
        77, 71, 76, 82,
        80, 81, 83, 74,
        70, 79, 75, 74,
        84, 78, 80, 73,
        68, 81, 74
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set the width and height of the plot
plt.figure(figsize=(16, 12))

# Create Seaborn scatterplot
sns.scatterplot(
    x='Average Monthly Travel Hours', y='Happiness Level (%)',
    hue='City', palette=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1',
        '#FFA133', '#A133FF', '#33A1FF', '#A1FF33', '#33A1A1',
        '#A13333', '#33FFA1', '#A1A133', '#57FF33', '#A133A1',
        '#33FF57', '#A15733', '#5733FF', '#A15757', '#33A157',
        '#FF5733', '#57A133', '#3357A1', '#57A1A1'
    ],
    data=df,
    s=150  # Marker size
)

# Add labels and title
plt.xlabel('Average Monthly Travel Hours')
plt.ylabel('Happiness Level (%)')
plt.title('Average Monthly Travel Hours vs. Happiness Level', fontsize=18, pad=20)

# Display plot
plt.show()