
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'age': [22, 25, 28, 29, 30, 31, 33, 35, 36, 38, 40, 42, 44, 46,
            48, 50, 51, 53, 55, 57, 60, 62, 65, 68]
}
df = pd.DataFrame(data)

# Seaborn Histogram
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], color="#3498db", binwidth=2)

plt.title('Age Distribution of Participants')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Show plot
plt.show()