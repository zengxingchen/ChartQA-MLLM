
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Popularity": [
        5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
        25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 
        43, 44, 45, 46, 47, 48, 49, 50
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 10))

sns.histplot(df['Popularity'], 
             bins=10, 
             kde=False, 
             color='#3498db', 
             binwidth=4,
             orientation='vertical')

plt.title('Distribution of Music Popularity Scores')
plt.xlabel('Popularity Score')
plt.ylabel('Frequency')

plt.show()