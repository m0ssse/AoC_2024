def part1(fname):
    with open(fname) as inputfile:
        contents = inputfile.read().strip()
    memory = []
    file_id = 0
    free_space_count = 0
    for i, n in enumerate(contents):
        if i%2==0:
            memory.extend([file_id]*int(n))
            file_id+=1
        else:
            memory.extend([-1]*int(n))
    free_memory_index = 0
    while free_space_count:
        while memory[free_memory_index]!=-1:
            free_memory_index+=1
        if memory[-1]!=-1:
            memory[-1], memory[free_memory_index] = memory[free_memory_index], memory[-1]
        memory.pop()
        free_space_count-=1
    checksum = 0
    for i, x in enumerate(memory):
        checksum+=i*x
    print(checksum)

def part2(fname):
    with open(fname) as inputfile:
        contents = inputfile.read().strip()
    memory = []
    file_id = 0
    for i, n in enumerate(contents):
        if i%2==0:
            memory.extend([file_id]*int(n))
            file_id+=1
        else:
            memory.extend([-1]*int(n))
    file_blocks = []
    memory_blocks = []
    curr_file_id = memory[0]
    curr_block_length = 1
    curr_block_start = 0
    for i in range(1, len(memory)):
        if memory[i]==curr_file_id:
            curr_block_length+=1
        else:
            if curr_file_id!=-1:
                file_blocks.append((curr_block_start, curr_block_length, curr_file_id))
            else:
                memory_blocks.append((curr_block_start, curr_block_length, -1))
            curr_file_id = memory[i]
            curr_block_length = 1
            curr_block_start = i
    if curr_file_id!=-1:
        file_blocks.append((curr_block_start, curr_block_length, curr_file_id))
    file_blocks = file_blocks[::-1]
    for file_start, file_size, file_id in file_blocks:
        for i, (block_start, block_size, _) in enumerate(memory_blocks):
            if block_start>=file_start:
                break
            elif block_size>=file_size:
                memory[block_start:block_start+file_size] = [file_id]*file_size
                memory[file_start:file_start+file_size] = [-1]*file_size
                memory_blocks[i] = (block_start+file_size, block_size-file_size, -1)
                break
    checksum = 0
    for i, x in enumerate(memory):
        if x!=-1:
            checksum+=i*x
    print(checksum)
fname = "day9_input.txt"
part2(fname)