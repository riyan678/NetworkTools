from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

username = input('Enter you Username: ')
password = getpass()
ip = input('Enter fqdn to connect or ip address (default is 172.24.105.14): ') or '172.24.105.14'
enable = input('Enter the enable secret: ')

Core_Switch = {
                'device_type': 'cisco_ios',
                'ip': ip,
                'username': username,
                'password': password,
                'secret': enable
               }

def get_vlan(Core_Switch):
    print('Connecting to ' + Core_Switch['ip'])
    connection = ConnectHandler(**Core_Switch)
    print('Getting vlan information')
    get_vlan = connection.send_command('show vlan br')
    connection.disconnect()
    parse_vlan = get_vlan.strip().splitlines()
    vlan_keys = []
    for line in parse_vlan:
        vlan_dict = {}
        if line.split()[0].isdigit():
            vlan_dict['vlan_id'] = line.split()[0]
            vlan_dict['vlan_name'] = line.split()[1]
            vlan_keys.append(vlan_dict)
    return vlan_keys



if __name__ == '__main__':
    vlans= get_vlan(Core_Switch)
    pprint(vlans)
