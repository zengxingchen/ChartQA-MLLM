
import matplotlib.pyplot as plt

# Data for the stacked area chart
months = ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 'Jun-2021', 
          'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021', 'Nov-2021', 'Dec-2021',
          'Jan-2022', 'Feb-2022', 'Mar-2022', 'Apr-2022', 'May-2022', 'Jun-2022',
          'Jul-2022', 'Aug-2022', 'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022']
transport = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135,
             140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195]
energy = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 
          270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380]
industry = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 
            320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430]

# Modify the dimensions of the plot
plt.figure(figsize=(16, 10))

# Creating the stacked area chart
plt.stackplot(months, transport, energy, industry,
              colors=['#FF4500', '#1E90FF', '#228B22'],
              labels=['Transport', 'Energy', 'Industry'])

# Adding the legend
plt.legend(loc='upper left')

# Adding titles and labels
plt.title('Monthly Carbon Emissions by Sector', pad=30)
plt.xlabel('Month')
plt.ylabel('Emissions in Kilotons')

# Add annotation
for i, transport_val in enumerate(transport):
    total_emissions = transport_val + energy[i] + industry[i]
    plt.text(months[i], total_emissions, f'{total_emissions}', ha='center', va='bottom', fontsize=8)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()