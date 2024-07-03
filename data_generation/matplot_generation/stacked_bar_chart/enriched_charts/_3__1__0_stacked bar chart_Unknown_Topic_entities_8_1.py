
import matplotlib.pyplot as plt

# Data from the table
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 
            'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
ancient_art = [200, 250, 220, 270, 260, 280, 300, 290]
modern_art = [300, 350, 320, 380, 340, 360, 390, 370]
digital_art = [150, 180, 170, 190, 200, 210, 230, 220]
street_art = [100, 130, 120, 140, 160, 170, 180, 150]

# Stacked bar data preparation
bar_height = 0.5
indices = range(len(quarters))

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

ax.barh(indices, ancient_art, height=bar_height, color='#8dd3c7', label='Ancient Art')
ax.barh(indices, modern_art, height=bar_height, left=ancient_art, color='#ffffb3', label='Modern Art')
ax.barh(indices, digital_art, height=bar_height, left=[i+j for i,j in zip(ancient_art, modern_art)], color='#bebada', label='Digital Art')
ax.barh(indices, street_art, height=bar_height, left=[i+j+k for i,j,k in zip(ancient_art, modern_art, digital_art)], color='#fb8072', label='Street Art')

# Labels and Titles
ax.set_xlabel('Number of Art Pieces')
ax.set_title('Art Pieces by Category per Quarter', pad=20)
ax.set_yticks(indices)
ax.set_yticklabels(quarters)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Numerical labels
for i in range(len(quarters)):
    ax.text(ancient_art[i]/2, i, str(ancient_art[i]), va='center', ha='center', color='black')
    ax.text(ancient_art[i] + modern_art[i]/2, i, str(modern_art[i]), va='center', ha='center', color='black')
    ax.text(ancient_art[i] + modern_art[i] + digital_art[i]/2, i, str(digital_art[i]), va='center', ha='center', color='black')
    ax.text(ancient_art[i] + modern_art[i] + digital_art[i] + street_art[i]/2, i, str(street_art[i]), va='center', ha='center', color='black')

# Remove the spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Grid lines
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Show plot
plt.tight_layout()
plt.show()