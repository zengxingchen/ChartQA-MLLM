
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Fruit Consumption': [3.2, 3.5, 4.1, 4.7, 5.3, 5.8, 6.2, 6.0, 5.6, 5.0, 4.4, 3.8]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 10))
plt.fill_between(df['Month'], df['Fruit Consumption'], color='#ff7f0e', alpha=0.6)
plt.plot(df['Month'], df['Fruit Consumption'], color='#ff7f0e')

# Add title and labels
plt.title('Average Monthly Fruit Consumption', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Fruit Consumption (kg)', fontsize=14)

# Add annotation
for i, consumption in enumerate(df['Fruit Consumption']):
    plt.text(i, consumption + 0.1, f'{consumption} kg', ha='center', fontsize=10)

plt.grid(True)
plt.show()