
import matplotlib.pyplot as plt

# Data
names = [
    "Michael Jordan", "Tiger Woods", "Cristiano Ronaldo", "LeBron James", "Lionel Messi",
    "Roger Federer", "Floyd Mayweather", "Serena Williams", "Tom Brady", "Usain Bolt",
    "Michael Schumacher", "Phil Mickelson", "David Beckham", "Kobe Bryant", 
    "Shaquille O'Neal", "Kevin Durant", "Neymar", "Maria Sharapova", "Simone Biles", "Rafael Nadal"
]
years_of_birth = [
    1963, 1975, 1985, 1984, 1987,
    1981, 1977, 1981, 1977, 1986,
    1969, 1970, 1975, 1978,
    1972, 1988, 1992, 1987, 1997, 1986
]
career_earnings = [
    1700, 1200, 1000, 1100, 1000,
    900, 1000, 300, 300, 150,
    1000, 950, 800, 600,
    700, 600, 500, 325, 100, 600
]

# Scatter plot
fig, ax = plt.subplots(figsize=(18, 10))
scatter = ax.scatter(
    years_of_birth,
    career_earnings,
    alpha=0.8,
    c=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF',
        '#FF8F33', '#33FF8F', '#8F33FF', '#FF3333', '#33FFF4',
        '#F433FF', '#33FFA4', '#FF8F8F', '#8FFF33', '#33A6FF',
        '#FF33D5', '#A6FF33', '#FF33A6', '#33FF77', '#7733FF'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Top Athletes: Year of Birth vs Career Earnings (in millions)', pad=20)
ax.set_xlabel('Year of Birth')
ax.set_ylabel('Career Earnings (in millions)')

# Adding the person names as labels next to each point
for i, name in enumerate(names):
    ax.annotate(name, (years_of_birth[i], career_earnings[i]), fontsize=8, ha='right')

plt.show()