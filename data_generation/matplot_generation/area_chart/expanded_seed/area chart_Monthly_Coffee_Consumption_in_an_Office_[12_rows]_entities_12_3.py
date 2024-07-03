
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Given data
data = [
    {'Month': 'January', 'Coffee Cups': 350},
    {'Month': 'February', 'Coffee Cups': 320},
    {'Month': 'March', 'Coffee Cups': 380},
    {'Month': 'April', 'Coffee Cups': 370},
    {'Month': 'May', 'Coffee Cups': 420},
    {'Month': 'June', 'Coffee Cups': 400},
    {'Month': 'July', 'Coffee Cups': 390},
    {'Month': 'August', 'Coffee Cups': 410},
    {'Month': 'September', 'Coffee Cups': 430},
    {'Month': 'October', 'Coffee Cups': 450},
    {'Month': 'November', 'Coffee Cups': 440},
    {'Month': 'December', 'Coffee Cups': 470}
]

# Extracting the months and the corresponding coffee cup counts
months = [entry['Month'] for entry in data]
coffee_cups = [entry['Coffee Cups'] for entry in data]

# Creating an area chart
plt.fill_between(months, coffee_cups, color="skyblue", alpha=0.5)
plt.plot(months, coffee_cups, color="Slateblue", alpha=0.6, linewidth=2)

# Adding titles and labels
plt.title("Coffee Cups Consumption by Month")
plt.xlabel("Month")
plt.ylabel("Number of Coffee Cups")

# Customizing the x-axis to display all months properly
plt.xticks(months, rotation=45)

# Ensuring the y-axis starts at 0
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.ylim(ymin=0)

# Adding grid lines
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Adding data labels on each point
for i, txt in enumerate(coffee_cups):
    plt.annotate(txt, (months[i], coffee_cups[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Show the plot
plt.tight_layout()
plt.show()