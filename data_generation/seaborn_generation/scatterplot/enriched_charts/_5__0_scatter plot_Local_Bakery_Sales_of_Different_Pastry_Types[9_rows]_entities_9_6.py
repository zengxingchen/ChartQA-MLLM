
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = """
Category,Amount_Spent,Number_of_Purchases
Groceries,250,30
Clothing,150,5
Electronics,300,2
Dining,200,15
Travel,500,3
Entertainment,120,10
Healthcare,180,7
Utilities,220,8
Transportation,190,12
Education,250,4
Personal_Care,140,6
Housing,700,1
Insurance,300,2
Savings,400,2
Investments,350,1
Charity,50,1
Pets,100,4
Subscriptions,60,5
Gifts,110,3
Miscellaneous,130,6
"""

df = pd.read_csv(StringIO(data))

plt.figure(figsize=(16, 9))
scatter = sns.scatterplot(
    data=df, 
    x="Amount_Spent", 
    y="Number_of_Purchases", 
    palette=sns.color_palette(["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]),
    edgecolor="k", s=150
)

scatter.set_title('Monthly Expenses: Amount Spent vs. Number of Purchases', fontsize=20, pad=20)
scatter.set_xlabel('Amount Spent ($)', fontsize=16)
scatter.set_ylabel('Number of Purchases', fontsize=16)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

sns.despine()

plt.show()