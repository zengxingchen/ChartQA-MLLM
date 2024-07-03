
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Sample data provided
data = [
    {'Week': '2023-02-01 to 2023-02-07', 'New Memberships': 25, 'Books Loaned': 340, 'Audio Books Loaned': 45, 'E-books Downloaded': 120},
    {'Week': '2023-02-08 to 2023-02-14', 'New Memberships': 30, 'Books Loaned': 320, 'Audio Books Loaned': 55, 'E-books Downloaded': 110},
    {'Week': '2023-02-15 to 2023-02-21', 'New Memberships': 35, 'Books Loaned': 360, 'Audio Books Loaned': 40, 'E-books Downloaded': 150},
    {'Week': '2023-02-22 to 2023-02-28', 'New Memberships': 20, 'Books Loaned': 370, 'Audio Books Loaned': 58, 'E-books Downloaded': 170},
    {'Week': '2023-03-01 to 2023-03-07', 'New Memberships': 28, 'Books Loaned': 380, 'Audio Books Loaned': 60, 'E-books Downloaded': 180},
    {'Week': '2023-03-08 to 2023-03-14', 'New Memberships': 32, 'Books Loaned': 390, 'Audio Books Loaned': 63, 'E-books Downloaded': 175},
    {'Week': '2023-03-15 to 2023-03-21', 'New Memberships': 27, 'Books Loaned': 400, 'Audio Books Loaned': 70, 'E-books Downloaded': 190},
    {'Week': '2023-03-22 to 2023-03-28', 'New Memberships': 30, 'Books Loaned': 410, 'Audio Books Loaned': 75, 'E-books Downloaded': 200}
]

# Extract data for plotting
weeks = [i['Week'].split(' to ')[0] for i in data]  # Using the start of the week for plotting
dates = [datetime.strptime(w, '%Y-%m-%d') for w in weeks]
memberships = [i['New Memberships'] for i in data]
books_loaned = [i['Books Loaned'] for i in data]
audio_books_loaned = [i['Audio Books Loaned'] for i in data]
ebooks_downloaded = [i['E-books Downloaded'] for i in data]

# Set the locator for the x-axis to show each week date
locator = mdates.WeekdayLocator(byweekday=mdates.MO)
formatter = mdates.DateFormatter('%Y-%m-%d')

fig, ax = plt.subplots()

# Stackplot
ax.stackplot(dates, memberships, books_loaned, audio_books_loaned, ebooks_downloaded, labels=['New Memberships', 'Books Loaned', 'Audio Books Loaned', 'E-books Downloaded'])

# Formatting x-axis with the date
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

# Beautify the x-labels
plt.gcf().autofmt_xdate()

# Add labels and title
plt.title('Library Transactions by Week')
plt.xlabel('Week Starting')
plt.ylabel('Number of Transactions')

# Add legend
plt.legend(loc='upper left')

# Show plot
plt.tight_layout()
plt.show()