
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': pd.date_range(start='2023-05-01', periods=31, freq='D'),
    'Visitors': [
        2200, 2300, 2100, 2150, 2250, 2350, 2450, 2550, 2650, 2750,
        2850, 2950, 3050, 3150, 3250, 3350, 3450, 3550, 3650, 3750,
        3850, 3950, 4050, 4150, 4250, 4350, 4450, 4550, 4650, 4750, 4850
    ]
}

df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(14, 7))
plt.fill_between(df['Date'], df['Visitors'], color="#FF7F50")
plt.plot(df['Date'], df['Visitors'], color="#FF4500")

# Annotation
for index in range(0, df.shape[0], 5):  # Adding annotations every 5 days for clarity
    date = df.iloc[index]['Date']
    visitors = df.iloc[index]['Visitors']
    plt.text(date, visitors + 100, str(visitors), ha='center')

# Customization
plt.title('Daily Tourists Visiting the National Park in May 2023', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Visitors', fontsize=12)
plt.xticks(rotation=45)
plt.grid(visible=True, linestyle='--', alpha=0.6)

# Show the plot
plt.tight_layout()
plt.show()