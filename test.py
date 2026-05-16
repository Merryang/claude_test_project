import os
import json


def read_config(path):
    with open(path, "r") as f:
        data = json.loads(f.read())
    return data


def average(numbers):
    if not numbers:
        return 0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


def find_max_index(values):
    max_val = values[0]
    max_idx = 0
    for i in range(1, len(values)):
        if values[i] > max_val:
            max_val = values[i]
            max_idx = i
    return max_idx


def is_admin(user):
    if user["role"] == "admin":
        return True
    return False


def delete_temp_files(directory):
    for name in os.listdir(directory):
        if name.endswith(".tmp"):
            os.remove(os.path.join(directory, name))


def fetch_user(user_id, users):
    return users.get(user_id)


def password_equal(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


if __name__ == "__main__":
    print(average([]))
    print(find_max_index([3, 1, 4, 1, 5, 9, 2, 6]))
    print(append_item(1))
    print(append_item(2))
    print(is_admin({"role": "guest"}))
