import os
import shutil

print("© Rokt Inc; 2024 - 2024")
print("Rokt Version: 0.0.1")

while True:
    cmd = input("> ")
    if cmd == "help":
        print("Available commands: \n help: Shows this text. \n makedir: Creates a directory \n deldir: Deletes a directory")
    elif cmd == "makedir":
        folder_name = input("DIR NAME > ")

        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print(f"Folder '{folder_name}' created successfully.")
        else:
            print(f"Folder '{folder_name}' already exists")
    elif cmd == "deldir":
        folder_name = input("DIR NAME > ")

        if os.path.exists(folder_name):
            os.rmdir(folder_name)
            print(f"Folder '{folder_name}' removed successfully.")
        else:
            print(f"Folder '{folder_name}' doesn't exists")
    elif cmd == "text":
        printe = input("Enter Text To Print > ")
        print(printe)
    elif cmd == "deltree":
        folder_name = input("Enter folder name > ")
        if shutil.os.path.exists(folder_name):
            shutil.rmtree(folder_name)
            print(f"Directory '{folder_name}' removed successfully.")
        else:
            print(f"Directory '{folder_name}' does not exist.")