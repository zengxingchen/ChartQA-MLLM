
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Steps': [
        4000, 4500, 4700, 5000, 5200, 5500, 5700, 5900, 6000, 6200,
        6300, 6500, 6700, 6900, 7100, 7300, 7500, 7700, 7900, 8100,
        8300, 8500, 8700, 8900, 9100, 9300, 9500, 9700, 9900, 10100,
        10300, 10500, 10700, 10900, 11100, 11300, 11500, 11700, 11900, 12100,
        12300, 12500, 12700, 12900, 13100, 13300, 13500, 13700, 13900
    ]
})

sns.set(style='darkgrid')
plt.figure(figsize=(12, 8))
sns.histplot(data['Steps'], color='#FF6347', binwidth=1000, binrange=(3500, 14000), orientation='vertical')
plt.title('Distribution of Daily Steps')
plt.xlabel('Daily Steps')
plt.ylabel('Frequency')
plt.show()