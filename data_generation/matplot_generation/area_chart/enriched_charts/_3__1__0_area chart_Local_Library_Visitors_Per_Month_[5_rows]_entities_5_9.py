
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=36, freq='MS'),
    'Score': [10, 12, 11, 14, 16, 18, 20, 23, 22, 25, 27, 28, 30, 32, 31, 33, 36, 37, 39, 41, 42, 45, 47, 50, 52, 54, 55, 57, 59, 60, 62, 64, 66, 67, 69, 70]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 9))
ax.fill_between(df['Date'], df['Score'], color='#5b84b1', alpha=0.7)

ax.set_title('Health & Psychology: Mental Health Improvement Over Time', fontsize=18, pad=25)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Mental Health Score', fontsize=14)
ax.annotate('Significant Improvement', xy=(df['Date'].iloc[-1], df['Score'].iloc[-1]), xytext=(df['Date'].iloc[-10], df['Score'].iloc[-1] + 5),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             fontsize=12)

plt.tight_layout()
plt.show()