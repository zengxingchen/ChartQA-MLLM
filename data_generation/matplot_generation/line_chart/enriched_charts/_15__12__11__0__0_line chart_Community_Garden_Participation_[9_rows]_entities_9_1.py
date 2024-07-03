
import matplotlib.pyplot as plt

# Data
dates = [
    '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
    '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10',
    '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14', '2024-01-15',
    '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20',
    '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', '2024-01-25',
    '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29', '2024-01-30'
]
view_counts = [
    2400, 2350, 2300, 2250, 2200, 2150, 2100, 2050, 2000, 1950,
    1900, 1850, 1800, 1750, 1700, 1650, 1600, 1550, 1500, 1450,
    1400, 1350, 1300, 1250, 1200, 1150, 1100, 1050, 1000, 950
]

plt.figure(figsize=(14, 8))
plt.plot(dates, view_counts, marker='o', color='#1E90FF', linewidth=2)

# Adding annotations for significant points
plt.annotate('Lowest View Count', xy=('2024-01-30', 950), xytext=('2024-01-29', 800),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))
plt.annotate('Highest View Count', xy=('2024-01-01', 2400), xytext=('2024-01-02', 2500),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05))

plt.title('Daily Stock Prices in January 2024', pad=20, fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Stock Price', fontsize=14)
plt.grid(True)

plt.xticks(rotation=45)
plt.gca().invert_yaxis()
plt.tight_layout()

plt.show()