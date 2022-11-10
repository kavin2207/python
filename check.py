import paramiko
ip="192.168.29.126"
user="pi"
passd="abhijeet"

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,username=user,password=passd)

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls")

output=ssh_stdout.readlines()

ssh.close()

print("sssss : ",output)
