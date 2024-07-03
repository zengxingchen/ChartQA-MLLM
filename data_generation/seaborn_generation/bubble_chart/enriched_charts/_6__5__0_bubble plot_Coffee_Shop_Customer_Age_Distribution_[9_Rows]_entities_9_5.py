
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Category': ['Fantasy', 'Sci-Fi', 'Mystery', 'Biography', 'Self-Help', 
                 'Romance', 'Horror', 'Historical Fiction', 'Poetry', 'Adventure', 
                 'Drama', 'Non-Fiction', 'Comics'],
    'Revenue': [120000, 150000, 100000, 90000, 110000, 
                140000, 95000, 130000, 70000, 155000, 
                125000, 135000, 105000],
    'Investment': [13000, 15000, 9000, 8000, 10000, 
                   16000, 8500, 14000, 6000, 18000,
                   11000, 12000, 9500],
    'Growth Rate': [10, 12, 8, 7, 9, 
                    11, 8.5, 10.5, 6, 13,
                    9.5, 10, 8.5]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
bubble_chart = sns.scatterplot(data=df, x='Revenue', y='Investment', 
                               hue='Growth Rate', size='Growth Rate', 
                               sizes=(100, 1000), alpha=0.7, 
                               palette=["#FF5733", "#33FF57", "#3357FF", "#FF33FB", "#FFC300", "#581845", "#FF5733", "#33FF57", "#3357FF", "#FF33FB", "#FFC300", "#581845", "#33FF57"])

plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Growth Rate')
plt.title('Revenue vs. Investment by Literature Category with Growth Rate', fontsize=18)
plt.xlabel('Revenue ($)', fontsize=14)
plt.ylabel('Investment ($)', fontsize=14)

plt.show()