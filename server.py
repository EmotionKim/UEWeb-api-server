import sys
import yaml
from time import sleep

from sshtunnel import open_tunnel


def load_config():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config


def ssh_tunnel(config):
    c = config['ssh_tunnel']
    with open_tunnel(
            (c['server_ip'], c['server_port']),
            ssh_username=c['ssh_username'],
            ssh_password=c['ssh_password'],
            remote_bind_address=(c['remote_bind_ip'], c['remote_bind_port'])
    ) as server:
        print(server.local_bind_port)
        print(server)
        while True:
            sleep(1)
            print('PING!')

    print('FINISH!')


if __name__ == '__main__':
    env = sys.argv[1] if len(sys.argv) > 2 else 'dev'
    config = load_config()

    ssh_tunnel(config)
