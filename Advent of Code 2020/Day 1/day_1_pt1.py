def day_1(report):
    for i in report:
        if (2020 - i) in report:
            return i * report[report.index(2020-i)]


def main():
    with open('input.txt') as file:
        report = [int(x) for x in (file.read().split('\n'))]
        print(day_1(sorted(report)))


if __name__ == '__main__':
    main()
