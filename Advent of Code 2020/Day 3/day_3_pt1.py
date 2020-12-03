def day_3(grid):
    start_x = 0
    start_y = 0
    count = 0
    while True:
        if len(grid) - 1 < start_x:
            break
        if 30 < start_y:
            start_y -= 31
        if grid[start_x][start_y] == '#':
            count += 1
        start_x += 1
        start_y += 3
    return count


def main():
    with open('input.txt') as file:
        grid = file.read().split('\n')
        print(day_3(grid))


if __name__ == '__main__':
    main()
