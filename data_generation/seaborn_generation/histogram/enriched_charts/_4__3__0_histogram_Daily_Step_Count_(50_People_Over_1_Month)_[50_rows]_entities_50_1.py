
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Hours': [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 1, 2, 3, 4, 5,
        6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        12, 13, 14, 15, 3, 4, 5, 6, 7, 8,
        9, 10, 11, 12, 13, 14, 15, 4, 5, 6,
        7, 8, 9, 10, 11, 12, 13, 14, 15
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

sns.histplot(data=df, x='Hours', color='#3498DB', binwidth=1, kde=True, orientation='horizontal')

plt.title('Daily Study Hours Distribution in a Sample Population')
plt.ylabel('Frequency')
plt.xlabel('Hours Spent on Study per Day')
plt.grid(True)

plt.show()