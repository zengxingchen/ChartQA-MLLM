
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'ExerciseHours': [
        4, 7, 10, 15, 9, 6, 8, 12, 5, 14, 11, 3, 13, 7, 10, 16, 9, 8, 11, 7, 
        15, 10, 12, 9, 13, 6, 14, 8, 11, 10, 5, 7, 12, 9, 13, 10, 8, 11, 9
    ]
}
df = pd.DataFrame(data)

sns.set_style('whitegrid')

plt.figure(figsize=(12, 6))
sns.histplot(data=df, x="ExerciseHours", color="#3498db", binwidth=2)

plt.title('Histogram of Monthly Exercise Hours by Individuals')
plt.xlabel('Exercise Hours')
plt.ylabel('Frequency')

plt.show()