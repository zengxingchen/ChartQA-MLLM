
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Company': ['Apple', 'Microsoft', 'Google', 'Amazon', 'Facebook', 'Intel', 'Tesla', 'IBM', 'Samsung', 'Huawei', 'Qualcomm', 'Cisco', 'Oracle', 'Sony', 'NVIDIA'],
    'R&D_Expenditure': [20000, 19000, 22000, 42000, 18000, 13000, 1500, 6000, 16000, 15000, 5600, 6300, 6400, 5500, 3400],
    'Revenue': [260000, 143000, 161857, 386064, 85965, 77965, 31536, 73200, 211940, 107000, 23531, 49161, 40579, 84500, 10818],
    'Employee_Count': [137000, 156439, 135301, 1335000, 58604, 110600, 70757, 282100, 287439, 194000, 41000, 77900, 132000, 114400, 18875],
    'Market_Influence': [95, 90, 93, 88, 85, 80, 87, 78, 92, 83, 81, 77, 82, 84, 79]
})

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(
    data=data,
    x='R&D_Expenditure',
    y='Revenue',
    size='Employee_Count',
    hue='Market_Influence',
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5'],
    sizes=(100, 2500),
    alpha=0.6
)

plt.legend(title='Market Influence Rating', loc='upper left', bbox_to_anchor=(1, 1))
plt.title('R&D Expenditure vs Revenue in Tech Companies', fontsize=20, pad=20)
plt.xlabel('R&D Expenditure in Millions USD', fontsize=14)
plt.ylabel('Revenue in Millions USD', fontsize=14)

plt.show()