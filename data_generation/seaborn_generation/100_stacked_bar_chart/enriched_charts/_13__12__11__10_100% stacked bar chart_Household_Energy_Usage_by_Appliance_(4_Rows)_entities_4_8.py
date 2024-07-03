
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Category': 'Product A', 'Revenue Generated': 500, 'Customer Satisfaction': 80, 'New Clients': 150, 'Market Share': 30, 'Employee Engagement': 70},
    {'Category': 'Product B', 'Revenue Generated': 700, 'Customer Satisfaction': 85, 'New Clients': 200, 'Market Share': 40, 'Employee Engagement': 75},
    {'Category': 'Product C', 'Revenue Generated': 450, 'Customer Satisfaction': 78, 'New Clients': 120, 'Market Share': 25, 'Employee Engagement': 68},
    {'Category': 'Product D', 'Revenue Generated': 600, 'Customer Satisfaction': 83, 'New Clients': 180, 'Market Share': 35, 'Employee Engagement': 73},
    {'Category': 'Product E', 'Revenue Generated': 550, 'Customer Satisfaction': 82, 'New Clients': 160, 'Market Share': 33, 'Employee Engagement': 72}
]

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(14, 8))

bottom = np.zeros(len(df))

colors = ['#00429d', '#76c893', '#e07b39', '#d95f02', '#6a3d9a']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.4)
    bottom += df_percentage[col]

plt.xlabel('Products')
plt.ylabel('Percentage')
plt.title('Business Performance Metrics Breakdown (100% Stacked)', pad=20)
plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()