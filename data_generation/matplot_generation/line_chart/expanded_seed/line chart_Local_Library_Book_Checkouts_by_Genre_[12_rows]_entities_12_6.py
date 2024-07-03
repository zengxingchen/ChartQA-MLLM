
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Month': 'January', 'Mystery': 320, 'Romance': 286, 'Science Fiction': 165, 'Non-Fiction': 412, 'Biographies': 198},
    {'Month': 'February', 'Mystery': 305, 'Romance': 271, 'Science Fiction': 159, 'Non-Fiction': 390, 'Biographies': 185},
    {'Month': 'March', 'Mystery': 330, 'Romance': 295, 'Science Fiction': 175, 'Non-Fiction': 420, 'Biographies': 205},
    {'Month': 'April', 'Mystery': 350, 'Romance': 310, 'Science Fiction': 180, 'Non-Fiction': 430, 'Biographies': 215},
    {'Month': 'May', 'Mystery': 375, 'Romance': 320, 'Science Fiction': 190, 'Non-Fiction': 440, 'Biographies': 220},
    {'Month': 'June', 'Mystery': 360, 'Romance': 310, 'Science Fiction': 200, 'Non-Fiction': 450, 'Biographies': 230},
    {'Month': 'July', 'Mystery': 340, 'Romance': 305, 'Science Fiction': 210, 'Non-Fiction': 460, 'Biographies': 240},
    {'Month': 'August', 'Mystery': 355, 'Romance': 325, 'Science Fiction': 220, 'Non-Fiction': 470, 'Biographies': 235},
    {'Month': 'September', 'Mystery': 365, 'Romance': 330, 'Science Fiction': 230, 'Non-Fiction': 480, 'Biographies': 245},
    {'Month': 'October', 'Mystery': 380, 'Romance': 340, 'Science Fiction': 240, 'Non-Fiction': 490, 'Biographies': 250},
    {'Month': 'November', 'Mystery': 370, 'Romance': 335, 'Science Fiction': 235, 'Non-Fiction': 480, 'Biographies': 260},
    {'Month': 'December', 'Mystery': 390, 'Romance': 345, 'Science Fiction': 250, 'Non-Fiction': 500, 'Biographies': 270}
]

# Extracting months
months = [record['Month'] for record in data]

# Extracting data for each genre
mystery = [record['Mystery'] for record in data]
romance = [record['Romance'] for record in data]
science_fiction = [record['Science Fiction'] for record in data]
non_fiction = [record['Non-Fiction'] for record in data]
biographies = [record['Biographies'] for record in data]

# Start plotting
plt.figure(figsize=(12, 8))

# Plotting each genre
plt.plot(months, mystery, label='Mystery', marker='o', linestyle='-', color='blue')
plt.plot(months, romance, label='Romance', marker='X', linestyle='--', color='red')
plt.plot(months, science_fiction, label='Science Fiction', marker='^', linestyle='-.', color='green')
plt.plot(months, non_fiction, label='Non-Fiction', marker='s', linestyle=':', color='purple')
plt.plot(months, biographies, label='Biographies', marker='D', linestyle='-', color='orange')

# Adding titles and labels
plt.title('Monthly Sales by Genre')
plt.xlabel('Month')
plt.ylabel('Sales')

# Add a legend
plt.legend()

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()