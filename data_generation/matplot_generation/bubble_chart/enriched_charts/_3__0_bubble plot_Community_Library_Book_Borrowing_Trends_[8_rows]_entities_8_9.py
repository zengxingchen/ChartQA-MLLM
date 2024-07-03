
import matplotlib.pyplot as plt

data = {
    'Brand': ["Harvard", "Stanford", "MIT", "Oxford", "Cambridge", "Caltech", "ETH Zurich", 
              "Imperial College", "University of Chicago", "Columbia", "Princeton", "Yale", 
              "UCLA", "UC Berkeley"],
    'Research Funding': [500, 450, 400, 350, 300, 250, 200, 150, 100, 90, 80, 70, 60, 50],
    'Impact Factor': [9.8, 9.7, 9.6, 9.5, 9.4, 9.3, 9.2, 9.1, 9.0, 8.9, 8.8, 8.7, 8.6, 8.5],
    'Number of Publications': [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20]
}

size = [value * 10 for value in data['Number of Publications']]

plt.figure(figsize=(16, 10))

scatter = plt.scatter(data['Research Funding'], data['Impact Factor'], 
                      s=size, alpha=0.5, 
                      c=['#FF5733', '#33FF57', '#3357FF', '#FFF233', '#F333FF', '#33FFF2', 
                         '#A233FF', '#FF333F', '#33FFA2', '#B2FF33', '#FF8333', '#33D2FF', 
                         '#4DFF33', '#FF3381'])

plt.title('Top Universities Research Impact and Funding', pad=20)
plt.xlabel('Research Funding (in millions)')
plt.ylabel('Impact Factor')

for index, brand in enumerate(data['Brand']):
    plt.text(data['Research Funding'][index], data['Impact Factor'][index], 
             brand, fontsize=9, ha='center', va='center')

plt.grid(True)
plt.show()