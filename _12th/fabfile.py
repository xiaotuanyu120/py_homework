from fabric.api import run, cd, env

env.hosts = [
    'root@192.168.0.96',
    'root@192.168.0.4'
] 

env.warn_only=True


def has_python():
    result = run('which python')
    if not result.return_code:
        return True
    else:
        return False

def has_ipython():
    result = run('which ipython')
    if not result.return_code:
        return True
    else:
        return False

def has_pip():
    result = run('which pip')
    if not result.return_code:
        return True
    else:
        return False

def deploy_ipython():
    if has_ipython():
        print 'Needn\'t install, ipython already existed!'
        return True
    else:
        if not has_python():
            try:
                run('yum -y install python')
            except Exception as e:
                print 'python install process error!', e
                return False
        if not has_pip():
            with cd('/tmp'):
                try:
                    run('wget https://bootstrap.pypa.io/get-pip.py')
                except Exception as e:
                    print 'pip download error!'
                    return False
                try:
                    run('python get-pip.py')
                    return True
                except Exception as e:
                    print 'pip install process error!', e
                    return False
        try:
            run('pip install ipython')
        except Exception as e:
            print 'ipython install process error!', e
            return False
