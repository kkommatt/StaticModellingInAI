import numpy as np

num_samples = 1000000

x = np.random.uniform(-1, 1, num_samples)
y = np.random.uniform(-1, 1, num_samples)
z = np.random.uniform(-1, 1, num_samples)

inside_cylinder1 = x**2 + y**2 <= 1
inside_cylinder2 = x**2 + z**2 <= 1

inside_intersection = inside_cylinder1 & inside_cylinder2

bounding_box_volume = 2 * 2 * 2

volume_estimate = np.sum(inside_intersection) / num_samples * bounding_box_volume

print(f"Приблизний об'єм: {volume_estimate}")
