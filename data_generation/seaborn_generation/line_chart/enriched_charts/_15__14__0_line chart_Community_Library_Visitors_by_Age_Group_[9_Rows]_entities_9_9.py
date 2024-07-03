
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Calories Burned': [250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
}
df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

line_plot = sns.lineplot(x='Month', y='Calories Burned', data=df, color='#FF5733', marker='o')

plt.annotate('Summer Peak', xy=('August', 600), xytext=('September', 650),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=12)
plt.annotate('Winter Start', xy=('November', 750), xytext=('December', 800),
             arrowprops=dict(facecolor='purple', shrink=0.05), fontsize=12)

plt.title('Monthly Calories Burned Trends for Fitness Program', fontsize=18, loc='center')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Calories Burned', fontsize=12)

plt.xticks(rotation=45)

plt.show()