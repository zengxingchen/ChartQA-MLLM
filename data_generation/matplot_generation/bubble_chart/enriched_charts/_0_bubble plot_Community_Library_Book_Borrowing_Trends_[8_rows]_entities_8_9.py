
import matplotlib.pyplot as plt

# Sample data for smartphone brands
data = {
    'Brand': ["Samsung", "Apple", "Huawei", "Xiaomi", "Oppo", "Vivo", "Motorola", "Nokia",
              "OnePlus", "Realme", "Google", "Sony", "LG", "HTC"],
    'Market Share': [20, 18, 15, 10, 9, 7, 5, 4, 3, 3, 2, 2, 1, 1],
    'Average Selling Price': [250, 750, 200, 150, 210, 160, 180, 100,
                              400, 130, 500, 300, 220, 190],
    'Customer Satisfaction Score': [80, 88, 75, 78, 74, 73, 70, 69,
                                    85, 76, 83, 79, 68, 65]
}

# Define size of the bubble to be proportional to the market share
size = [value * 10 for value in data['Market Share']]

plt.figure(figsize=(14, 8))  # Change width and height of the chart

# Create a scatter plot
scatter = plt.scatter(data['Average Selling Price'], data['Customer Satisfaction Score'], 
                      s=size, alpha=0.5, 
                      c=['#FF5733', '#33FF57', '#3357FF', '#FFF233', '#F333FF', '#33FFF2', '#A233FF',
                         '#FF333F', '#33FFA2', '#B2FF33', '#FF8333', '#33D2FF', '#4DFF33', '#FF3381'])

# Adding title and labels
plt.title('Smartphone Brand Market Share, Price, and Satisfaction')
plt.xlabel('Average Selling Price')
plt.ylabel('Customer Satisfaction Score')

# Adding annotations for each bubble
for index, brand in enumerate(data['Brand']):
    plt.text(data['Average Selling Price'][index], data['Customer Satisfaction Score'][index], 
             brand, fontsize=9, ha='center', va='center')

plt.grid(True)  # Adding a grid
plt.show()