import os
import shutil
command_list = ["ls", "cd", "mv", "rm", "mkdir", "pwd", "clear", "help"]
def check_file_folder(path):
    if os.path.isfile(path):
        return 1
    elif os.path.isdir(path):
        if not os.listdir(path):
            return 3
        else:
            return 2
    else:
        return 0

def run_command(user_input):
    try:
        command = user_input[0]
        args = user_input[1] if len(user_input) >= 2 else None
        current_path = os.getcwd()
        match command:
            case "ls":
                contents = os.listdir(current_path)
                result = "\n".join(contents)
            case "cd":
                os.chdir(user_input[1])

                result = None
            case "mv":
                prefix_index = args.find(' "')
                source_path = current_path + "\\" + args[:prefix_index + 1]
                destination_path = args[prefix_index + 2:-1]

                shutil.move(source_path, destination_path)

                result = None
            case "rm":
                path = current_path + "\\" + str(args)
                result = None

                match check_file_folder(path):
                    case 0:
                        result = "No such file or directory"
                    case 1:
                        os.remove(args)
                    case 2:
                        shutil.rmtree(args)
                    case 3:
                        os.rmdir(args)
            case "mkdir":
                os.mkdir(current_path + "\\" + str(args))

                result = None
            case "pwd":
                result = current_path
            case "clear":
                os.system("cls" if os.name == "nt" else "clear")

                result = None
            case "help":
                result = "\n".join(command_list)
            case _:
                result = f"Command '{command}' not recognized."

        print("", end="" if not result else result + "\n")


    except Exception as e:
        return f"An error occurred: {e}"


while True:
    user_input = input()

    match user_input:
        case "exit":
            break
        case _:
            user_input = user_input.split(" ", 1)

            run_command(user_input)