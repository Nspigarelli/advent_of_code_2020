def day_1(report):
    for i in report:
        for j in report[::-1]:
            if (2020 - i - j) in report:
                return i * j * report[report.index(2020 - i - j)]


def main():
    with open('input.txt') as file:
        report = [int(x) for x in (file.read().split('\n'))]
        print(day_1(sorted(report)))


if __name__ == '__main__':
    main()
