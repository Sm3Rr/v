import paramiko
import sys

def execute_command(ip, username, password, command):
    try:
        # Connect to the server
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password)

        # Execute the command
        stdin, stdout, stderr = ssh.exec_command(command)

        # Print the output of the command
        print(stdout.read().decode('utf-8'))

        # Close the connection
        ssh.close()

    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <ip> <username> <password>")
        sys.exit(1)

    ip = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    command = "net user Administrator Smer@Smer11"

    execute_command(ip, username, password, command)
