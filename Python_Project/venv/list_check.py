r = []
for c in 'this is a string with blanks':  #walks through string,char by char
    if c == ' ': continue                 #skip rest of block, continue loop
    r.append(c)
    a = ' '.join(r)
    print(a)




