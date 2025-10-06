# https://www.codewars.com/kata/5601409514fc93442500010b/train/python
def better_than_average(class_points, your_points):
    print(len(class_points))
    return your_points > sum(class_points) / len(class_points)

print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 55))
