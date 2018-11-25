with open('C:/Users/nidhi.baghel/OneDrive - Shell/Documents/Python/venv/sample.txt', 'w') as bb:
    bb.write('1')
    bb.write('\n')
    bb.write('Nidhi is a good girl')

    print("Writing is done now reading the file \n")

with open('C:/Users/nidhi.baghel/OneDrive - Shell/Documents/Python/venv/sample.txt') as bb:
    content = bb.read()
    print(content)


# Appending the data

with open('C:/Users/nidhi.baghel/OneDrive - Shell/Documents/Python/venv/sample.txt', 'a') as bb:
    bb.write('\n Vinit is a good boy ---- >This line is appended')

with open('C:/Users/nidhi.baghel/OneDrive - Shell/Documents/Python/venv/sample.txt') as bb:
    content = bb.read()
    print(content)
