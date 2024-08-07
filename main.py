import sys

def brainfuck_interpreter(code, input_data=""):
    code = [c for c in code if c in ['>', '<', '+', '-', '.', ',', '[', ']']]
    data = [0] * 30000
    code_ptr = 0
    data_ptr = 0
    input_ptr = 0
    output = []

    brackets = []
    matching_bracket = {}
    for i, command in enumerate(code):
        if command == '[':
            brackets.append(i)
        elif command == ']':
            start = brackets.pop()
            matching_bracket[start] = i
            matching_bracket[i] = start

    while code_ptr < len(code):
        command = code[code_ptr]

        if command == '>':
            data_ptr += 1
        elif command == '<':
            data_ptr -= 1
        elif command == '+':
            data[data_ptr] = (data[data_ptr] + 1) % 256
        elif command == '-':
            data[data_ptr] = (data[data_ptr] - 1) % 256
        elif command == '.':
            output.append(chr(data[data_ptr]))
        elif command == ',':
            if input_ptr < len(input_data):
                data[data_ptr] = ord(input_data[input_ptr])
                input_ptr += 1
            else:
                data[data_ptr] = 0
        elif command == '[':
            if data[data_ptr] == 0:
                code_ptr = matching_bracket[code_ptr]
        elif command == ']':
            if data[data_ptr] != 0:
                code_ptr = matching_bracket[code_ptr]

        code_ptr += 1

    return ''.join(output)

def main():
    if len(sys.argv) < 2:
        print("Usage: python brainfuck_interpreter.py <source_file> [input_string]")
        return

    source_file = sys.argv[1]
    input_data = sys.argv[2] if len(sys.argv) > 2 else ""

    try:
        with open(source_file, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"File not found: {source_file}")
        return

    output = brainfuck_interpreter(code, input_data)
    print(output)

if __name__ == "__main__":
    main()
