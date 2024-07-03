import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
electricity_usage = [320, 310, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200]

plt.figure(figsize=(16, 8))

plt.plot(months, electricity_usage, marker='s', linestyle='--', color='#1E90FF')  # Dodger Blue color

for i, usage in enumerate(electricity_usage):
    plt.annotate(str(usage), xy=(months[i], usage), xytext=(5, -10), textcoords='offset points')

plt.title('Monthly Electricity Usage (kWh)', pad=20)
plt.xlabel('Month')
plt.ylabel('Electricity Usage (kWh)')

plt.show()