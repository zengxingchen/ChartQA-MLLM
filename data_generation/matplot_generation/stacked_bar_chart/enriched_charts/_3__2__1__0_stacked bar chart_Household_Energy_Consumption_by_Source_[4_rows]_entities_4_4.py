
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
netflix = [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000]
amazon_prime = [8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500]
hulu = [5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200]
disney_plus = [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100]

fig, ax = plt.subplots(figsize=(16, 10))

bar_width = 0.5

# Plotting data (changing direction of chart to vertical)
p1 = ax.bar(months, netflix, bar_width, color='#FF5733', label='Netflix')
p2 = ax.bar(months, amazon_prime, bar_width, bottom=netflix, color='#33FF57', label='Amazon Prime')
p3 = ax.bar(months, hulu, bar_width, bottom=[i+j for i,j in zip(netflix, amazon_prime)], color='#3357FF', label='Hulu')
p4 = ax.bar(months, disney_plus, bar_width, bottom=[i+j+k for i,j,k in zip(netflix, amazon_prime, hulu)], color='#FF33A1', label='Disney Plus')

ax.set_ylabel('Hours')
ax.set_title('Monthly Streaming Hours Comparison')
ax.set_xticks([i for i in range(len(months))])
ax.set_xticklabels(months, rotation=45, ha='right')
ax.legend()

# Add numerical labels to each bar segment
for i in range(len(months)):
    ax.text(i, netflix[i] / 2, str(netflix[i]), ha='center', va='center', color='white')
    ax.text(i, netflix[i] + amazon_prime[i] / 2, str(amazon_prime[i]), ha='center', va='center', color='white')
    ax.text(i, netflix[i] + amazon_prime[i] + hulu[i] / 2, str(hulu[i]), ha='center', va='center', color='white')
    ax.text(i, netflix[i] + amazon_prime[i] + hulu[i] + disney_plus[i] / 2, str(disney_plus[i]), ha='center', va='center', color='white')

plt.grid(which='major', linestyle='--', linewidth='0.5', color='black')
plt.show()