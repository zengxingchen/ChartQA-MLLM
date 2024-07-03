
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data: City GDP and Unemployment Rate
data = {
    'City': [
        'London', 'Berlin', 'Paris', 'Madrid', 'Rome',
        'Amsterdam', 'Brussels', 'Vienna', 'Oslo',
        'Stockholm', 'Copenhagen', 'Lisbon', 'Prague',
        'Warsaw', 'Athens', 'Helsinki', 'Dublin',
        'Barcelona', 'Zurich', 'Milan', 'Munich',
        'Hamburg', 'Frankfurt'
    ],
    'GDP (Billion $)': [
        600, 300, 350, 250, 200,
        180, 170, 160, 100,
        130, 140, 90, 110,
        120, 80, 95, 105,
        220, 280, 240, 320,
        200, 260
    ],
    'Unemployment Rate (%)': [
        4.5, 5.0, 7.2, 13.5, 11.0,
        3.4, 6.8, 4.9, 3.6,
        6.0, 4.1, 12.3, 2.9,
        3.3, 15.2, 4.7, 5.2,
        14.1, 3.0, 8.6, 3.9,
        5.5, 4.4
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set the width and height of the plot
plt.figure(figsize=(14, 10))

# Create Seaborn scatterplot
sns.scatterplot(
    x='GDP (Billion $)', y='Unemployment Rate (%)',
    hue='City', palette=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1',
        '#A133FF', '#FFA133', '#33D4FF', '#FF3399', '#9933FF',
        '#33FFBD', '#FF5733', '#FF33EC', '#33FF57', '#FF3333',
        '#33FFF4', '#A1FF33', '#FF3399', '#FFD433', '#A1FF33',
        '#33A1FF', '#33FF57', '#FF5733'
    ],
    data=df,
    s=100  # Marker size
)

# Add labels and title
plt.xlabel('GDP (Billion $)')
plt.ylabel('Unemployment Rate (%)')
plt.title('City GDP vs. Unemployment Rate in Europe')

# Display plot
plt.show()