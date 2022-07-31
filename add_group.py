
group = input('Enter group name: ')
username = input('Enter username: ')
password = input('Enter password: ')

#### Writing host to exsiting host file####

with open ('groups.yml', 'a') as f:
    f.write (group + ':  \n')
    f.write ('\n')
    f.write ('  platform: ios' + '\n')
    f.write ('  username: ' + username + '\n')
    f.write ('  password: ' + password + '\n') 
    f.write('\n')
    f.write('\n')
