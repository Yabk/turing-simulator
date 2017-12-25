#!/usr/bin/python3

import sys
import os
import re
from turing import Turing
from ast import literal_eval


def main():
    if len(sys.argv) > 2:
        print('Input only one file!')
        return
    with open(sys.argv[1]) as f:
        symbols = re.search('symbols=(.*)', f.readline()).group(1)
        default = re.search('default_symbol=(.)', f.readline()).group(1)
        tape = list(re.search('tape=(.*)', f.readline()).group(1))
        cursor = int(re.search('cursor=(.*)', f.readline()).group(1))
        starting_state = re.search('starting_state=(.*)', f.readline()).group(1)
        ending_state = re.search('ending_state=(.*)', f.readline()).group(1)
        states = literal_eval(''.join(f.readlines())[6:])

    turing = Turing(states, starting_state, tape, cursor, ending_state, default)
    q = ''
    step = 0
    finished = False
    while q != 'q' and not finished:
        if turing.state == ending_state:
            finished = True
            instruction = ['-', '-', '-']
        else:
            instruction = turing.states[turing.state][turing.tape[turing.cursor]]
        rows, columns = os.popen('stty size', 'r').read().split()
        os.system('clear')
        print('Step:{:8}'.format(step))
        print(tape_part(turing.tape, turing.cursor, int(columns), default))
        print('State: ' + turing.state)
        print('Write: ' + str(instruction[0]))
        if instruction[1] == 'r':
            print('Going Right')
        elif instruction[1] == 'l':
            print('Going Left')
        else:
            print('Not moving')
        print('Next state: ' + instruction[2])
        q = input()
        turing.step()
        step += 1


def tape_part(tape, cursor, columns, defaut):
    d = (columns-2)//2
    e = (columns-2)%2
    s = ''
    for i in range(cursor-d, cursor+d+e):
        if i == cursor:
            s += '['+str(tape[cursor])+']'
        elif (i < 0) or (i >= len(tape)):
            s += defaut
        else:
            s += str(tape[i])
    return s


if __name__ == '__main__':
    main()
