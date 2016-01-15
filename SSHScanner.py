from pssh import ParallelSSHClient
import paramiko
import argparse
import pssh.utils

parser = argparse.ArgumentParser(description='Take an SSH Key and Blast it across the network.')
parser.add_argument('-i', '--input', required=True, help='The input file containing hosts')
parser.add_argument('-s', '--sudo', default=False, action='store_true', help='Whether Sudo should be called (Default: False)')
parser.add_argument('-c', '--command', default='id', help='The Command to run (Default: id)')
parser.add_argument('-t', '--timeout', default=120, help='The timeout in seconds (Default: 120)') 
parser.add_argument('-p', '--parallel', default=10, help='The number of hosts to run (Default: 10)')
parser.add_argument('-r', '--retries', default=1, help='Amount of times to retire (Default: 1)')
parser.add_argument('-u', '--user', default='root', help='The username (Default: root)')
parser.add_argument('-k', '--key', required=True, help='The Key file to use')
parser.add_argument('-v', '--verbose', default=False, action='store_true', help='Output Activity to StOut')
parser.add_argument('-o', '-output', help='The output file')
args = vars(parser.parse_args())

Scan_Hosts(args)

def Get_Hosts_From_File(input)
    hosts=[]
    for line in open(input, 'r'):
        hosts.add(line)

    return hosts
 
def Scan_Hosts(args): 
    if args['verbose']:
        pssh.utils.enable_host_logger()

    private_key = paramiko.RSAKey.from_private_key_file(args['key'])
    client = ParallelSSHClient(Get_Hosts_From_File(args['input']), pkey=private_key, pool_size=args['parallel'], timeout=args['timeout'], num_retries=args['retries'])
    output = client.run_command(args['command'], sudo=args['sudo'], stop_on_errors=False)
    
    f = open(args['output'], 'w')
    f.write("Host\tOutput")
    for host in output:
        for line in output[host]['stdout']:
            f.write(host + "\t" + line)    
