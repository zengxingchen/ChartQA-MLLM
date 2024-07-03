
import matplotlib.pyplot as plt

# Data for the stacked area chart
months = ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 'Jun-2021', 
          'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021', 'Nov-2021', 'Dec-2021',
          'Jan-2022', 'Feb-2022', 'Mar-2022', 'Apr-2022', 'May-2022', 'Jun-2022',
          'Jul-2022', 'Aug-2022', 'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022']
technology = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220,
              230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340]
healthcare = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 
              270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380]
finance = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 
           320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430]

# Modify the dimensions of the plot
plt.figure(figsize=(14, 9))

# Creating the stacked area chart
plt.stackplot(months, technology, healthcare, finance,
              colors=['#FF6347', '#4682B4', '#32CD32'],
              labels=['Technology', 'Healthcare', 'Finance'])

# Adding the legend
plt.legend(loc='upper left')

# Adding titles and labels
plt.title('Monthly Revenues by Sector', pad=20)
plt.xlabel('Month')
plt.ylabel('Revenue in Thousands')

# Add annotation
for i, tech in enumerate(technology):
    total_revenue = tech + healthcare[i] + finance[i]
    plt.text(months[i], total_revenue, f'{total_revenue}', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()