from copy import copy
from enum import IntEnum

class Mode(IntEnum):
    POS = 0
    IMM = 1
    REL = 2


class Op(IntEnum):
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_T = 5
    JUMP_F = 6
    LT = 7
    EQ = 8
    BASE = 9
    HALT = 99


n_args = {
    Op.ADD: 4,
    Op.MULT: 4,
    Op.INPUT: 2,
    Op.OUTPUT: 2,
    Op.JUMP_T: 3,
    Op.JUMP_F: 3,
    Op.LT: 4,
    Op.EQ: 4,
    Op.BASE: 2,
    Op.HALT: 1
}


class Intcode:
    def __init__(self, reg, inputs=[]):
        self.reg = copy(reg)
        self.reg.extend([0] * 20000)
        self.ip = 0
        self.base = 0
        self.done = False

        self.inputs = inputs

        self.mode = Mode.POS
        self.value = None
        self.debug = False

    def run(self, until_output=False, display=False):
        while True:
            ins = self.reg[self.ip]
            mp1, mp2, mp3 = ((ins // v) % 10 for v in (100, 1000, 10000))
            op = ins % 100

            if op == Op.HALT:
                self.done = True
                break

            if n_args[op] >= 2:
                if mp1 == Mode.IMM:
                    r1 = self.ip+1
                elif mp1 == Mode.POS:
                    r1 = self.reg[self.ip+1]
                elif mp1 == Mode.REL:
                    r1 = self.reg[self.ip+1] + self.base

            if n_args[op] >= 3:
                if mp2 == Mode.IMM:
                    r2 = self.ip+2
                elif mp2 == Mode.POS:
                    r2 = self.reg[self.ip+2]
                elif mp2 == Mode.REL:
                    r2 = self.reg[self.ip+2] + self.base

            if n_args[op] >= 4:
                if mp3 == Mode.IMM:
                    r3 = self.ip+3
                elif mp3 == Mode.POS:
                    r3 = self.reg[self.ip+3]
                elif mp3 == Mode.REL:
                    r3 = self.reg[self.ip+3] + self.base

            if self.debug:
                line = Op.__dict__['_value2member_map_'][op].name
                if n_args[op] == 2:
                    line += ' R{}'.format(r1)
                elif n_args[op] == 3:
                    a = self.reg[r1]
                    line += ' R{} -> R{}'.format(r1, r2)
                if n_args[op] == 4:
                    a, b = self.reg[r1], self.reg[r2]
                    line += ' R{} R{} -> R{}'.format(r1, r2, r3)

            if op == Op.ADD:
                self.reg[r3] = self.reg[r1] + self.reg[r2]
                self.ip += n_args[op]
            elif op == Op.MULT:
                self.reg[r3] = self.reg[r1] * self.reg[r2]
                self.ip += n_args[op]
            elif op == Op.INPUT:
                self.reg[r1] = self.inputs.pop(0)
                self.ip += n_args[op]
            elif op == Op.OUTPUT:
                self.value = self.reg[r1]
                self.ip += n_args[op]
                if display:
                    if self.reg[self.ip] % 100 == Op.HALT:
                        print(f'Diagnostic code: {self.value}')
                    else:
                        print(f'Test: {self.value}{" - FAILED " if self.value != 0 else ""}')
                if until_output:
                    break
            elif op == Op.JUMP_T:
                if self.reg[r1]:
                    self.ip = self.reg[r2]
                else:
                    self.ip += n_args[op]
            elif op == Op.JUMP_F:
                if self.reg[r1] == 0:
                    self.ip = self.reg[r2]
                else:
                    self.ip += n_args[op]
            elif op == Op.LT:
                self.reg[r3] = 1 if self.reg[r1] < self.reg[r2] else 0
                self.ip += n_args[op]
            elif op == Op.EQ:
                self.reg[r3] = 1 if self.reg[r1] == self.reg[r2] else 0
                self.ip += n_args[op]
            elif op == Op.BASE:
                self.base += self.reg[r1]
                self.ip += n_args[op]
            else:
                print(f'Bad opcode: {op} - EXITING')
                break

            if self.debug:
                if n_args[op] == 2:
                    adding = '{}'.format(self.reg[r1])
                if n_args[op] == 3:
                    adding = '{} -> {}'.format(a, self.reg[r2])
                if n_args[op] == 4:
                    adding = '{} {} -> {}'.format(a, b, self.reg[r3])

                line += ' [{}]'.format(adding)
                print(line)
        return self.value

    def run_until_output(self):
        return self.run(until_output=True)

    def run_until_n_output(self, n):
        o = []
        for _ in range(n):
            o.append(self.run_until_output())
        return o

    def run_collect_output(self):
        d = []
        while not self.done:
            d.append(self.run_until_output())
        return d

    def run_with_output(self):
        return self.run(display=True)

    def run_with_nv(self, noun, verb):
        self.reg[1] = noun
        self.reg[2] = verb
        self.run()
        return self.reg[0]

    def set_debug(self, debug=True):
        self.debug = debug
