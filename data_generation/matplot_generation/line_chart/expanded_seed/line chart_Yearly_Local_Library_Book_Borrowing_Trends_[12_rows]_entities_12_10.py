
import matplotlib.pyplot as plt

# Data from the chart table
data = [
    {'Year': 2010, 'Adult Fiction': 8700, 'Adult Non-Fiction': 6500, 'Young Adult': 3400, "Children's Books": 7800, 'Graphic Novels': 2900},
    {'Year': 2011, 'Adult Fiction': 8900, 'Adult Non-Fiction': 6700, 'Young Adult': 3550, "Children's Books": 8000, 'Graphic Novels': 3100},
    # ... add all the other years here
    {'Year': 2021, 'Adult Fiction': 10300, 'Adult Non-Fiction': 8000, 'Young Adult': 5000, "Children's Books": 9000, 'Graphic Novels': 5100}
]

# Parsing the data
years = [entry['Year'] for entry in data]
adult_fiction = [entry['Adult Fiction'] for entry in data]
adult_non_fiction = [entry['Adult Non-Fiction'] for entry in data]
young_adult = [entry['Young Adult'] for entry in data]
childrens_books = [entry["Children's Books"] for entry in data]
graphic_novels = [entry['Graphic Novels'] for entry in data]

# Plotting the data
plt.figure(figsize=(10, 6))

plt.plot(years, adult_fiction, color='blue', linestyle='-', marker='o', label='Adult Fiction')
plt.plot(years, adult_non_fiction, color='green', linestyle='--', marker='x', label='Adult Non-Fiction')
plt.plot(years, young_adult, color='red', linestyle=':', marker='s', label='Young Adult')
plt.plot(years, childrens_books, color='purple', linestyle='-.', marker='^', label="Children's Books")
plt.plot(years, graphic_novels, color='orange', linestyle='-', marker='d', label='Graphic Novels')

# Adding title and labels
plt.title('Book Sales Data from 2010 to 2021')
plt.xlabel('Year')
plt.ylabel('Units Sold')

# Add grid lines for better readability
plt.grid(True)

# Add a legend to the chart
plt.legend()

# Ensure the x-axis represents the years correctly and not as floating-point numbers
plt.xticks(years, [str(year) for year in years])

# Show the chart
plt.show()