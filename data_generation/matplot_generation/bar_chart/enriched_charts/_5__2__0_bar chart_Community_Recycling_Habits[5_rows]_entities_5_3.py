
import matplotlib.pyplot as plt

# Data
movies = ['Avatar', 'Avengers', 'Titanic', 'Frozen', 'Inception', 'Joker', 'Toy Story', 'Lion King', 'Black Panther', 'Star Wars', 'Harry Potter', 'Spider-Man', 'Jurassic Park', 'Wonder Woman', 'The Matrix', 'Aladdin', 'Guardians of the Galaxy', 'Finding Nemo', 'Moana', 'Coco']
ticket_sales = [1200, 1450, 1300, 1150, 900, 1350, 1100, 1250, 1500, 1400, 1450, 1300, 1350, 1000, 1200, 1100, 950, 1050, 980, 1100]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1', '#FF8F33', '#33C4FF', '#FF33C4', '#FFC433', '#5733FF', '#FF3357', '#A1FF33', '#33FF8F', '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1']

# Figure size
plt.figure(figsize=(14, 8))

# Horizontal bar chart
plt.barh(movies, ticket_sales, color=colors, height=0.6)

# Labeling
plt.xlabel('Ticket Sales')
plt.title('Monthly Ticket Sales for Movies')

# Set y-axis limit
plt.xlim(900, 1600)

# Show and save plot
plt.tight_layout()
plt.show()