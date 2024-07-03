
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': [
        '2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01',
        '2024-06-01', '2024-07-01', '2024-08-01', '2024-09-01', '2024-10-01',
        '2024-11-01', '2024-12-01', '2025-01-01', '2025-02-01', '2025-03-01',
        '2025-04-01', '2025-05-01', '2025-06-01', '2025-07-01', '2025-08-01',
        '2025-09-01', '2025-10-01', '2025-11-01', '2025-12-01', '2026-01-01',
        '2026-02-01', '2026-03-01', '2026-04-01', '2026-05-01', '2026-06-01',
        '2026-07-01', '2026-08-01', '2026-09-01', '2026-10-01', '2026-11-01',
        '2026-12-01'
    ],
    'Book_Sales': [
        100, 110, 105, 120, 130, 125, 135, 140, 150, 155, 160, 170, 175, 180, 
        185, 190, 200, 210, 220, 225, 230, 235, 240, 250, 255, 260, 265, 270, 
        275, 280, 290, 295, 300, 305, 310, 315
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16, 8))
plt.fill_between(df['Date'], df['Book_Sales'], color='#87CEEB', alpha=0.5)
plt.plot(df['Date'], df['Book_Sales'], color='#4682B4', alpha=0.8)

plt.title('Monthly Book Sales Over Three Years', fontsize=18, y=1.05)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Book Sales (in thousands)', fontsize=14)

for i in range(len(df)):
    if i % 6 == 0:
        plt.text(df['Date'][i], df['Book_Sales'][i] + 2, str(df['Book_Sales'][i]), fontsize=10, ha='center')

plt.show()