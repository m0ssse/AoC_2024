def counts(design, options, memory):
    if design in memory:
        return memory[design]
    memory[design]=0
    for prefix in options:
        if design.startswith(prefix):
            suffix = design[len(prefix):]
            memory[design]+=counts(suffix, options, memory)
    return memory[design]

def solve(designs, options):
    memory = {"": 1}
    res1 = 0
    res2 = 0 
    for design in designs:
        n = counts(design, options, memory)
        if n:
            res1+=1
            res2+=n
    print(res1)
    print(res2)

fname = "day19_input.txt"
with open(fname) as myfile:
    options, designs = myfile.read().split("\n\n")
    options = options.split(", ")
    designs = designs.split()

solve(designs, options)