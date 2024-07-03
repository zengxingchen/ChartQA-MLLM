
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'hours_of_sleep': [5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 12]
}
df = pd.DataFrame(data)

# Seaborn Horizontal Histogram
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))
sns.histplot(df['hours_of_sleep'], color="#FF5733", binwidth=1, orientation="horizontal")

plt.title('Distribution of Hours of Sleep Among Participants')
plt.xlabel('Frequency')
plt.ylabel('Hours of Sleep')

# Show plot
plt.show()