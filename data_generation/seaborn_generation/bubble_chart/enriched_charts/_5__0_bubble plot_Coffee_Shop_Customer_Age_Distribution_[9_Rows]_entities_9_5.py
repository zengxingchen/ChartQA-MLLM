
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Category': ['Fintech', 'Real Estate', 'Healthcare', 'Retail', 'Manufacturing', 
                 'Tech', 'Energy', 'Transportation', 'Hospitality', 'Education', 
                 'Agriculture', 'Consulting', 'Entertainment'],
    'Revenue': [150000, 90000, 95000, 110000, 105000, 
                85000, 118000, 104000, 80000, 145000, 
                123000, 102000, 97000],
    'Investment': [18000, 14000, 13500, 16000, 11500, 
                   10000, 17000, 14800, 12500, 20000,
                   15500, 13200, 14400],
    'Growth Rate': [12, 8, 9, 10, 7, 
                    6, 11, 8.5, 5.5, 14,
                    9.5, 7.5, 9]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 9))
bubble_chart = sns.scatterplot(data=df, x='Revenue', y='Investment', 
                               hue='Growth Rate', size='Growth Rate', 
                               sizes=(100, 1000), alpha=0.7, 
                               palette=["#FF5733", "#33FF57", "#3357FF", "#FF33FB", "#FFC300", "#581845"])

plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Growth Rate')
plt.title('Revenue vs. Investment by Category with Growth Rate', fontsize=18)
plt.xlabel('Revenue ($)', fontsize=14)
plt.ylabel('Investment ($)', fontsize=14)

plt.show()