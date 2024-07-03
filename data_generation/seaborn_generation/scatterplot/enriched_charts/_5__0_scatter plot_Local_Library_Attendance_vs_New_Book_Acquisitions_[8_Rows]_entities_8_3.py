
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'City': ['London', 'Paris', 'Rome', 'Berlin', 'Madrid', 'Amsterdam', 'Prague', 
             'Vienna', 'Venice', 'Barcelona', 'Lisbon', 'Athens',
             'Dublin', 'Oslo', 'Stockholm', 'Helsinki', 'Copenhagen', 
             'Budapest', 'Warsaw', 'Istanbul'],
    'AverageIncome': [55000, 48000, 45000, 53000, 47000, 59000, 40000, 54000, 45000, 50000, 
                      42000, 38000, 57000, 62000, 60000, 55000, 61000, 43000, 41000, 39000],
    'AverageSpending': [32000, 31000, 29000, 30000, 28000, 33000, 26000, 31000, 27500, 
                        29500, 27000, 25000, 32000, 34000, 33500, 31000, 33000, 26000, 25500, 24000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
sns.scatterplot(data=df, x='AverageIncome', y='AverageSpending', 
                palette=['#4B0082', '#FFD700'], 
                s=120)  # Adjusted marker size

plt.title('Relationship between Average Income and Average Spending in European Cities', fontsize=18, pad=20)
plt.xlabel('Average Income ($)', fontsize=14)
plt.ylabel('Average Spending ($)', fontsize=14)

plt.show()