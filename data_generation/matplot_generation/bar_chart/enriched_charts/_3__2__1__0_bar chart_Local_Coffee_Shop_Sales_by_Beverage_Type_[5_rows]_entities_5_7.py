
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023, 2024, 2025,
    2026, 2027, 2028, 2029, 2030
]
campaigns = [
    5, 8, 11, 16, 14,
    21, 24, 29, 33, 30,
    38, 44, 49, 52, 58,
    63, 68, 72, 77, 82
]

# Plot configuration
plt.figure(figsize=(10, 16))
bars = plt.bar(years, campaigns, width=0.6, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1',
    '#A133FF', '#FF8C33', '#33FF8C', '#5733FF',
    '#FF5733', '#33FFA1', '#3357A1', '#FF33D4',
    '#A133A1', '#FFA133', '#33FFA1', '#5733A1',
    '#FFA133', '#33FFD4', '#FF5733', '#33FFA1'
])

# Axes labels and title
plt.ylabel('Number of Campaigns')
plt.xlabel('Year')
plt.title('Annual Mental Health Awareness Campaigns (2011-2030)', pad=20)

# Show the plot
plt.show()