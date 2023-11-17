import paramiko

def change_vps_password(vps_ip, username, password, new_password):
    # برقراری ارتباط با VPS
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(vps_ip, username=username, password=password)

    # اجرای دستور net user برای تغییر رمز عبور
    command = f"net user Administrator {new_password}"
    stdin, stdout, stderr = client.exec_command(command)

    # چاپ خروجی دستور
    print(stdout.read().decode())

    # بستن اتصال
    client.close()

# ورودی‌ها
vps_ip = input("IP VPS را وارد کنید: ")
username = input("نام کاربری را وارد کنید: ")
password = input("رمز عبور را وارد کنید: ")
new_password = input("رمز عبور جدید را وارد کنید: ")

# تغییر رمز عبور سرور مجازی
change_vps_password(vps_ip, username, password, new_password)
