

hostname = input('enter hostname: ')
ip = input('enter IP address: ')
group = input('Enter group name: ')


hostname2 = input('enter hostname2: ')
ip2 = input('enter IP address2: ')
group2 = input('Enter group name2: ')


hostname3 = input('enter hostname3: ')
ip3 = input('enter IP address3: ')
group3 = input('Enter group name3: ')


hostname4 = input('enter hostname4: ')
ip4 = input('enter IP address4: ')
group4 = input('Enter group name4: ')




with open ('hosts.yml', 'a') as f:
    f.write (hostname + ':  \n')
    f.write ('  hostname: ' + ip + '\n')
    f.write ('  groups:' + '\n')
    f.write ('    - ' + group + '\n') 
    f.write('\n')
    f.write (hostname2 + ':  \n')
    f.write ('  hostname: ' + ip2 + '\n')
    f.write ('  groups:' + '\n')
    f.write ('    - ' + group2 + '\n')
    f.write('\n')
    f.write (hostname3 + ':  \n')
    f.write ('  hostname: ' + ip3 + '\n')
    f.write ('  groups:' + '\n')
    f.write ('    - ' + group3 + '\n')
    f.write ('\n')
    f.write (hostname4 + ':  \n')
    f.write ('  hostname: ' + ip4 + '\n')
    f.write ('  groups:' + '\n')
    f.write ('    - ' + group4 + '\n')
    f.write('\n')
    f.write('\n')
