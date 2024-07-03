
import matplotlib.pyplot as plt

# Define data
companies = [
    "Amazon", "Apple", "Microsoft", "Alphabet", "Facebook", "Tesla",
    "Berkshire Hathaway", "Tencent", "Alibaba", "Samsung", "Visa",
    "Johnson & Johnson", "Walmart", "Procter & Gamble", "Nestle", 
    "Pfizer", "Intel", "Cisco", "PepsiCo", "Adobe"
]

revenue = [
    469822, 365817, 168088, 257637, 117929, 53823, 276094, 85842,
    109480, 200734, 24111, 94348, 559151, 76118, 95256, 41908,
    77367, 49601, 70372, 15655
]

employees = [
    1600000, 147000, 181000, 135301, 58604, 70757, 360000, 94000,
    251462, 287439, 21000, 134500, 2200000, 101000, 273000, 78000,
    110600, 77500, 291000, 24500
]

market_cap = [
    1630000, 2745000, 2310000, 1820000, 1050000, 758900, 632000,
    656000, 587000, 510000, 503000, 428000, 392000, 382000, 347000,
    314000, 225000, 224000, 213000, 301000
]

revenue_growth = [
    22, 16, 18, 23, 37, 71, 6, 20, 22, 9, 10, 10, 7, 5, 8, 2, 8, 1, 12, 24
]

# Create a figure with specified width and height
fig, ax = plt.subplots(figsize=(18, 12))

# Bubble sizes as a fraction of market_cap (adjust the scaling as needed)
sizes = [market_cap[i] / 20000 for i in range(len(market_cap))]

# Scatter plot (using revenue as weight for bubble size)
scatter = ax.scatter(
    revenue, employees, s=sizes, alpha=0.6,
    color=['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3333',
           '#FF33FF', '#57FFC8', '#FFC857', '#33FFFA', '#DD33FF',
           '#3FFFA5', '#A53FFF', '#3FA5FF', '#FFA53F', '#FF3FA5',
           '#33A1FF', '#FF5733', '#33FF57', '#3357FF', '#57FF33']
)

# Customize the appearance
ax.set_title('Top Global Companies: Revenue, Employees, Market Cap, and Revenue Growth')
ax.set_xlabel('Revenue (millions $)')
ax.set_ylabel('Number of Employees')
ax.grid(True)

# Adding the names of the companies to the bubbles
for i, txt in enumerate(companies):
    ax.annotate(txt, (revenue[i], employees[i]))

plt.show()