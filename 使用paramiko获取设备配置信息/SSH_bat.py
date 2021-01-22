import paramiko
from Device_IP_List import IP_ADD

# IP_ADD = ['192.168.152.11','192.168.152.12']

USER = 'admin'
PWD = 'admin'
PORT = 22

def get_config(IP):
    ssh = paramiko.SSHClient()      #创建SSH对象
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())       #允许连接不在know_hosts文件中的主机
    ssh.connect(hostname=IP,port=PORT,username=USER,password=PWD)       #连接服务器
    stdin,stdout,stderr = ssh.exec_command('show run | include name')       #执行命令
    result = stdout.read()      #获取命令结果
    # print(str(result,encoding='utf-8'))
    result = str(result,encoding='utf-8')
    ssh.close()     #关闭连接
    return result

for x in IP_ADD:
    a = get_config(x)
    print(a)
    with open('/tmp/device_config.txt','a+') as f:
        f.write(a + '\n')
        f.close()
