
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Memberships': [450, 470, 490, 510, 530, 550, 570, 590, 610, 630, 650, 670]
}

df = pd.DataFrame(data)
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(16, 8))

sns.lineplot(data=df, x='Month', y='Memberships', color='#ff5733', marker='o', linewidth=2.5)

plt.text(0, df['Memberships'][0], f"{df['Memberships'][0]}", color='black', ha="center")
plt.text(5, df['Memberships'][5], f"{df['Memberships'][5]}", color='black', ha="center")
plt.text(11, df['Memberships'][11], f"{df['Memberships'][11]}", color='black', ha="center")

plt.title('Monthly Gym Membership Sign-ups in 2023', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Memberships', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()