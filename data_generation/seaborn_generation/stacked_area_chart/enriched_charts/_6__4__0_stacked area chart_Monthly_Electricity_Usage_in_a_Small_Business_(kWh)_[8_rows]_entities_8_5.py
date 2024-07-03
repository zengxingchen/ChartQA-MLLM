
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Protein': [50, 60, 55, 65, 70, 75, 80, 85, 90, 95, 100, 105],
    'Carbohydrates': [200, 210, 215, 220, 230, 240, 250, 260, 270, 280, 290, 300],
    'Fat': [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Nutrient', value_name='Values')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(16, 12))
sns.set(style="whitegrid")

colors = ["#8B0000", "#FFD700", "#1E90FF"]  # Protein, Carbohydrates, Fat

sns.lineplot(data=df_melted, x='Month', y='Values', hue='Nutrient', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Protein"], color="#8B0000", alpha=0.5)
plt.fill_between(data['Month'], df["Protein"], df["Protein"] + df["Carbohydrates"], color="#FFD700", alpha=0.5)
plt.fill_between(data['Month'], df["Protein"] + df["Carbohydrates"], df["Protein"] + df["Carbohydrates"] + df["Fat"], color="#1E90FF", alpha=0.5)

for idx, month in enumerate(data['Month']):
    if idx % 2 == 0:
        plt.text(x=idx, y=df.loc[idx, "Protein"]/2, s=df.loc[idx, "Protein"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Protein"] + df.loc[idx, "Carbohydrates"]/2, s=df.loc[idx, "Carbohydrates"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Protein"] + df.loc[idx, "Carbohydrates"] + df.loc[idx, "Fat"]/2, s=df.loc[idx, "Fat"], ha='center', color='black')

plt.xlabel('Month')
plt.ylabel('Intake (grams)')
plt.title('Monthly Nutrient Intake in a Balanced Diet', pad=20, loc='left')
plt.xticks(rotation=45)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()