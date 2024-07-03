
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'City': [
        'London', 'Berlin', 'Paris', 'Madrid', 'Rome', 'Amsterdam',
        'Brussels', 'Vienna', 'Oslo', 'Stockholm', 'Copenhagen', 'Lisbon',
        'Prague', 'Warsaw', 'Athens', 'Helsinki', 'Dublin', 'Budapest',
        'Zurich', 'Moscow'
    ],
    'Tourist Arrivals': [
        150000, 130000, 180000, 160000, 170000, 140000,
        110000, 125000, 95000, 105000, 90000, 115000,
        120000, 100000, 135000, 98000, 145000, 125000,
        110000, 95000
    ],
    'Hotel Occupancy Rate': [
        75, 80, 78, 85, 82, 77,
        72, 79, 83, 88, 86, 76,
        84, 81, 79, 82, 85, 80,
        74, 77
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))

sns.scatterplot(
    x='Tourist Arrivals', y='Hotel Occupancy Rate',
    hue='City', palette=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF',
        '#33FFA1', '#FFA133', '#33A1FF', '#A1FF33', '#FF3333',
        '#57FF33', '#5733FF', '#FF33FF', '#33FF33', '#FF5733',
        '#33A1FF', '#FFA133', '#A133FF', '#FF33A1', '#33FFA1'
    ],
    data=df,
    s=120
)

plt.xlabel('Tourist Arrivals')
plt.ylabel('Hotel Occupancy Rate')
plt.title('Tourism Impact on Hotel Occupancy in Various Cities', pad=20)
plt.show()