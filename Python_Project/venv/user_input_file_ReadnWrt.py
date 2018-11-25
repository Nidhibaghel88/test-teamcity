def file_overwrite(filename, n):
    with open(filename, 'r+') as f:
        content = f.read()
        print(content)
        while True:
            feedback = input("Type 'y' to overwrite the file or 'n' to exit: ")
            if feedback.lower() == 'y':
                # move the file pointer back to the start and then truncate the file
                f.seek(0)
                f.truncate()
                break
            elif feedback.lower() == 'n':
                # return instantly, another advantage of using a function
                return
            else:
                print("Please enter either 'y' or 'n'.")

        print('Write {} lines to the file.'.format(n))
        lines = []
        for line_num in range(1, n + 1):
            line = input('line {}: '.format(line_num))
            lines.append(line)

        f.write('\n'.join(lines))
    with open(filename, 'r+') as f:
        content = f.read()
        print(content)

file_overwrite('C:/Users/nidhi.baghel/OneDrive - Shell/Documents/Python/venv/sample.txt', 3)

