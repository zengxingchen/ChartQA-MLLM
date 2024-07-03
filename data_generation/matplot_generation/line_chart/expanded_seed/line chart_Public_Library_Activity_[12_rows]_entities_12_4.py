
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Month': 'January', 'New Memberships': 150, 'Books Borrowed': 1200, 'eBook Downloads': 350, 'Library Visitations': 760},
    {'Month': 'February', 'New Memberships': 120, 'Books Borrowed': 1150, 'eBook Downloads': 330, 'Library Visitations': 670},
    {'Month': 'March', 'New Memberships': 180, 'Books Borrowed': 1300, 'eBook Downloads': 390, 'Library Visitations': 810},
    {'Month': 'April', 'New Memberships': 200, 'Books Borrowed': 1350, 'eBook Downloads': 400, 'Library Visitations': 880},
    {'Month': 'May', 'New Memberships': 190, 'Books Borrowed': 1400, 'eBook Downloads': 410, 'Library Visitations': 850},
    {'Month': 'June', 'New Memberships': 210, 'Books Borrowed': 1450, 'eBook Downloads': 420, 'Library Visitations': 900},
    {'Month': 'July', 'New Memberships': 230, 'Books Borrowed': 1550, 'eBook Downloads': 430, 'Library Visitations': 930},
    {'Month': 'August', 'New Memberships': 240, 'Books Borrowed': 1600, 'eBook Downloads': 440, 'Library Visitations': 970},
    {'Month': 'September', 'New Memberships': 205, 'Books Borrowed': 1500, 'eBook Downloads': 425, 'Library Visitations': 920},
    {'Month': 'October', 'New Memberships': 220, 'Books Borrowed': 1580, 'eBook Downloads': 415, 'Library Visitations': 890},
    {'Month': 'November', 'New Memberships': 180, 'Books Borrowed': 1470, 'eBook Downloads': 405, 'Library Visitations': 860},
    {'Month': 'December', 'New Memberships': 175, 'Books Borrowed': 1490, 'eBook Downloads': 410, 'Library Visitations': 940}
]

# Extracting the months and metrics
months = [entry['Month'] for entry in data]
new_memberships = [entry['New Memberships'] for entry in data]
books_borrowed = [entry['Books Borrowed'] for entry in data]
ebook_downloads = [entry['eBook Downloads'] for entry in data]
library_visitations = [entry['Library Visitations'] for entry in data]

# Plotting the lines with diversified visual encodings
plt.figure(figsize=(14, 8))

plt.plot(months, new_memberships, label='New Memberships', color='blue', linestyle='-', marker='o')
plt.plot(months, books_borrowed, label='Books Borrowed', color='green', linestyle='--', marker='s')
plt.plot(months, ebook_downloads, label='eBook Downloads', color='red', linestyle='-.', marker='^')
plt.plot(months, library_visitations, label='Library Visitations', color='purple', linestyle=':', marker='x')

# Adding titles and labels
plt.title('Library Statistics Over a Year', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Count', fontsize=14)

# Adding legend
plt.legend()

# Displaying the grid
plt.grid(True)

# Customizing axis ticks for better readability
plt.xticks(rotation=45)
plt.yticks(range(0, 1700, 100))

# Show plot
plt.tight_layout()
plt.show()