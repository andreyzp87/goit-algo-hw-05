def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0
    value = None

    while low <= high:
        count += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            value = arr[mid]

        # інакше x присутній на позиції і повертаємо його
        else:
            value = arr[mid]
            break

    # якщо елемент не знайдений
    return count, value


if __name__ == '__main__':
    arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    keys = [0.2, 0.63, 1.2]

    for key in keys:
        print(f'{key} - {binary_search(arr, key)}')

