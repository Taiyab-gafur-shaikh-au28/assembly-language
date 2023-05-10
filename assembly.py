def execute(instructions):
    # Initialize 4 registers
    registers = [0, 0, 0, 0]

    for instruction in instructions:
        # Parse instruction
        parts = instruction.split()

        if parts[0] == "MV":
            # Move immediate value into register
            reg_num = int(parts[1][3]) # Extract register number from instruction
            value = int(parts[2][1:])
            registers[reg_num] = value

        elif parts[0] == "ADD":
            # Add immediate value or value from another register to a register
            reg_num_1 = int(parts[1][3])
            if parts[2].startswith("#"):
                value = int(parts[2][1:])
                registers[reg_num_1] += value
            else:
                reg_num_2 = int(parts[2][3])
                registers[reg_num_1] += registers[reg_num_2]

        elif parts[0] == "SHOW":
            # Print value in register
            reg_num = int(parts[1][3])
            print(registers[reg_num])

        else:
            raise ValueError("Invalid instruction: " + instruction)

# Example program
program = [
    "MV REG1, #2000",
    "MV REG2, #4000",
    "ADD REG1, REG2",
    "ADD REG1, #600",
    "SHOW REG1"
]

execute(program)

