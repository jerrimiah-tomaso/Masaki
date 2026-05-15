numbers = 1234567890

valid_commands = ["timer","alarm"]

def parse(data):

    commands = []

    tokens = data.split()

    print("Parsing: ", data)

    for token in tokens:
        if token in valid_commands:
            current_command = token
        elif token.isdigit() and current_command is not None:
            commands.append((current_command, int(token)))
            current_command = None

