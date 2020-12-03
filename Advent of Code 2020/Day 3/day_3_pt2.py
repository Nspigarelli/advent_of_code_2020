def day_3(grid, slopes):
    count_list = 1
    for y, x in slopes:
        count = 0
        start_x = 0
        start_y = 0
        while True:
            if len(grid) - 1 < start_x:
                count_list *= count
                break
            if 30 < start_y:
                start_y -= 31
            if grid[start_x][start_y] == '#':
                count += 1
            start_x += x
            start_y += y
    return count_list


def main():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    with open('input.txt') as file:
        grid = file.read().split('\n')
        print(day_3(grid, slopes))


if __name__ == '__main__':
    main()
