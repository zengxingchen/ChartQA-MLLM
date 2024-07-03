
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Workshops': [200, 220, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430],
    'Online Courses': [180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290],
    'Conferences': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Values')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(18, 10))
sns.set(style="whitegrid")

colors = ["#FF6347", "#4682B4", "#3CB371"]  # Workshops, Online Courses, Conferences

sns.lineplot(data=df_melted, x='Month', y='Values', hue='Category', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Workshops"], color="#FF6347", alpha=0.5)
plt.fill_between(data['Month'], df["Workshops"], df["Workshops"] + df["Online Courses"], color="#4682B4", alpha=0.5)
plt.fill_between(data['Month'], df["Workshops"] + df["Online Courses"], df["Workshops"] + df["Online Courses"] + df["Conferences"], color="#3CB371", alpha=0.5)

for idx, month in enumerate(data['Month']):
    if idx % 2 == 0:
        plt.text(x=idx, y=df.loc[idx, "Workshops"]/2, s=df.loc[idx, "Workshops"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Workshops"] + df.loc[idx, "Online Courses"]/2, s=df.loc[idx, "Online Courses"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Workshops"] + df.loc[idx, "Online Courses"] + df.loc[idx, "Conferences"]/2, s=df.loc[idx, "Conferences"], ha='center', color='black')

plt.xlabel('Month')
plt.ylabel('Participation')
plt.title('Monthly Trends in Education & Learning', pad=20)
plt.xticks(rotation=45)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()