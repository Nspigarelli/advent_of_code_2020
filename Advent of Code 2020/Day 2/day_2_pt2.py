def day_2(report):
    valid_passwords = 0
    for i in report:
        i = i.split(' ')
        letter_count = [(int(x) - 1) for x in i[0].split('-')]
        letter = i[1][0]
        password = i[2]
        if letter_count[1] <= len(password):
            if password[letter_count[0]] == letter or password[letter_count[1]] == letter:
                if password[letter_count[0]] == letter and password[letter_count[1]] == letter:
                    continue
                valid_passwords += 1

    return valid_passwords


def main():
    with open('input.txt') as file:
        report = file.read().split('\n')
        print(day_2(report))


if __name__ == '__main__':
    main()
