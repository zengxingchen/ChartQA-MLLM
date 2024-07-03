
import matplotlib.pyplot as plt

# Input data
data = [
    {'Year': 2019, 'Fiction': '40%', 'Non-Fiction': '25%', "Children's Literature": '20%', 'Biography': '10%', 'Science and Technology': '5%'},
    {'Year': 2020, 'Fiction': '35%', 'Non-Fiction': '30%', "Children's Literature": '20%', 'Biography': '10%', 'Science and Technology': '5%'},
    {'Year': 2021, 'Fiction': '45%', 'Non-Fiction': '20%', "Children's Literature": '25%', 'Biography': '5%', 'Science and Technology': '5%'},
    {'Year': 2022, 'Fiction': '50%', 'Non-Fiction': '25%', "Children's Literature": '15%', 'Biography': '5%', 'Science and Technology': '5%'}
]

# Prepare data
years = [d['Year'] for d in data]
fiction = [float(d['Fiction'].strip('%')) / 100 for d in data]
non_fiction = [float(d['Non-Fiction'].strip('%')) / 100 for d in data]
children_lit = [float(d["Children's Literature"].strip('%')) / 100 for d in data]
biography = [float(d['Biography'].strip('%')) / 100 for d in data]
sci_tech = [float(d['Science and Technology'].strip('%')) / 100 for d in data]

# Cumulative data for stacking
cumulative_non_fiction = [f + nf for f, nf in zip(fiction, non_fiction)]
cumulative_children_lit = [f + nf + cl for f, nf, cl in zip(fiction, non_fiction, children_lit)]
cumulative_biography = [f + nf + cl + b for f, nf, cl, b in zip(fiction, non_fiction, children_lit, biography)]
cumulative_sci_tech = [f + nf + cl + b + st for f, nf, cl, b, st in zip(fiction, non_fiction, children_lit, biography, sci_tech)]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
ax.bar(years, fiction, label='Fiction', color='skyblue')
ax.bar(years, non_fiction, label='Non-Fiction', color='orange', bottom=fiction)
ax.bar(years, children_lit, label="Children's Literature", color='lightgreen', bottom=cumulative_non_fiction)
ax.bar(years, biography, label='Biography', color='orchid', bottom=cumulative_children_lit)
ax.bar(years, sci_tech, label='Science and Technology', color='grey', bottom=cumulative_biography)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Year')
ax.set_ylabel('Distribution (%)')
ax.set_title('Book Genre Distribution Over Years (Stacked 100%)')
ax.set_xticks(years)
ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
ax.set_yticklabels(['0%', '25%', '50%', '75%', '100%'])
ax.legend()

# Display the percentages on the bars
for i, (fic, n_fic, chl, bio, sct) in enumerate(zip(fiction, non_fiction, children_lit, biography, sci_tech)):
    ax.text(years[i], fic / 2, f'{fic*100:.0f}%', ha='center', va='center', color='black')
    ax.text(years[i], fic + n_fic / 2, f'{n_fic*100:.0f}%', ha='center', va='center', color='black')
    ax.text(years[i], cumulative_non_fiction[i] + chl / 2, f'{chl*100:.0f}%', ha='center', va='center', color='black')
    ax.text(years[i], cumulative_children_lit[i] + bio / 2, f'{bio*100:.0f}%', ha='center', va='center', color='black')
    ax.text(years[i], cumulative_biography[i] + sct / 2, f'{sct*100:.0f}%', ha='center', va='center', color='white')

# Show plot
plt.tight_layout()
plt.show()