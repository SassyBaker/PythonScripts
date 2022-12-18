# NGINX Install from official Repo
import subprocess


def execute_command(text_list):
    for text in text_list:
        process_output = subprocess.run([text], shell=True)
        if process_output.returncode != 0:
            return False

    return True


def user_prompt():
    print('What OS should I install it for (q to quit)?')
    print('E.X Debian, Windows, Mac')
    user_input = input('>').lower()

    if user_input == 'q':
        exit()

    print(f"You have selected {user_input}")
    return user_input


def debian_installer():
    commands_list = [
        'apt install curl gnupg2 ca-certificates lsb-release debian-archive-keyring',
        'curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor | tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null',
        'gpg --dry-run --quiet --no-keyring --import --import-options import-show /usr/share/keyrings/nginx-archive-keyring.gpg',
        'echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] http://nginx.org/packages/debian `lsb_release -cs` nginx" | tee /etc/apt/sources.list.d/nginx.list',
        'echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" | tee /etc/apt/preferences.d/99nginx',
        'apt update'
        'apt install nginx'
    ]

    process_output = execute_command(commands_list)
    print(process_output)


if __name__ == '__main__':
    while True:
        output = user_prompt()
        if output == 'debian':
            debian_installer()
        else:
            print('Sorry that option is not available\n')
