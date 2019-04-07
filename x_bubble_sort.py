

def bubble_sort(l: list) -> list:
    unsorted: list = l.copy()
    for x in unsorted:
        for idx, item in enumerate(unsorted):
            if idx == len(unsorted) - 1 or item <= unsorted[idx+1]:
                continue
            unsorted[idx], unsorted[idx+1] = unsorted[idx+1], unsorted[idx]
    return unsorted


def test_bubble_sort():
    test_case = [3, 5 , 1, 4, 2, 9, 0, 8, 1, -6]
    assert bubble_sort(test_case) == [-6, 0, 1, 1, 2, 3, 4, 5, 8, 9]
