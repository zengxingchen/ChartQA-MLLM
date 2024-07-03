
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Given data in the form of a list of dictionaries
data = [
    {'Transportation Mode': 'Subway', 'Number of Passengers (Thousands)': 1200, 'Ticket Price (USD)': 1.25, 'Total Revenue (USD)': 1500},
    {'Transportation Mode': 'Bus', 'Number of Passengers (Thousands)': 900, 'Ticket Price (USD)': 1.0, 'Total Revenue (USD)': 900},
    {'Transportation Mode': 'Tram', 'Number of Passengers (Thousands)': 100, 'Ticket Price (USD)': 1.5, 'Total Revenue (USD)': 150},
    {'Transportation Mode': 'Commuter Train', 'Number of Passengers (Thousands)': 500, 'Ticket Price (USD)': 2.5, 'Total Revenue (USD)': 1250},
    {'Transportation Mode': 'Ferry', 'Number of Passengers (Thousands)': 150, 'Ticket Price (USD)': 3.5, 'Total Revenue (USD)': 525},
    {'Transportation Mode': 'Bike Share', 'Number of Passengers (Thousands)': 80, 'Ticket Price (USD)': 0.75, 'Total Revenue (USD)': 60},
    {'Transportation Mode': 'Rideshare', 'Number of Passengers (Thousands)': 50, 'Ticket Price (USD)': 4.0, 'Total Revenue (USD)': 200},
    {'Transportation Mode': 'Taxi', 'Number of Passengers (Thousands)': 40, 'Ticket Price (USD)': 3.0, 'Total Revenue (USD)': 120},
    {'Transportation Mode': 'Private Coach', 'Number of Passengers (Thousands)': 30, 'Ticket Price (USD)': 5.0, 'Total Revenue (USD)': 150},
    {'Transportation Mode': 'Scooter Share', 'Number of Passengers (Thousands)': 60, 'Ticket Price (USD)': 1.0, 'Total Revenue (USD)': 60},
    {'Transportation Mode': 'Car Share', 'Number of Passengers (Thousands)': 70, 'Ticket Price (USD)': 3.0, 'Total Revenue (USD)': 210},
    {'Transportation Mode': 'Airport Shuttle', 'Number of Passengers (Thousands)': 20, 'Ticket Price (USD)': 10.0, 'Total Revenue (USD)': 200}
]

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Create a treemap
sizes = df['Total Revenue (USD)'].values
labels = df.apply(lambda x: f"{x['Transportation Mode']}\n({x['Total Revenue (USD)']} USD)", axis=1)
color = plt.cm.coolwarm(df['Ticket Price (USD)'] / df['Ticket Price (USD)'].max())

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=color, alpha=0.8)
plt.axis('off')

# Add title and subtitle
plt.title('Treemap of Transportation Mode by Total Revenue', fontsize=18)
plt.suptitle('Size of each block corresponds to total revenue, color intensity corresponds to ticket price', fontsize=10)

# Show plot
plt.show()