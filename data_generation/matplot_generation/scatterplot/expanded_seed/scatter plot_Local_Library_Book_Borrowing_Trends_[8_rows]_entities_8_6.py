
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Genre': 'Week1', 'Mystery': 47, 'Romance': 53, 'Science Fiction': 29, 'Non-Fiction': 34, 'Biography': 20},
    {'Genre': 'Week2', 'Mystery': 52, 'Romance': 48, 'Science Fiction': 35, 'Non-Fiction': 30, 'Biography': 25},
    {'Genre': 'Week3', 'Mystery': 49, 'Romance': 60, 'Science Fiction': 32, 'Non-Fiction': 27, 'Biography': 19},
    {'Genre': 'Week4', 'Mystery': 45, 'Romance': 55, 'Science Fiction': 28, 'Non-Fiction': 44, 'Biography': 24},
    {'Genre': 'Week5', 'Mystery': 50, 'Romance': 62, 'Science Fiction': 33, 'Non-Fiction': 31, 'Biography': 18},
    {'Genre': 'Week6', 'Mystery': 55, 'Romance': 59, 'Science Fiction': 37, 'Non-Fiction': 45, 'Biography': 21},
    {'Genre': 'Week7', 'Mystery': 53, 'Romance': 58, 'Science Fiction': 39, 'Non-Fiction': 50, 'Biography': 23},
    {'Genre': 'Week8', 'Mystery': 60, 'Romance': 64, 'Science Fiction': 41, 'Non-Fiction': 48, 'Biography': 22}
]

# Preparing the data for plotting
weeks = [d['Genre'].replace('Week', '') for d in data]
mystery = [d['Mystery'] for d in data]
romance = [d['Romance'] for d in data]
science_fiction = [d['Science Fiction'] for d in data]
non_fiction = [d['Non-Fiction'] for d in data]
biography = [d['Biography'] for d in data]

# Plotting the data
plt.scatter(weeks, mystery, color='blue', marker='o', label='Mystery')
plt.scatter(weeks, romance, color='red', marker='s', label='Romance')
plt.scatter(weeks, science_fiction, color='green', marker='^', label='Science Fiction')
plt.scatter(weeks, non_fiction, color='purple', marker='*', label='Non-Fiction')
plt.scatter(weeks, biography, color='orange', marker='x', label='Biography')

# Adding title and labels
plt.title('Book Sales Over 8 Weeks by Genre')
plt.xlabel('Weeks')
plt.ylabel('Sales Count')
plt.legend()

# Showing the plot
plt.show()