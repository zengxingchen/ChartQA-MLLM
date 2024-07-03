
import matplotlib.pyplot as plt

# Data points
athletes = [
    'Lionel Messi', 'LeBron James', 'Serena Williams', 'Tom Brady', 'Roger Federer',
    'Cristiano Ronaldo', 'Usain Bolt', 'Simone Biles', 'Michael Phelps', 'Neymar',
    'Lewis Hamilton', 'Rafael Nadal', 'Stephen Curry', 'Tiger Woods', 'Novak Djokovic',
    'Kevin Durant', 'Virat Kohli', 'Floyd Mayweather', 'Kobe Bryant', 'Shaun White',
    'Manny Pacquiao', 'Conor McGregor'
]
average_salary = [
    75000000, 85000000, 40000000, 30000000, 70000000, 65000000, 25000000, 12000000,
    20000000, 75000000, 55000000, 50000000, 80000000, 45000000, 45000000, 60000000,
    25000000, 100000000, 25000000, 10000000, 20000000, 32000000
]
number_of_titles = [
    35, 29, 23, 20, 20, 33, 8, 32, 28, 27, 7, 20, 4, 15, 20, 4, 27, 50, 5, 3, 12, 22
]
popularity = [
    95, 98, 90, 85, 92, 97, 88, 87, 89, 94, 91, 93, 86, 80, 89, 87, 92, 99, 88, 70, 90, 85
]

# Bubble size is scaled by popularity
bubble_size = [pop * 10 for pop in popularity]

# Set the figure size
plt.figure(figsize=(16, 10))

# Create the scatter plot
plt.scatter(average_salary, number_of_titles, s=bubble_size,
            color=['#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF', '#5733FF', '#57FF33', '#F3FF33', '#33FFF3', '#FF3357', '#33FF3F', 
                   '#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF', '#5733FF', '#57FF33', '#F3FF33', '#33FFF3'],
            alpha=0.7, edgecolors='w', linewidth=2)

# Title and labels
plt.title('Average Annual Salary vs. Number of Titles Won by Famous Athletes')
plt.xlabel('Average Annual Salary ($)')
plt.ylabel('Number of Titles Won')

# Add athlete labels to the bubbles
for i, athlete in enumerate(athletes):
    plt.text(average_salary[i], number_of_titles[i], athlete, ha='center', va='center')

# Show plot
plt.show()