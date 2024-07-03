
import matplotlib.pyplot as plt

# Data
locations = ["Beach", "Museum", "Mountain", "Theme Park", "Zoo", 
             "Aquarium", "Historical Site", "National Park", "Botanical Garden", "Concert Hall", 
             "Cinema", "Art Gallery", "Festival", "Sports Event", "Market", 
             "Theatre", "Exhibition", "Food Fair", "Street Performance", "Library", 
             "Lecture", "Book Fair"]
research_projects = [15, 8, 12, 10, 6, 7, 9, 11, 5, 7, 
                     9, 8, 13, 14, 5, 6, 4, 10, 3, 2, 
                     4, 5]
average_funding = [50000, 20000, 70000, 80000, 30000, 25000, 40000, 60000, 35000, 55000, 
                   45000, 50000, 65000, 75000, 20000, 55000, 30000, 40000, 15000, 5000, 
                   10000, 25000]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(16, 12))

# Scatter plot
ax.scatter(research_projects, average_funding, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
                                                      "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", 
                                                      "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
                                                      "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", 
                                                      "#1f77b4", "#ff7f0e"])

# Title and labels
plt.title('Number of Research Projects vs. Average Funding in Various Locations', pad=20)
plt.xlabel('Number of Research Projects')
plt.ylabel('Average Funding ($)')

# Show plot
plt.show()