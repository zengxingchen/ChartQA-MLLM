
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
                'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea', 
                'Spain', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 
                'Saudi Arabia', 'Turkey', 'Switzerland'],
    'GDP per Capita (USD)': [62589, 10410, 40200, 46445, 2170, 42230,
                             41465, 8898, 35220, 46214, 11290, 31846, 
                             29760, 55434, 10044, 4240, 52249, 23670, 
                             9125, 83780],
    'Life Expectancy (Years)': [78.86, 76.91, 84.55, 81.18, 69.73, 81.40,
                                82.66, 75.88, 84.01, 82.30, 72.41, 83.30, 
                                83.56, 83.44, 75.07, 71.72, 82.28, 75.13, 
                                77.69, 83.78],
    'Population (Millions)': [331, 1438, 126, 83, 1367, 66,
                              65, 213, 60, 38, 145, 51,
                              47, 25, 128, 273, 17,
                              34, 84, 8]
}

df = pd.DataFrame(data)

# Plotting the bubble chart
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df,
                               x='GDP per Capita (USD)',
                               y='Life Expectancy (Years)',
                               size='Population (Millions)',
                               hue='GDP per Capita (USD)',
                               palette=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'],
                               sizes=(20, 800),
                               alpha=0.7)

plt.title('Health and Economy Indicators of Different Countries')
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Life Expectancy (Years)')
plt.legend(loc='upper left', title='Population (Millions)')

# Show the final plot
plt.show()