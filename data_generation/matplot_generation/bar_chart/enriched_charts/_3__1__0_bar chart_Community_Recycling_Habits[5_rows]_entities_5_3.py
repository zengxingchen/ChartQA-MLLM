
import matplotlib.pyplot as plt

programming_languages = ['Python', 'JavaScript', 'Java', 'C#', 'PHP', 'C++', 'TypeScript', 'Swift', 'Kotlin', 'Go', 'Rust', 'Ruby', 'Objective-C', 'Scala', 'Perl', 'Dart', 'Elixir', 'Clojure', 'Haskell', 'Lua']
popularity = [8500, 7800, 6200, 5000, 4500, 4300, 3900, 3600, 3400, 3200, 3100, 2900, 2700, 2600, 2400, 2300, 2200, 2100, 2000, 1900]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFF5', '#FF9933', '#99FF33', '#33FF99', '#5733FF', '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFF5', '#FF9933', '#99FF33', '#33FF99', '#5733FF']

plt.figure(figsize=(14, 8))

plt.barh(programming_languages, popularity, color=colors, height=0.6)

plt.xlabel('Popularity (in millions)')
plt.title('Popularity of Programming Languages in 2024')
plt.tight_layout()
plt.show()