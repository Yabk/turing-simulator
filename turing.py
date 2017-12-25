#!/usr/bin/python3


class Turing:

    def __init__(self, states, starting_state, starting_tape, cursor, ending_state, default_symbol = 'b'):
        self.states = states
        self.state = starting_state
        self.tape = starting_tape
        self.cursor = cursor
        self.end = ending_state
        self.default = default_symbol

    def step(self):
        if self.state != self.end:
            instruction = self.states[self.state][self.tape[self.cursor]]
            self.tape[self.cursor] = instruction[0]

            if instruction[1] == 'r':
                self.cursor += 1
                if self.cursor == len(self.tape):
                    self.tape.append(self.default)
            elif instruction[1] == 'l':
                if self.cursor == 0:
                    self.tape.insert(0, self.default)
                else:
                    self.cursor -= 1
            self.state = instruction[2]


if __name__ == '__main__':
    states = {'q0': {'0': ['0', 'r', 'q1'], '1': ['1', 'r', 'q1'], '2': ['2', 'r', 'q1'], '3': ['3', 'r', 'q1'],
                     '4': ['4', 'r', 'q1'], '5': ['5', 'r', 'q1'], '6': ['6', 'r', 'q1'], '7': ['7', 'r', 'q1'],
                     '8': ['8', 'r', 'q1'], '9': ['9', 'r', 'q1'], 'b': ['b', 'r', 'q0']},
              'q1': {'0': ['0', 'r', 'q1'], '1': ['1', 'r', 'q1'], '2': ['2', 'r', 'q1'], '3': ['3', 'r', 'q1'],
                     '4': ['4', 'r', 'q1'], '5': ['5', 'r', 'q1'], '6': ['6', 'r', 'q1'], '7': ['7', 'r', 'q1'],
                     '8': ['8', 'r', 'q1'], '9': ['9', 'r', 'q1'], 'b': ['b', 'l', 'q2']},
              'q2': {'0': ['1', 'n', 'q1'], '1': ['2', 'n', 'q1'], '2': ['3', 'n', 'q1'], '3': ['4', 'n', 'q1'],
                     '4': ['5', 'n', 'q1'], '5': ['6', 'n', 'q1'], '6': ['7', 'n', 'q1'], '7': ['8', 'n', 'q1'],
                     '8': ['9', 'n', 'q1'], '9': ['0', 'l', 'q2'], 'b': ['1', 'n', 'qf']}
              }
    tape = ['b','b','b','1','2','6','9','b','b']
    test = Turing(states, 'q0', tape, 1, 'qf')

    print('test')
    for i in range(10):
        print(tape)
        test.step()
