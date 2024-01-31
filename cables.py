import heapq


def heap_sort(arr):
    heapq.heapify(arr)  # Перетворюємо список в піраміду (min heap)

    sorted_arr = []
    while arr:
        # Витягуємо найменший елемент і додаємо його до відсортованого списку
        smallest = heapq.heappop(arr)
        sorted_arr.append(smallest)

    return sorted_arr


def minimize_cable_costs(cables):
    sorted_cables = heap_sort(cables)

    total_cost = 0

    while len(sorted_cables) > 1:
        # Беремо два найкоротших кабелі і з'єднуємо їх
        shortest_cables = sorted_cables[:2]
        combined_length = sum(shortest_cables)

        # Додаємо витрати на з'єднання до загальних витрат
        total_cost += combined_length

        # Замінюємо два найкоротші кабелі на їхнє з'єднання
        sorted_cables = [combined_length] + sorted_cables[2:]

        # Знову сортуємо кабелі за зростанням довжини
        sorted_cables.sort()

    return total_cost


# Приклад використання
cables = [8, 4, 6, 12, 44, 1, 6]
result = minimize_cable_costs(cables)

print("Мінімальні витрати на об'єднання кабелів:", result)
