from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir.core.filter import F

nr = InitNornir(
    config_file="config.yml"
)

def config(push):
    push.run(task=netmiko_send_config, config_file="cfg-update.txt")
    push.run(task=netmiko_send_command, command_string = "sh run | begin line ")
    push.run(task=netmiko_send_command, command_string = "wr mem")

host = input("Enter host name(811-SW1) : ")

devices = nr.filter((F(hostname__contains=(host))))

results = devices.run(task = config)

print_title("Deploying Configuration")
print_result(results)

