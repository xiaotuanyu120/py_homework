from fabric.api import run, env, roles, local, put

env.hosts = [
    'root@192.168.0.96:22',
    'root@192.168.0.4:22'
] 

env.passwords = {
    'root@192.168.0.96:22':'Sudoroot88',
    'root@192.168.0.4:22':'Sudoroot88'
}


def deploy_key(warn_only=True):
    run('rm -rf ~/.ssh')
    run('mkdir -p ~/.ssh/;chmod 700 ~/.ssh/')
    put('/root/.ssh/id_rsa.pub', '~/.ssh/authorized_keys')
    run('chmod 600 ~/.ssh/authorized_keys')
