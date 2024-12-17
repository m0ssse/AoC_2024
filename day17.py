def run(a, b, c, program):
    registers = [a, b, c]
    i = 0
    output = []
    while i<len(program):
        opcode, param = program[i:i+2]
        if opcode==0:
            i = opcode0(registers, param, i)
        if opcode==1:
            i = opcode1(registers, param, i)
        if opcode==2:
            i = opcode2(registers, param, i)
        if opcode==3:
            i = opcode3(registers, param, i)
        if opcode==4:
            i = opcode4(registers, param, i)
        if opcode==5:
            i = opcode5(registers, param, i, output)
        if opcode==6:
            i = opcode6(registers, param, i)
        if opcode==7:
            i = opcode7(registers, param, i)
    return output
def combo(registers, param):
    if param>=4:
        return registers[param-4]
    return param

def opcode0(registers, param, i):
    registers[0]>>=combo(registers, param)
    return i+2

def opcode1(registers, param, i):
    registers[1]^=param
    return i+2

def opcode2(registers, param, i):
    registers[1]=combo(registers, param)%8
    return i+2

def opcode3(registers, param, i):
    if not registers[0]:
        return i+2
    return param

def opcode4(registers, param, i):
    registers[1]^=registers[2]
    return i+2

def opcode5(registers, param, i, output):
    output.append(combo(registers, param)%8)
    return i+2

def opcode6(registers, param, i):
    registers[1] = registers[0]>>combo(registers, param)
    return i+2

def opcode7(registers, param, i):
    registers[2] = registers[0]>>combo(registers, param)
    return i+2
    
def part2(program):
    ll = len(program)
    suffixes = {0}
    coeff = 1
    res = float("inf")
    for target_length in range(1, ll+1):
        suffixes_new = set()
        for suffix in suffixes:
            for i in range(4096):
                a = i*coeff+suffix
                output = run(a, 0, 0, program)
                if output[:target_length] == program[:target_length]:
                    suffixes_new.add(a%(8*coeff))
                if output==program:
                    res = min(res, a)
        suffixes = suffixes_new
        coeff*=8
    print(res)
    
fname = "day17_input.txt"
with open(fname) as file:
    registers, program = file.read().split("\n\n")
registers = registers.split("\n")
a, b, c = [int(s.split(": ")[-1]) for s in registers]
program = [int(s) for s in program.split(": ")[-1].split(",")]
print(run(a, b, c, program))
part2(program)
