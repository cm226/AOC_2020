f = open("input_day8.txt")

cmds = []

for line in f:
    cmd, arg = line.split(' ')

    sgn = arg[0]
    if sgn == '-' : 
        sgn = -1
    else :
        sgn = 1

    arg = int(arg[1:])*sgn

    cmds.append((cmd, arg))

# run the program


change_instruction_acc = 3
while True:
    tmp_cmds = cmds.copy()
    change_instruction_counter = 0

    instruction_ptr = 0
    visited_instructions = []
    global_acc = 0

    while True:

        if instruction_ptr == len(cmds):
            print(global_acc)
            exit()

        instruction = tmp_cmds[instruction_ptr]
        
        if instruction_ptr in visited_instructions:
            break;

        visited_instructions.append(instruction_ptr)

        if instruction[0] == 'jmp' or instruction[0] == 'nop':
            change_instruction_counter+=1

        if change_instruction_counter == change_instruction_acc:
            change_instruction_counter+=1
            if instruction[0] == 'nop':
                instruction = ('jmp', instruction[1])
            else:
                instruction = ('nop', instruction[1])

        if instruction[0] == 'nop':
            instruction_ptr+=1    
            continue
        
        if instruction[0] == 'acc':
            global_acc += instruction[1]
            instruction_ptr+=1
            continue

        if instruction[0] == 'jmp':
            instruction_ptr += instruction[1]
            continue

        print("GOT BAD INSTRUCTION" + instruction[0])

    
    change_instruction_acc+=1



