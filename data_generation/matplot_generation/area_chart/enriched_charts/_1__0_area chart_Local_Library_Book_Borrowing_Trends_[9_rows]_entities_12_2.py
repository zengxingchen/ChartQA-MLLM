
import matplotlib.pyplot as plt
import pandas as pd

# Create the data
data = {
    'Date': pd.date_range(start='2023-05-01', periods=30, freq='D'),
    'Stock_Index': [3200, 3225, 3190, 3215, 3250, 3265, 3245, 3270, 3280, 3260, 3295, 3300, 3325, 3340, 3330, 3350, 3365, 3370, 3380, 3400, 3415, 3430, 3420, 3445, 3450, 3470, 3485, 3490, 3500, 3515]
}

df = pd.DataFrame(data)

# Plot the data
plt.figure(figsize=(12, 6))
plt.fill_between(df['Date'], df['Stock_Index'], color='#1f77b4', alpha=0.5)
plt.plot(df['Date'], df['Stock_Index'], color='#1f77b4', alpha=0.8)

# Title and labels
plt.title('Stock Market Index Over Time', fontsize=16, pad=20)
plt.xlabel('Date')
plt.ylabel('Stock Index')

# Annotations
plt.annotate('Highest Point', xy=(pd.Timestamp('2023-05-30'), 3515), xytext=(pd.Timestamp('2023-05-25'), 3450),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center')

# Display the plot
plt.tight_layout()
plt.show()