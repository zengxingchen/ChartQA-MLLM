
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Age': [
        15, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52,
        54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92,
        94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132,
        134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172,
        174, 176, 178, 180
    ]
}

df = pd.DataFrame(data)

sns.set_style('whitegrid')
plt.figure(figsize=(12, 6))

sns.histplot(df['Age'], bins=20, color='#3498db', kde=False, orientation='vertical')

plt.title('Age Distribution in a Demographic Study', fontsize=18, pad=20)
plt.xlabel('Age', fontsize=15)
plt.ylabel('Frequency', fontsize=15)

plt.show()