
import matplotlib.pyplot as plt

data = [
    {'Day': 'Monday', 'Company A': 150, 'Company B': 160, 'Company C': 170, 'Company D': 180, 'Company E': 190},
    {'Day': 'Tuesday', 'Company A': 148, 'Company B': 162, 'Company C': 168, 'Company D': 182, 'Company E': 192},
    {'Day': 'Wednesday', 'Company A': 146, 'Company B': 164, 'Company C': 166, 'Company D': 184, 'Company E': 194},
    {'Day': 'Thursday', 'Company A': 144, 'Company B': 166, 'Company C': 164, 'Company D': 186, 'Company E': 196},
    {'Day': 'Friday', 'Company A': 142, 'Company B': 168, 'Company C': 162, 'Company D': 188, 'Company E': 198},
    {'Day': 'Saturday', 'Company A': 140, 'Company B': 170, 'Company C': 160, 'Company D': 190, 'Company E': 200},
    {'Day': 'Sunday', 'Company A': 138, 'Company B': 172, 'Company C': 158, 'Company D': 192, 'Company E': 202}
]

days = [item['Day'] for item in data]
company_a_prices = [item['Company A'] for item in data]
company_b_prices = [item['Company B'] for item in data]
company_c_prices = [item['Company C'] for item in data]
company_d_prices = [item['Company D'] for item in data]
company_e_prices = [item['Company E'] for item in data]

plt.figure(figsize=(12, 8))
plt.plot(days, company_a_prices, label='Company A', linestyle='-', marker='o', color='#1a75ff')
plt.plot(days, company_b_prices, label='Company B', linestyle='--', marker='s', color='#ff1a1a')
plt.plot(days, company_c_prices, label='Company C', linestyle='-.', marker='^', color='#33cc33')
plt.plot(days, company_d_prices, label='Company D', linestyle=':', marker='D', color='#ffcc00')
plt.plot(days, company_e_prices, label='Company E', linestyle='-', marker='*', color='#cc33ff')

plt.title('Weekly Stock Prices', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Stock Price ($)')
plt.legend(loc='lower left')

plt.grid(True, linestyle='--', linewidth=0.5, color='gray')

for i, txt in enumerate(company_d_prices):
    plt.annotate(txt, (days[i], company_d_prices[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()