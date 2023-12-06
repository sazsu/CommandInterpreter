import os
import shutil
command_list = ["ls", "cd", "mv", "rm", "mk", "mkdir", "pwd", "clear", "help"]
help_dict = {
    "ls" : "вывести содержимое текущей директории",
    "cd" : "изменить текущую директорию",
    "mv" : "переместить файл или директорию",
    "rm" : "удалить файл или директорию",
    "mk" : "создать файл",
    "mkdir" : "создать директорию",
    "pwd" : "вывести текущую директорию",
    "clear" : "очистить экран",
    "exit" : "завершить программу"
}
def check_file_folder(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            return 1
        elif os.path.isdir(path):
            return 2 if os.listdir(path) else 3
    return 0

def ls(current_path):
    contents = os.listdir(current_path)
    result = "\n".join(contents)
    return result
def cd(args):
    if args.startswith("\\"):
        args = args[1:]
    os.chdir(args)

def mv(args, current_path):
    src, dest = args.split(" \\", 1)
    source_path = os.path.join(current_path, src)
    destination_path = os.path.join(current_path, dest)

    shutil.move(source_path, destination_path)

def rm(args):
    result = None
    match check_file_folder(args):
        case 0:
            result = "Нет такого файла или директории"
        case 1:
            os.remove(args)
        case 2:
            shutil.rmtree(args)
        case 3:
            os.rmdir(args)
    return result
def mk(args):
    with open(args, "a") as file:
        while True:
            user_append_to_file = input()
            if user_append_to_file.lower() != "exit":
                file.write(user_append_to_file + '\n')
            else:
                break

def mkdir(args, current_path):
    os.mkdir(current_path + "\\" + str(args))

def pwd():
    return os.getcwd()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def help(args):
    if args and args in command_list:
        result = f'{args} - {help_dict.get(args)}'
    else:
        result = "\n".join(command_list)
    return result

def run_command(user_input):
    try:
        current_path = os.getcwd()
        command = user_input[0]
        args = user_input[1] if len(user_input) >= 2 else None
        match command:
            case "ls":
                result = ls(current_path)
            case "cd":
                result = cd(args)
            case "mv":
                result = mv(args, current_path)
            case "rm":
                result = rm(args)
            case "mk":
                result = mk(args)
            case "mkdir":
                result = mkdir(args, current_path)
            case "pwd":
                result = pwd()
            case "clear":
                result = clear()
            case "help":
                result = help(args)

        print("", end="" if not result else result + "\n")


    except Exception as e:
        print(f"Ошибка: {e}")

while True:
    user_input = input()
    match user_input:
        case "exit":
            break
        case _:
            user_input = user_input.split(" ", 1)
            run_command(user_input)