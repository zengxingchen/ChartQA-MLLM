
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data provided
data = [
    {'Month': 'January', 'Library Visitors': 320, 'New Books Acquired': 50},
    {'Month': 'February', 'Library Visitors': 280, 'New Books Acquired': 45},
    {'Month': 'March', 'Library Visitors': 360, 'New Books Acquired': 60},
    {'Month': 'April', 'Library Visitors': 400, 'New Books Acquired': 70},
    {'Month': 'May', 'Library Visitors': 450, 'New Books Acquired': 65},
    {'Month': 'June', 'Library Visitors': 420, 'New Books Acquired': 50},
    {'Month': 'July', 'Library Visitors': 480, 'New Books Acquired': 75},
    {'Month': 'August', 'Library Visitors': 500, 'New Books Acquired': 80}
]

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(data=df, x='Month', y='Library Visitors', 
                          size='New Books Acquired', sizes=(50, 500), 
                          hue='Library Visitors', palette='coolwarm', 
                          style='Month', markers=True)

# Customize the axes and title
scatter.set_xticklabels(df['Month'], rotation=45)
scatter.set_title('Library Visitors & New Books Acquired (Monthly)')

# Show the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Show the plot
plt.show()