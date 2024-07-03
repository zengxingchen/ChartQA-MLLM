
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for creating the treemap
data = {
    'Event': ['Jazz Festival', 'Rock Concert', 'Opera Night', 'Ballet Performance', 'Theater Play',
              'Comedy Show', 'Magic Show', 'Classical Music Concert', 'Hip Hop Battle', 'Art Exhibition',
              'Poetry Slam', 'Street Performance', 'Circus', 'Dance Competition', 'Film Screening',
              'Puppet Show', 'Mime Show', 'Improvisation Theater', 'Carnival Parade', 'Flash Mob'],
    'Attendance': [15000, 35000, 12000, 8000, 20000, 
                   17000, 11000, 22000, 14000, 18000,
                   9000, 7000, 16000, 13000, 19000,
                   6000, 5000, 10000, 30000, 2500]
}

# Convert the data dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Define size of the figure
plt.figure(figsize=(14,10))

# Define custom colors using specific color codes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
          '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5']

# Create the treemap
squarify.plot(sizes=df['Attendance'], label=df['Event'], color=colors, alpha=0.8)

# Set the title of the treemap
plt.title('Event Attendance in the Music & Performing Arts Sector')

# Remove the axis lines
plt.axis('off')

# Display the treemap
plt.show()