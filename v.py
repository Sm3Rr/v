import requests
import json

def change_password(old_password, new_password, username, server_ip):
    url = f"http://{server_ip}/api/users/password"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "oldPassword": old_password,
        "newPassword": new_password,
        "username": username,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), auth=('admin', 'password'))
    
    try:
        response.raise_for_status()
        return " PASSWORD CHANGED ! "
    except requests.exceptions.HTTPError as errh:
        return "Http Error:", errh
    except requests.exceptions.ConnectionError as errc:
        return "Error Connecting:", errc
    except requests.exceptions.Timeout as errt:
        return "Timeout Error:", errt
    except requests.exceptions.RequestException as err:
        return "OOps: Something Else", err

if __name__ == "__main__":
    old_password = input("old pass : ")
    new_password = input("new pass : ")
    username = input("user : ")
    server_ip =input("ip address : ")
    result = change_password(old_password, new_password, username, server_ip)
    print(result)
