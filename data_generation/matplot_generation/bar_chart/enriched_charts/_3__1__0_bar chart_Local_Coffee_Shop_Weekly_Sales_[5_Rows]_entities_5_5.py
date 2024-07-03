
import matplotlib.pyplot as plt

categories = [
    "Artificial Intelligence", "Quantum Computing", "Blockchain", 
    "Augmented Reality", "Robotics", "3D Printing", 
    "Nanotechnology", "Cybersecurity", "Biotechnology", 
    "Internet of Things", "Autonomous Vehicles"
]
percentages = [20.0, 15.0, 12.0, 10.0, 8.0, 7.0, 6.0, 10.0, 7.0, 5.0, 5.0]

plt.figure(figsize=(14, 8))

plt.barh(categories, percentages, color=[
    '#FF5733', '#3375FF', '#FFC300', '#8E33FF', 
    '#FF33AB', '#57C785', '#D733FF', '#4CAF50', 
    '#ADD45C', '#33FFDD', '#FF5733'], height=0.6)

plt.xlabel('Percentage of Interest', fontsize=14)
plt.title('Popularity of Emerging Technologies', fontsize=18)
plt.xlim(0, 25)

plt.tight_layout()
plt.show()