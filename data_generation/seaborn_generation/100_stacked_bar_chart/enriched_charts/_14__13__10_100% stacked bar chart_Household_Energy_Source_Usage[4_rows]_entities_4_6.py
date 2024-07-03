
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2019, 'Online Courses (%)': 20, 'Books (%)': 30, 'Workshops (%)': 25, 'Webinars (%)': 25},
    {'Year': 2020, 'Online Courses (%)': 25, 'Books (%)': 35, 'Workshops (%)': 20, 'Webinars (%)': 20},
    {'Year': 2021, 'Online Courses (%)': 22, 'Books (%)': 28, 'Workshops (%)': 30, 'Webinars (%)': 20},
    {'Year': 2022, 'Online Courses (%)': 27, 'Books (%)': 25, 'Workshops (%)': 23, 'Webinars (%)': 25},
    {'Year': 2023, 'Online Courses (%)': 30, 'Books (%)': 20, 'Workshops (%)': 25, 'Webinars (%)': 25}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

df_percent = df.div(df.sum(axis=1), axis=0)

ax = df_percent.plot(kind='bar', stacked=True, color=['#1E90FF', '#FFD700', '#32CD32', '#FF6347'], figsize=(12, 6), width=0.75)

plt.title('Preferred Learning Methods Over Years (Percentage Stacked)', pad=20)
plt.xlabel('Year')
plt.ylabel('Percentage %')

for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy() 
    if height > 0:
        ax.text(x + width / 2, 
                y + height / 2, 
                '{:.0%}'.format(height), 
                horizontalalignment='center', 
                verticalalignment='center')

plt.legend(title='Learning Methods', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()