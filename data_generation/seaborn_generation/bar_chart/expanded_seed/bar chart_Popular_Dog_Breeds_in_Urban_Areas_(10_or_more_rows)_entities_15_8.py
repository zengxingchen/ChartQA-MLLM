
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = [
    {'Breed': 'Labrador Retriever', 'Number of Registrations': 1570},
    {'Breed': 'French Bulldog', 'Number of Registrations': 1452},
    {'Breed': 'German Shepherd', 'Number of Registrations': 1230},
    {'Breed': 'Golden Retriever', 'Number of Registrations': 1104},
    {'Breed': 'Bulldog', 'Number of Registrations': 957},
    {'Breed': 'Beagle', 'Number of Registrations': 850},
    {'Breed': 'Poodle', 'Number of Registrations': 711},
    {'Breed': 'Rottweiler', 'Number of Registrations': 630},
    {'Breed': 'Yorkshire Terrier', 'Number of Registrations': 571},
    {'Breed': 'Boxer', 'Number of Registrations': 465},
    {'Breed': 'Dachshund', 'Number of Registrations': 402},
    {'Breed': 'Siberian Husky', 'Number of Registrations': 359},
    {'Breed': 'Great Dane', 'Number of Registrations': 302},
    {'Breed': 'Doberman Pinscher', 'Number of Registrations': 276},
    {'Breed': 'Cavalier King Charles Spaniel', 'Number of Registrations': 258}
]

# Convert the data to a pandas DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the bar chart
plt.figure(figsize=(10, 8))
barplot = sns.barplot(
    data=df,
    x='Number of Registrations',
    y='Breed',
    palette='viridis',    # Using a different color palette for visual appeal
    edgecolor='black'     # Adding edgecolor for definition
)

# Adding the values to the bars
for i in barplot.patches:
    barplot.text(
        i.get_width(), 
        i.get_y() + i.get_height() / 2,
        f'{i.get_width()}', 
        va = 'center'
    )

# Set the title and labels
plt.title('Number of Dog Registrations by Breed', fontsize=16)
plt.xlabel('Number of Registrations', fontsize=14)
plt.ylabel('Dog Breed', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()