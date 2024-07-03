
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Rating': [8.5, 7.2, 9.1, 6.8, 7.9, 8.3, 7.6, 8.0, 9.4, 6.5, 7.4, 8.7, 6.9, 
               7.8, 8.2, 9.0, 6.7, 7.3, 8.6, 7.1, 8.4, 7.7, 9.3, 6.6, 7.5, 8.1, 
               9.2, 6.4, 7.0, 8.9, 6.3, 9.5, 8.8, 6.2, 7.1, 8.0, 6.1, 7.3, 8.2, 9.1]
}

df = pd.DataFrame(data)

sns.set_style('whitegrid')

plt.figure(figsize=(12, 6))

sns.histplot(df['Rating'], bins=8, kde=False, color='#3498db', binwidth=0.6, orientation='vertical')

plt.title('Distribution of Movie Ratings', pad=20)
plt.xlabel('Rating')
plt.ylabel('Frequency')

plt.show()