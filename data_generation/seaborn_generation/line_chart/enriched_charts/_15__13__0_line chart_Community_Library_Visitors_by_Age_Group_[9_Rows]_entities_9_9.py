
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Total Steps': [8000, 7500, 7200, 6800, 7100, 6900, 6500, 6300, 6000, 5800, 6200, 6400]
}
df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))

line_plot = sns.lineplot(x='Month', y='Total Steps', data=df, color='#FF5733', marker='o')

plt.annotate('New Year Resolution Effect', xy=('January', 8000), xytext=('February', 8500),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=12)
plt.annotate('Summer Dip', xy=('July', 6500), xytext=('August', 6800),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=12)

plt.title('Monthly Step Count in 2024 for Health Tracking', fontsize=18)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Steps', fontsize=12)

plt.xticks(rotation=45)

plt.show()