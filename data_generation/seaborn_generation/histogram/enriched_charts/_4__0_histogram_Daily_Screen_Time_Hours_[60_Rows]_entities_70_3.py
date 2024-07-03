
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Sleep Hours": [6.5, 7.2, 8.1, 5.4, 7.8, 6.0, 7.3, 8.5, 7.9, 6.6,
                    7.1, 8.0, 5.7, 6.8, 7.4, 8.2, 6.2, 7.6, 8.4, 6.9,
                    7.5, 8.3, 5.9, 7.7, 8.6, 6.1, 7.0, 8.7, 6.3, 7.8,
                    6.4, 8.9, 7.3, 5.8, 7.2, 8.1, 6.5, 7.9, 8.2, 6.6,
                    7.4, 8.3, 6.0, 7.5, 8.5, 6.8, 7.6, 8.0, 5.7, 7.1,
                    8.4, 6.2, 7.8, 6.9, 8.6, 7.0, 5.9, 8.7, 6.3, 7.2, 
                    8.1]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
sns.histplot(data=df, y="Sleep Hours", color="#FF5733", binwidth=0.3, orientation='vertical')
plt.title('Distribution of Sleep Hours per Night')
plt.ylabel('Sleep Hours (hrs)')
plt.xlabel('Frequency')
plt.grid(True)
plt.show()