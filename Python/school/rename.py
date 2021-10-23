import time

Array = ["0", "1", "2"]

print("Array 0 " + Array[0])
print("Array 1 " + Array[1])
print("Array 2 " + Array[2])


List = []
print("Blank list.")
print(List)

List.append("Index 0")
print(List[0])
print("List " + List[0])

List.clear()
print(List)

List.extend(["a", "e", "i", "o", "i", "u"])

List_count = List.count("i")
print(List_count)


def area(width, height):
    calc_area = width * height
    return calc_area


print(area(40, 40))


def add(a, b):
    calc_add = a + b
    return calc_add


print(add(2, 3))


def countto(start_no, interval, stop_at):
    i = int(start_no)
    while i < stop_at + 1:
        print(i)
        i += 1
        time.sleep(interval)


countto(0, 0.5, 20)
