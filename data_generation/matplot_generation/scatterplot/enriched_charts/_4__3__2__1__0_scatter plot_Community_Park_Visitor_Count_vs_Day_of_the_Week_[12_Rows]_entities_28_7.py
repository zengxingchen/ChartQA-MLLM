
import matplotlib.pyplot as plt

# Data
technologies = [
    "Artificial Intelligence", "Blockchain", "Quantum Computing", "5G Technology",
    "Internet of Things (IoT)", "Virtual Reality", "Augmented Reality", "Autonomous Vehicles",
    "Edge Computing", "Cybersecurity", "Robotics", "3D Printing",
    "Nanotechnology", "Biotechnology", "Renewable Energy", "Space Exploration",
    "Smart Cities", "Digital Twins", "Drone Technology", "6G Technology"
]
release_years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031]
investments = [500, 700, 800, 1000, 1200, 1500, 1600, 1800, 2000, 2200, 2500, 2700, 2900, 3100, 3300, 3500, 3700, 3900, 4100, 4300]

# Scatter plot
fig, ax = plt.subplots(figsize=(16, 9))  # Change the width and height of the chart
scatter = ax.scatter(
    release_years,
    investments,
    alpha=0.8,
    c=[
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Future Technologies & Society: Investment Over the Years', pad=20)
ax.set_xlabel('Year')
ax.set_ylabel('Investment (in millions)')

# Adding the technology names as labels next to each point
for i, technology in enumerate(technologies):
    ax.annotate(technology, (release_years[i], investments[i]), fontsize=8, ha='right')

plt.show()