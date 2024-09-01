import random

def approximate_pi():
    num_points = int(input("How many random points to generate? "))
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_approx = 4 * (inside_circle / num_points)
    print(f"Approximation of pi: {pi_approx:.5f}")

approximate_pi()
