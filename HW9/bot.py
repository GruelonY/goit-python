def input_error(func):
    def inner(command):
        try:
            return func(command)
        except KeyError:
            return f'There is no phone with that name, please enter valid name!!'
        except ValueError:
            return f'Give me name and phone please'
        except IndexError:
            return f'Give me data for command,name and phone for commands "change" or "add", name for command "phone"'

    return inner


def hello_handler():
    return 'How can i help you?'


@input_error
def add_handler(command):
    name = command[1].capitalize()
    phone = command[2]
    phone_dict[name] = int(phone)
    return f'Successfully added user phone: {name}!!'


@input_error
def change_handler(command):
    name = command[1].capitalize()
    phone = command[2]
    if name not in phone_dict.keys():
        return phone_dict[name]
    else:
        phone_dict[name] = int(phone)
        return f'Successfully changed phone for user: {name}!!'


@input_error
def show_phone_handler(command):
    name = command[1].capitalize()
    return phone_dict[name]


def show_all_handler():
    full_list = []
    for item in phone_dict.items():
        full_list.append(item)
    return f'{full_list}'


def main():
    user_commands = {
        'add': add_handler,
        'change': change_handler,
        'phone': show_phone_handler,
    }
    default_commands = {
        'help': lambda: f'This bot supports these commands: {", ".join(commands_list)}',
        'hello': hello_handler,
        'show': show_all_handler,
    }

    commands_list = ['help', 'hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close', 'exit']

    user_command = input('Write command: ')
    while user_command not in ['good bye', 'close', 'exit']:
        user_input = user_command.lower().split()
        cmd_name = user_input[0]
        if cmd_name in user_commands.keys():
            print(user_commands.get(cmd_name)(user_input))
        elif cmd_name in default_commands.keys():
            print(default_commands.get(cmd_name)())
        else:
            print('Invalid command')
        user_command = input('Write command: ')
    print('Good bye!')


if __name__ == '__main__':
    main()