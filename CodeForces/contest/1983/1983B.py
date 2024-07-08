from typing import List

def can_transform(grid_a: List[List[int]], grid_b: List[List[int]], rows: int, cols: int) -> bool:
    for row in range(rows - 1, 0, -1):
        for col in range(cols - 1, 0, -1):
            if grid_a[row][col] != grid_b[row][col]:
                diff = (grid_b[row][col] - grid_a[row][col] + 3) % 3
                grid_a[row][col] = grid_b[row][col]
                grid_a[row - 1][col] = (grid_a[row - 1][col] + 2 * diff) % 3
                grid_a[row][col - 1] = (grid_a[row][col - 1] + 2 * diff) % 3
                grid_a[row - 1][col - 1] = (grid_a[row - 1][col - 1] + diff) % 3

    for row in range(rows):
        if grid_a[row][0] != grid_b[row][0]:
            return False

    for col in range(cols):
        if grid_a[0][col] != grid_b[0][col]:
            return False

    return True

if __name__ == "__main__":
    test_cases = int(input())

    while test_cases:
        rows, cols = map(int, input().split())

        grid_a = [[int(input()) for _ in range(cols)] for _ in range(rows)]
        grid_b = [[int(input()) for _ in range(cols)] for _ in range(rows)]

        if can_transform(grid_a, grid_b, rows, cols):
            print("YES")
        else:
            print("NO")

        test_cases -= 1
