
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Age": [25, 28, 32, 27, 30, 34, 22, 26, 29, 33, 31, 21, 24, 35, 36, 23, 38, 20, 39, 37, 
            40, 41, 19, 42, 18, 17, 43, 16, 44, 15, 45, 46, 14, 47, 13, 48, 12, 49, 50, 11, 
            51, 10, 52, 9, 53, 8, 54, 7, 55, 6, 56, 5, 57, 4, 58, 3, 59, 2, 60, 1, 61, 62]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 8))

sns.histplot(data=df, x="Age", color="#FF6347", binwidth=2, orientation='horizontal')

plt.title('Distribution of Ages Among Participants')
plt.xlabel('Frequency')
plt.ylabel('Age')
plt.grid(True)

plt.show()