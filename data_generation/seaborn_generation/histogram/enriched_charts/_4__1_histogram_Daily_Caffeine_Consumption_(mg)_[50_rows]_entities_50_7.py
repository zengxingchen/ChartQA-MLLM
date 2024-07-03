
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Sleep_Hours': [7, 8, 6, 5, 9, 7.5, 6.5, 8.2, 5.7, 7.1, 6.8, 9.3, 5.5, 6.9, 8.7, 
                    7.3, 6.2, 8.5, 7.6, 7.9, 6.3, 9.1, 7.8, 5.8, 8.4, 6.6, 7.4, 9.5, 
                    8.8, 7.2, 6.4, 8.1, 7.7, 6.7, 9.2, 5.9]
}

df = pd.DataFrame(data)

sns.set_style('whitegrid')
plt.figure(figsize=(8, 10))
sns.histplot(df['Sleep_Hours'], bins=15, kde=False, color='#ff5733', binwidth=0.5)
plt.title('Sleep Hours Distribution of Individuals', loc='right')
plt.xlabel('Hours of Sleep')
plt.ylabel('Frequency')
plt.show()