import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def random_points(number_of_points, max_value):
    np.random.seed(2137)
    x = np.random.uniform(0, max_value, number_of_points)
    y = np.random.uniform(0, max_value, number_of_points)
    cites = pd.DataFrame({'X': x, 'Y': y})
    cites.index.name = 'City number'
    return cites

def generate_population(size):
    population = []
    for i in range(size):
        population.append(np.random.permutation(50))
    return population

def rate_population(population, cities_df):
    for i in range(len(population)):
        cities_df['population'] = population[i]
        cities_df.sort_values('population', ascending=False, inplace=True)
    return cities_df

def plot_points(x, y):
    fig = plt.figure(figsize=(10, 10))
    plt.scatter(x, y)
    plt.show()


cities_df = random_points(50, 300)
# plot_points(cities_df['X'], cities_df['Y'])
population = generate_population(5)
print(rate_population(population, cities_df))
#print(population)
#print(cities_df)
