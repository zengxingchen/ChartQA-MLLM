
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Height': [
        150, 152, 155, 160, 162, 165, 167, 170, 172, 175,
        177, 180, 182, 185, 187, 190, 192, 195, 197, 200,
        202, 205, 207, 210, 212, 215, 217, 220, 222, 225,
        227, 230, 232, 235, 237, 240, 242, 245, 247, 250,
        252, 255, 257, 260, 262, 265, 267, 270, 272, 275,
        277, 280
    ]
})

sns.set(style='darkgrid')
plt.figure(figsize=(14, 10))
sns.histplot(data['Height'], color='#1E90FF', binwidth=5, binrange=(145, 285), orientation='horizontal')
plt.title('Distribution of Heights', pad=20)
plt.xlabel('Frequency')
plt.ylabel('Height (cm)')
plt.show()