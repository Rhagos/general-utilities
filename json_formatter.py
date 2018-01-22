from __future__ import print_function
import sys

with open(sys.argv[1], 'r') as readfile:
    with open(sys.argv[1][:-4] + "_org" + sys.argv[1][-4:], 'w') as file:
        level = 0;
        newline = False;
        for line in readfile:
            for ch in line:
                if ch == '}' or ch == ']':
                    newline = True
                    level -= 1
                if newline:
                    file.write('\n')
                    for i in range(level):
                        file.write('   ')
                    newline = False
                if ch != ' ':
                    file.write(ch)
                if ch == ':':
                    file.write(' ')

                if ch == '{' or ch == '[':
                    level += 1
                    newline = True
                if ch == ',':
                    newline = True

