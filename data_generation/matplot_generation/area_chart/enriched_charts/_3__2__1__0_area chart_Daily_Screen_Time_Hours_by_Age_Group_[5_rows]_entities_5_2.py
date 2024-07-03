
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
    'Views': [
        105, 115, 108, 112, 120, 110, 125, 118, 122, 130, 128, 135, 132, 138, 
        140, 145, 150, 155, 153, 160, 165, 162, 170, 175, 178, 183, 185, 190, 
        195, 200, 205, 210, 215, 220, 225, 230
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16, 8))
plt.fill_between(df['Date'], df['Views'], color='#6A5ACD', alpha=0.5)
plt.plot(df['Date'], df['Views'], color='#483D8B', alpha=0.8)

plt.title('Monthly Website Traffic Analysis', fontsize=18, y=1.05)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Views (in thousands)', fontsize=14)

for i in range(len(df)):
    if i % 6 == 0:
        plt.text(df['Date'][i], df['Views'][i] + 2, str(df['Views'][i]), fontsize=10, ha='center')

plt.show()