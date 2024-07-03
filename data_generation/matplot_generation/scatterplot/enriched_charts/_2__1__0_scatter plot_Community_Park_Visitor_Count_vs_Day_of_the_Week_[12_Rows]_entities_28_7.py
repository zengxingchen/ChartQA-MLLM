
import matplotlib.pyplot as plt

# Data
persons = [
    "Elon Musk", "Jeff Bezos", "Bernard Arnault", "Bill Gates", "Mark Zuckerberg",
    "Warren Buffett", "Larry Ellison", "Larry Page", "Sergey Brin", "Mukesh Ambani",
    "Steve Ballmer", "Carlos Slim", "Francoise Bettencourt Meyers", "Amancio Ortega", 
    "Michael Bloomberg", "Jim Walton", "Alice Walton", "Rob Walton", "MacKenzie Scott", 
    "Phil Knight"
]
years_of_birth = [1971, 1964, 1949, 1955, 1984, 1930, 1944, 1973, 1973, 1957, 1956, 1940, 1953, 1936, 1942, 1948, 1949, 1944, 1970, 1938]
net_worths = [219, 177, 158, 129, 118, 111, 106, 103, 100, 94, 93, 86, 85, 75, 70, 66, 65, 64, 62, 60]

# Scatter plot
fig, ax = plt.subplots(figsize=(16, 9))  # Change the width and height of the chart
scatter = ax.scatter(
    years_of_birth,
    net_worths,
    alpha=0.8,
    c=[
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
        '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Billionaires: Year of Birth vs Net Worth', pad=20)
ax.set_xlabel('Year of Birth')
ax.set_ylabel('Net Worth (in billions)')

# Adding the person names as labels next to each point
for i, person in enumerate(persons):
    ax.annotate(person, (years_of_birth[i], net_worths[i]), fontsize=8, ha='right')

plt.show()