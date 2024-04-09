import os
import subprocess
import time

def take_screenshot(full_folder_path):

    while True:
        existing_files = [int(filename.split('.')[0]) for filename in os.listdir(full_folder_path) if filename.endswith('.png')]
        file_number = max(existing_files, default=0) + 1
        file_name = f'{file_number}.png'
        user_input = input('Do you want to take a screenshot? (y/n): ')
        if user_input.lower() == 'y':
            print(f'Taking screenshot in 3 seconds...')
            time.sleep(3)
            subprocess.run(['gnome-screenshot', '-a', '-f', os.path.join(full_folder_path, file_name)])
            print(f'Screenshot saved as {file_name}')

            confirm_input = input('Do you want to keep this screenshot? (y/n): ')
            if confirm_input.lower() == 'n':
                os.remove(os.path.join(full_folder_path, file_name)) 
        else:
            print('No screenshot taken.')
            break

if __name__ == '__main__':
    while True:
        workdir = input("Enter the working directory: ")
        if os.path.exists(workdir) and os.path.isdir(workdir):
            full_workdir = os.path.join(workdir, 'images')
            print("CWD> ", full_workdir)
            take_screenshot(full_workdir)
            break
        else:
            print("Invalid path. Please enter a valid directory path.")

