import subprocess

cmd=input("请输入指令>>>")
sub_obj=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

print(sub_obj.stdout.read().decode("gbk"))