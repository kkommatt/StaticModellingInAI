import numpy as np

num_samples = 1000000

x = np.random.uniform(0, 4, num_samples)
y = np.random.uniform(-4, 4, num_samples)

condition1 = (-x <= y) & (y <= x)
condition2 = (2 * x <= x**2 + y**2) & (x**2 + y**2 <= 4 * x)

inside_figure = condition1 & condition2

bounding_box_area = 4 * 8

area_estimate = np.sum(inside_figure) / num_samples * bounding_box_area

print(f"Приблизна площа фігури: {area_estimate}")
