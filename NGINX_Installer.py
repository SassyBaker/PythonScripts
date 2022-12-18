# NGINX Install from official Repo
import subprocess


def user_prompt():
    print('What OS should I install it for (q to quit)?')
    print('E.X Debian, Windows, Mac')
    user_input = input('>> ').lower()

    if user_input == 'q':
        exit()

    print(f"You have selected {user_input}")
    return user_input


def debian_installer():
    process_output = subprocess.run(['sudo apt install curl gnupg2 ca-certificates lsb-release debian-archive-keyring'])
    print(process_output)


if __name__ == '__main__':
    while True:
        output = user_prompt()
        if output == 'debian':
            debian_installer()
        else:
            print('Sorry that option is not available\n')

# https://codefather.tech/blog/shell-command-python/
