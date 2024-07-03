
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Year': 2018, 'Age 0-12': 1200, 'Age 13-18': 800, 'Age 19-30': 900, 'Age 31-50': 1100, 'Age 51+': 950},
    {'Year': 2019, 'Age 0-12': 1250, 'Age 13-18': 850, 'Age 19-30': 950, 'Age 31-50': 1200, 'Age 51+': 1000},
    {'Year': 2020, 'Age 0-12': 800, 'Age 13-18': 600, 'Age 19-30': 700, 'Age 31-50': 900, 'Age 51+': 850},
    {'Year': 2021, 'Age 0-12': 1300, 'Age 13-18': 900, 'Age 19-30': 1000, 'Age 31-50': 1250, 'Age 51+': 1050},
    {'Year': 2022, 'Age 0-12': 1400, 'Age 13-18': 950, 'Age 19-30': 1100, 'Age 31-50': 1300, 'Age 51+': 1100}
]

# Extracting years and age group data
years = [item['Year'] for item in data]
age_0_12 = [item['Age 0-12'] for item in data]
age_13_18 = [item['Age 13-18'] for item in data]
age_19_30 = [item['Age 19-30'] for item in data]
age_31_50 = [item['Age 31-50'] for item in data]
age_51_plus = [item['Age 51+'] for item in data]

# Plotting area chart
fig, ax = plt.subplots(figsize=(10, 6))

ax.fill_between(years, age_0_12, color='skyblue', alpha=0.5, label='Age 0-12')
ax.fill_between(years, age_0_12, age_13_18, where=(age_13_18 >= age_0_12), facecolor='green', alpha=0.5, interpolate=True, label='Age 13-18')
ax.fill_between(years, age_13_18, age_19_30, where=(age_19_30 >= age_13_18), facecolor='yellow', alpha=0.5, interpolate=True, label='Age 19-30')
ax.fill_between(years, age_19_30, age_31_50, where=(age_31_50 >= age_19_30), facecolor='orange', alpha=0.5, interpolate=True, label='Age 31-50')
ax.fill_between(years, age_31_50, age_51_plus, where=(age_51_plus >= age_31_50), facecolor='red', alpha=0.5, interpolate=True, label='Age 51+')

# Adding titles and labels
ax.set_title("Population by Age Group Over Years", fontsize=16)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Population", fontsize=12)

# Customizing the grid lines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Adding legend
ax.legend(title="Age Groups")

# Show plot
plt.tight_layout()
plt.show()