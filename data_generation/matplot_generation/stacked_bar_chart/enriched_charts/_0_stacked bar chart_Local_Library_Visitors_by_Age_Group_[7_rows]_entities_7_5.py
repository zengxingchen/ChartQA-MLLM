
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020],
    'Apples': [20, 25, 22, 30, 27, 32],
    'Oranges': [35, 30, 29, 45, 40, 38],
    'Bananas': [30, 35, 38, 40, 42, 47],
    'Grapes': [15, 20, 25, 22, 30, 35]
}

df = pd.DataFrame(data)

# Plotting the horiztonal stacked bar chart
fig, ax = plt.subplots(figsize=(10, 8))

ax.barh(df['Year'], df['Apples'], color='#FFA07A', edgecolor='grey', height=0.8, label='Apples')
ax.barh(df['Year'], df['Oranges'], left=df['Apples'], color='#20B2AA', edgecolor='grey', height=0.8, label='Oranges')
ax.barh(df['Year'], df['Bananas'], left=df['Apples']+df['Oranges'], color='#778899', edgecolor='grey', height=0.8, label='Bananas')
ax.barh(df['Year'], df['Grapes'], left=df['Apples']+df['Oranges']+df['Bananas'],
        color='#B0C4DE', edgecolor='grey', height=0.8, label='Grapes')

ax.set_xlabel('Quantity of Fruits')
ax.set_title('Fruit Consumption Over Years')
ax.legend()

plt.show()