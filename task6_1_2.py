import numpy as np

num_samples = 1000000

x = np.random.uniform(-1, 1, num_samples)
y = np.random.uniform(-1, 2, num_samples)

inside_figure = x**2 + (y - np.sqrt(np.abs(x)))**2 <= 1

bounding_box_area = 2 * 3

area_estimate = np.sum(inside_figure) / num_samples * bounding_box_area

print(f"Приблизна площа фігури: {area_estimate}")
