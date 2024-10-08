
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Hours of Sleep': [
        7, 8, 6, 6, 7, 7, 8, 9, 7, 6,
        7, 7, 8, 9, 10, 8, 7, 7, 6, 7,
        6, 5, 4, 3, 8, 7, 10, 11, 9, 8,
        12, 10, 9, 10, 11, 9, 8, 7, 8, 9,
        7, 6, 5, 4, 7, 7, 8, 9, 10, 8,
        7, 8, 9, 8, 10, 11, 9, 7, 6, 6
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 8))

sns.histplot(data=df, y='Hours of Sleep', color='#FF5733', binwidth=1, kde=True, orientation='vertical')

plt.title('Distribution of Hours of Sleep per Night')
plt.xlabel('Frequency')
plt.ylabel('Hours of Sleep')
plt.grid(True)

plt.show()