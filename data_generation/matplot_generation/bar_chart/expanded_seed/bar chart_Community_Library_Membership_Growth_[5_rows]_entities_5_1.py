
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2017, 'Adult Members': 1200, 'Youth Members': 800},
    {'Year': 2018, 'Adult Members': 1350, 'Youth Members': 850},
    {'Year': 2019, 'Adult Members': 1400, 'Youth Members': 900},
    {'Year': 2020, 'Adult Members': 1500, 'Youth Members': 950},
    {'Year': 2021, 'Adult Members': 1600, 'Youth Members': 1000}
]

# Extracting data for plotting
years = [item['Year'] for item in data]
adult_members = [item['Adult Members'] for item in data]
youth_members = [item['Youth Members'] for item in data]

# X locations for the groups
ind = range(len(years))  

# Bar width
width = 0.35       

# Plotting the bars
fig, ax = plt.subplots()

# Creating bars for adult members
adult_bars = ax.bar(ind, adult_members, width, label='Adult Members', color='grey')

# Creating bars for youth members, with an offset of 'width' to put them next to the adult bars
youth_bars = ax.bar([i+width for i in ind], youth_members, width, label='Youth Members', color='lightblue')

# Adding labels, title, and legend
ax.set_xlabel('Year')
ax.set_ylabel('Number of Members')
ax.set_title('Membership by year and group')
ax.set_xticks([i + width / 2 for i in ind])
ax.set_xticklabels(years)
ax.legend()

# Adding value labels on top of the bars
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
        
add_value_labels(adult_bars)
add_value_labels(youth_bars)

# Finally, show the plot
plt.show()