
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [10000, 12000, 14000, 13000, 15000, 17000, 16000, 18000, 19000, 21000, 20000, 22000]

# Changes to data to enrich visualization
revenue[4] += 2000  # May
revenue[-3] -= 2000  # October

# Modify color scheme with color codes, change figure size, change trend by adjusting the scores
plt.figure(figsize=(16, 9))
plt.plot(months, [rev - 1500 if i % 2 == 0 else rev + 1500 for i, rev in enumerate(revenue)], 
         color='#e74c3c', marker='o', linestyle='--')  # Adjusted trend with color code

# Adding labels with annotations
for i, (month, rev) in enumerate(zip(months, revenue)):
    adjusted_rev = rev - 1500 if i % 2 == 0 else rev + 1500
    plt.annotate(f'{rev}', (month, adjusted_rev), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Revenue of a Startup in 2023')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')

# Display chart
plt.show()