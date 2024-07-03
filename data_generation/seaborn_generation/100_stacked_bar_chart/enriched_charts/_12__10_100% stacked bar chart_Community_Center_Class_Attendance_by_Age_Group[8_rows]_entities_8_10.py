
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Calories Burned in Gym': '500', 'Calories Burned Running': '300', 'Calories Burned Swimming': '200'},
    {'Month': 'February', 'Calories Burned in Gym': '450', 'Calories Burned Running': '350', 'Calories Burned Swimming': '250'},
    {'Month': 'March', 'Calories Burned in Gym': '550', 'Calories Burned Running': '250', 'Calories Burned Swimming': '200'},
    {'Month': 'April', 'Calories Burned in Gym': '600', 'Calories Burned Running': '300', 'Calories Burned Swimming': '100'},
    {'Month': 'May', 'Calories Burned in Gym': '650', 'Calories Burned Running': '200', 'Calories Burned Swimming': '150'},
    {'Month': 'June', 'Calories Burned in Gym': '700', 'Calories Burned Running': '300', 'Calories Burned Swimming': '100'},
    {'Month': 'July', 'Calories Burned in Gym': '750', 'Calories Burned Running': '350', 'Calories Burned Swimming': '100'},
    {'Month': 'August', 'Calories Burned in Gym': '800', 'Calories Burned Running': '250', 'Calories Burned Swimming': '150'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].astype('float')

df_long = df.melt(id_vars='Month', var_name='Activity', value_name='Calories')

pivot_df = df_long.pivot(index='Month', columns='Activity', values='Calories')

colors = ['#FF5733', '#33FF57', '#3357FF']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(10, 6), width=0.7)

plt.title('Monthly Calories Burned by Activity', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Calories Burned', labelpad=15)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()