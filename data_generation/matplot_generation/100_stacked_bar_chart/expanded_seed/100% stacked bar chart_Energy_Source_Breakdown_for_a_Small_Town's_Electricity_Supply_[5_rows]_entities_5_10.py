
import matplotlib.pyplot as plt

# Data
data = [
    {'Year': 2016, 'Coal': '40%', 'Natural Gas': '30%', 'Nuclear': '20%', 'Renewables': '10%'},
    {'Year': 2017, 'Coal': '35%', 'Natural Gas': '30%', 'Nuclear': '25%', 'Renewables': '10%'},
    {'Year': 2018, 'Coal': '30%', 'Natural Gas': '35%', 'Nuclear': '25%', 'Renewables': '10%'},
    {'Year': 2019, 'Coal': '25%', 'Natural Gas': '40%', 'Nuclear': '20%', 'Renewables': '15%'},
    {'Year': 2020, 'Coal': '20%', 'Natural Gas': '40%', 'Nuclear': '20%', 'Renewables': '20%'}
]

# Extract years
years = [d['Year'] for d in data]

# Normalize data and convert to integer
for d in data:
    for key in d:
        if key != 'Year':
            # Remove % and convert to integer
            d[key] = int(d[key].rstrip('%'))

# Setup the values for each stack
coal = [d['Coal'] for d in data]
natural_gas = [d['Natural Gas'] for d in data]
nuclear = [d['Nuclear'] for d in data]
renewables = [d['Renewables'] for d in data]

# Create stacked bar chart
plt.figure(figsize=(10, 6))

plt.bar(years, coal, label='Coal', edgecolor='white')
plt.bar(years, natural_gas, bottom=coal, label='Natural Gas', edgecolor='white')
plt.bar(years, nuclear, bottom=[i+j for i,j in zip(coal, natural_gas)], label='Nuclear', edgecolor='white')
plt.bar(years, renewables, bottom=[i+j+k for i,j,k in zip(coal, natural_gas, nuclear)], label='Renewables', edgecolor='white')

# Customize the plot
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Energy Source Distribution Over Years')
plt.xticks(years)
plt.yticks(range(0, 101, 10))

# Create a legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1), title='Energy Sources')

# Annotate each stack with the percentage value
for i in range(len(years)):
    plt.text(years[i], coal[i]/2, f'{coal[i]}%', ha='center', va='center', color='white')
    plt.text(years[i], coal[i] + natural_gas[i]/2, f'{natural_gas[i]}%', ha='center', va='center', color='white')
    plt.text(years[i], coal[i] + natural_gas[i] + nuclear[i]/2, f'{nuclear[i]}%', ha='center', va='center', color='white')
    plt.text(years[i], coal[i] + natural_gas[i] + nuclear[i] + renewables[i]/2, f'{renewables[i]}%', ha='center', va='center', color='white')

# Tight layout to fit legend
plt.tight_layout()

# Show plot
plt.show()