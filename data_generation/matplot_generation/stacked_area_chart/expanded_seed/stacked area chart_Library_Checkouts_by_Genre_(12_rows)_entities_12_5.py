
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime

# Data provided
data = [
    {'Week': '2023-03-01 to 2023-03-07', 'Non-Fiction': 75, 'Fiction': 120, 'Young Adult': 60, "Children's Books": 89, 'Mystery': 45, 'Thriller': 66},
    {'Week': '2023-03-08 to 2023-03-14', 'Non-Fiction': 60, 'Fiction': 110, 'Young Adult': 55, "Children's Books": 85, 'Mystery': 50, 'Thriller': 70},
    # ... (other data points)
    {'Week': '2023-05-17 to 2023-05-23', 'Non-Fiction': 105, 'Fiction': 170, 'Young Adult': 100, "Children's Books": 140, 'Mystery': 85, 'Thriller': 95}
]

# Parsing the date ranges and taking the first date for plotting
dates = [datetime.datetime.strptime(w['Week'][:10], "%Y-%m-%d") for w in data]
x = date2num(dates) # Convert to Matplotlib's internal date format

# Extracting the data for the stacked area chart
non_fiction = [w['Non-Fiction'] for w in data]
fiction = [w['Fiction'] for w in data]
young_adult = [w['Young Adult'] for w in data]
children_books = [w["Children's Books"] for w in data]
mystery = [w['Mystery'] for w in data]
thriller = [w['Thriller'] for w in data]

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(x, non_fiction, fiction, young_adult, children_books, mystery, thriller, labels=['Non-Fiction', 'Fiction', 'Young Adult', "Children's Books", 'Mystery', 'Thriller'], alpha=0.8)

# Formatting the x-axis to show dates
ax.xaxis_date()
fig.autofmt_xdate() # Rotate date labels

# Adding titles and labels
plt.title('Book Sales by Genre Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Books Sold')

# Adding legend
plt.legend(loc='upper left')

# Show the plot
plt.show()