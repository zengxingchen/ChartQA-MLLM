
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Company A': 1200, 'Company B': 1100, 'Company C': 1050, 'Company D': 980, 'Company E': 950},
    {'Month': 'February', 'Company A': 1180, 'Company B': 1090, 'Company C': 1030, 'Company D': 970, 'Company E': 940},
    {'Month': 'March', 'Company A': 1160, 'Company B': 1075, 'Company C': 1010, 'Company D': 960, 'Company E': 930},
    {'Month': 'April', 'Company A': 1140, 'Company B': 1060, 'Company C': 990, 'Company D': 950, 'Company E': 920},
    {'Month': 'May', 'Company A': 1120, 'Company B': 1045, 'Company C': 970, 'Company D': 940, 'Company E': 910},
    {'Month': 'June', 'Company A': 1100, 'Company B': 1030, 'Company C': 950, 'Company D': 930, 'Company E': 900},
    {'Month': 'July', 'Company A': 1080, 'Company B': 1015, 'Company C': 930, 'Company D': 920, 'Company E': 890},
    {'Month': 'August', 'Company A': 1060, 'Company B': 1000, 'Company C': 910, 'Company D': 910, 'Company E': 880},
    {'Month': 'September', 'Company A': 1040, 'Company B': 985, 'Company C': 890, 'Company D': 900, 'Company E': 870},
    {'Month': 'October', 'Company A': 1020, 'Company B': 970, 'Company C': 870, 'Company D': 890, 'Company E': 860},
    {'Month': 'November', 'Company A': 1000, 'Company B': 955, 'Company C': 850, 'Company D': 880, 'Company E': 850},
    {'Month': 'December', 'Company A': 980, 'Company B': 940, 'Company C': 830, 'Company D': 870, 'Company E': 840}
]

months = [record['Month'] for record in data]
company_a = [record['Company A'] for record in data]
company_b = [record['Company B'] for record in data]
company_c = [record['Company C'] for record in data]
company_d = [record['Company D'] for record in data]
company_e = [record['Company E'] for record in data]

plt.figure(figsize=(14, 8))

plt.plot(months, company_a, label='Company A', marker='o', linestyle='-', color='#FF5733')
plt.plot(months, company_b, label='Company B', marker='X', linestyle='--', color='#33FF57')
plt.plot(months, company_c, label='Company C', marker='^', linestyle='-.', color='#3357FF')
plt.plot(months, company_d, label='Company D', marker='s', linestyle=':', color='#FF33A1')
plt.plot(months, company_e, label='Company E', marker='D', linestyle='-', color='#FFA533')

plt.title('Monthly Stock Prices for Tech Companies', pad=20)
plt.xlabel('Month')
plt.ylabel('Stock Price (in USD)')
plt.gca().invert_yaxis()
plt.legend(loc='upper right')

plt.annotate('Highest Price', xy=('January', 1200), xytext=('February', 1220),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.show()