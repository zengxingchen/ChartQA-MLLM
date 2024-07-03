
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Company': ['Company A', 'Company B', 'Company C', 'Company D', 'Company E', 
                'Company F', 'Company G', 'Company H', 'Company I', 'Company J', 
                'Company K', 'Company L', 'Company M', 'Company N', 'Company O', 
                'Company P', 'Company Q', 'Company R', 'Company S', 'Company T'],
    'Revenue': [800000, 900000, 850000, 1100000, 750000, 940000, 990000, 1040000, 
                880000, 960000, 870000, 920000, 1000000, 910000, 870000, 950000, 
                990000, 850000, 930000, 890000],
    'RD_Spending': [120000, 100000, 95000, 150000, 80000, 110000, 130000, 140000, 
                    90000, 105000, 85000, 98000, 125000, 102000, 89000, 108000, 
                    130000, 92000, 106000, 95000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
sns.scatterplot(data=df, x='Revenue', y='RD_Spending', 
                palette=['#FF5733', '#33FF57', '#3357FF'], 
                s=150)  # Adjusted marker size

plt.title('Company Revenue vs. R&D Spending', fontsize=20, pad=20)
plt.xlabel('Revenue ($)', fontsize=16)
plt.ylabel('R&D Spending ($)', fontsize=16)

plt.show()