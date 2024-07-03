
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Number of Books Read': 5, 'Knowledge Score': 70},
    {'Date': '2023-03-02', 'Number of Books Read': 7, 'Knowledge Score': 75},
    {'Date': '2023-03-03', 'Number of Books Read': 6, 'Knowledge Score': 72},
    {'Date': '2023-03-04', 'Number of Books Read': 8, 'Knowledge Score': 78},
    {'Date': '2023-03-05', 'Number of Books Read': 5, 'Knowledge Score': 70},
    {'Date': '2023-03-06', 'Number of Books Read': 9, 'Knowledge Score': 80},
    {'Date': '2023-03-07', 'Number of Books Read': 4, 'Knowledge Score': 68},
    {'Date': '2023-03-08', 'Number of Books Read': 10, 'Knowledge Score': 82},
    {'Date': '2023-03-09', 'Number of Books Read': 6, 'Knowledge Score': 74},
    {'Date': '2023-03-10', 'Number of Books Read': 7, 'Knowledge Score': 76},
    {'Date': '2023-03-11', 'Number of Books Read': 5, 'Knowledge Score': 70},
    {'Date': '2023-03-12', 'Number of Books Read': 8, 'Knowledge Score': 78},
    {'Date': '2023-03-13', 'Number of Books Read': 4, 'Knowledge Score': 68},
    {'Date': '2023-03-14', 'Number of Books Read': 9, 'Knowledge Score': 80}
]

# Extracting data for plotting
dates = [datetime.strptime(item['Date'], '%Y-%m-%d') for item in data]
books_read = [item['Number of Books Read'] for item in data]
knowledge_score = [item['Knowledge Score'] for item in data]

# Setting up the plot
plt.figure(figsize=(16, 10))

# Plotting both number of books read and knowledge score
plt.plot(dates, books_read, marker='o', linestyle='-', color='#1E90FF', label='Number of Books Read')
plt.plot(dates, knowledge_score, marker='s', linestyle='--', color='#32CD32', label='Knowledge Score')

# Formatting the x-axis to show dates clearly
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Adding some aesthetics
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Daily Books Read and Knowledge Score Over Two Weeks', pad=20)
plt.legend(loc='upper left')
plt.grid(True)

# Rotating the date labels for better readability
plt.gcf().autofmt_xdate()

# Adding annotations
for i, txt in enumerate(books_read):
    plt.annotate(txt, (dates[i], books_read[i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(knowledge_score):
    plt.annotate(txt, (dates[i], knowledge_score[i]), textcoords="offset points", xytext=(0,-15), ha='center', color='#32CD32')

# To show the plot
plt.show()