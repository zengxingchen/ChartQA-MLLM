
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Company': ['Toyota', 'Volkswagen', 'Ford', 'Honda', 'BMW', 'Nissan', 'Mercedes-Benz', 'Hyundai', 'Kia', 'Peugeot', 'Others'],
    'Shipments': [90.2, 83.4, 65.5, 55.3, 50.1, 45.7, 40.6, 38.5, 35.4, 30.2, 20.3],
    'MarketShare': [20.4, 18.9, 14.9, 12.5, 11.3, 10.4, 9.2, 8.7, 8.0, 6.8, 4.9],
    'Revenue': [250.3, 230.1, 190.6, 165.4, 150.2, 140.3, 130.1, 125.7, 120.8, 110.5, 90.6]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
bubble = sns.scatterplot(data=df, x='MarketShare', y='Shipments', size='Revenue', hue='Company', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#57FFC1', '#FFD133', '#8333FF', '#33FFF7', '#FF335B', '#FF9733', '#737373'], sizes=(100, 2000), alpha=0.7, edgecolor='black')

plt.title('Market Share and Shipments of Car Manufacturers', fontsize=18)
plt.xlabel('Market Share (%)', fontsize=14)
plt.ylabel('Shipments (Millions)', fontsize=14)

hand, labl = bubble.get_legend_handles_labels()
bubble.legend(hand[1:], labl[1:], title='Company', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()