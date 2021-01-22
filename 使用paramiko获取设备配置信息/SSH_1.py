import paramiko
from Device_info_list_1 import device_info_list

USER = device_info_list[0]['username']
PWD = device_info_list[0]['password']
IP = device_info_list[0]['ip_address']
PORT = '22'

def get_config(IP1=IP):
    ssh =paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=IP1,port=PORT,username=USER,password=PWD)
    stdin,stdout,stderr = ssh.exec_command('show run | include name')
    result = stdout.read()
    print(str(result,encoding='utf-8'))
    result = str(result,encoding='utf-8')
    ssh.close()
    return result

get_config()
