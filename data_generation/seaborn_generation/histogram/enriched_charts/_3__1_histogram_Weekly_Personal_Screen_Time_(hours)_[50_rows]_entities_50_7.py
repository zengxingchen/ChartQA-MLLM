
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'price': [15, 18, 22, 22, 25, 29, 30, 32, 35, 35, 36, 38, 40, 42, 45, 48, 
              50, 53, 55, 58, 60, 62, 65, 68, 70, 73, 75, 78, 80, 82, 85, 88, 90]
}
df = pd.DataFrame(data)

# Seaborn Histogram
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))
sns.histplot(df['price'], color="#2ecc71", binwidth=5, orientation='horizontal')

plt.title('Distribution of Product Prices')
plt.xlabel('Frequency')
plt.ylabel('Price')

# Show plot
plt.show()