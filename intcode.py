from copy import copy


class Intcode:
    POS = 0
    IMM = 1

    def __init__(self, reg, inputs):
        self.reg = copy(reg)
        self.ip = 0
        self.done = False

        self.inputs = inputs

        self.mode = self.POS
        self.value = None

    def run(self, until_output=False):
        while True:
            ins = self.reg[self.ip]
            mp1, mp2, mp3 = (int(ins / v) % 10 for v in (100, 1000, 10000))
            op = ins % 100

            if op == 99:
                self.done = True
                break
            r1 = self.ip+1 if mp1 == self.IMM else self.reg[self.ip+1]
            r2 = self.ip+2 if mp2 == self.IMM else self.reg[self.ip+2]
            try:
                r3 = self.ip+3 if mp3 == self.IMM else self.reg[self.ip+3]
            except IndexError:
                pass # if this happens, you don't need it
            if op == 1:
                self.reg[r3] = self.reg[r1] + self.reg[r2]
                self.ip += 4
            elif op == 2:
                self.reg[r3] = self.reg[r1] * self.reg[r2]
                self.ip += 4
            elif op == 3:
                self.reg[r1] = self.inputs.pop(0)
                self.ip += 2
            elif op == 4:
                self.value = self.reg[r1]
                self.ip += 2
                if until_output:
                    break
            elif op == 5:
                if self.reg[r1]:
                    self.ip = self.reg[r2]
                else:
                    self.ip += 3
            elif op == 6:
                if self.reg[r1] == 0:
                    self.ip = self.reg[r2]
                else:
                    self.ip += 3
            elif op == 7:
                self.reg[r3] = 1 if self.reg[r1] < self.reg[r2] else 0
                self.ip += 4
            elif op == 8:
                self.reg[r3] = 1 if self.reg[r1] == self.reg[r2] else 0
                self.ip += 4
            else:
                print(f'Bad opcode: {op} - EXITING')
                break
        return self.value

    def run_until_output(self):
        return self.run(until_output=True)
