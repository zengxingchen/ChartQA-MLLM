
import matplotlib.pyplot as plt
import numpy as np

# Data from the provided table
data = [
    {'Month': 'January', 'Visits': 400, "Children's Books Loans": 350, 'Novels Loans': 300, 'Non-Fiction Books Loans': 200, 'E-books Downloads': 150},
    {'Month': 'February', 'Visits': 370, "Children's Books Loans": 320, 'Novels Loans': 280, 'Non-Fiction Books Loans': 190, 'E-books Downloads': 160},
    {'Month': 'March', 'Visits': 450, "Children's Books Loans": 400, 'Novels Loans': 350, 'Non-Fiction Books Loans': 210, 'E-books Downloads': 170},
    {'Month': 'April', 'Visits': 420, "Children's Books Loans": 380, 'Novels Loans': 330, 'Non-Fiction Books Loans': 220, 'E-books Downloads': 175},
    {'Month': 'May', 'Visits': 480, "Children's Books Loans": 450, 'Novels Loans': 370, 'Non-Fiction Books Loans': 230, 'E-books Downloads': 180},
    {'Month': 'June', 'Visits': 500, "Children's Books Loans": 480, 'Novels Loans': 390, 'Non-Fiction Books Loans': 240, 'E-books Downloads': 185},
    {'Month': 'July', 'Visits': 520, "Children's Books Loans": 510, 'Novels Loans': 410, 'Non-Fiction Books Loans': 250, 'E-books Downloads': 190},
    {'Month': 'August', 'Visits': 530, "Children's Books Loans": 520, 'Novels Loans': 420, 'Non-Fiction Books Loans': 260, 'E-books Downloads': 195},
    {'Month': 'September', 'Visits': 490, "Children's Books Loans": 470, 'Novels Loans': 400, 'Non-Fiction Books Loans': 250, 'E-books Downloads': 180},
    {'Month': 'October', 'Visits': 470, "Children's Books Loans": 440, 'Novels Loans': 380, 'Non-Fiction Books Loans': 240, 'E-books Downloads': 175},
    {'Month': 'November', 'Visits': 450, "Children's Books Loans": 420, 'Novels Loans': 360, 'Non-Fiction Books Loans': 230, 'E-books Downloads': 170},
    {'Month': 'December', 'Visits': 480, "Children's Books Loans": 460, 'Novels Loans': 390, 'Non-Fiction Books Loans': 240, 'E-books Downloads': 180}
]

# Extract month names for the x-axis
months = [entry['Month'] for entry in data]

# Stacking data
childrens_books_loans = np.array([entry["Children's Books Loans"] for entry in data])
novels_loans = np.array([entry['Novels Loans'] for entry in data])
non_fiction_books_loans = np.array([entry['Non-Fiction Books Loans'] for entry in data])
e_books_downloads = np.array([entry['E-books Downloads'] for entry in data])

# Define the bar width
bar_width = 0.5

# Setting index for each month
index = np.arange(len(months))

# Plotting data
plt.figure(figsize=(15, 8))

plt.bar(index, childrens_books_loans, bar_width, label="Children's Books", color='lightblue')
plt.bar(index, novels_loans, bar_width, bottom=childrens_books_loans, label='Novels', color='salmon')
plt.bar(index, non_fiction_books_loans, bar_width, bottom=childrens_books_loans + novels_loans, label='Non-Fiction Books', color='lightgreen')
plt.bar(index, e_books_downloads, bar_width, bottom=childrens_books_loans + novels_loans + non_fiction_books_loans, label='E-books Downloads', color='plum')

# Adding the xticks, title, legend and labels
plt.xticks(index, months, rotation=45, ha="right")
plt.xlabel('Month')
plt.ylabel('Total Number')
plt.title('Library Usage Statistics by Month')
plt.legend()

# Display numbers on the bars
for i in range(len(index)):
    plt.text(i, childrens_books_loans[i] + novels_loans[i] + non_fiction_books_loans[i] + e_books_downloads[i] + 10, f"{data[i]['Visits']} visits", ha='center', color='black')

# Display the plot
plt.tight_layout()
plt.show()