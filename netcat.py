import subprocess, argparse, socket, shlex, sys, textwrap, threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output =  subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT)

    return(output.decode())



#доделать середину ( класс NetCat)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='что-то там написать надо',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            natcat.py -t 192.168.1.108 -p 5555 -l -c
            natcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt
            natcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\"
            echo 'ABC' | natcat.py -t 192.168.1.108 -p 135
            natcat.py -t 192.168.1.108 -p 5555
        '''))
    parser.add_argument('-c', '--command', action='store_true')
    parser.add_argument('-e', '--execute')
    parser.add_argument('-l', '--listen', action='store_true')
    parser.add_argument('-p', '--port', type=int, default=5555)
    parser.add_argument('-t', '--target', default='192.168.1.203')
    parser.add_argument('-u', '--upload')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode())
    nc.run()
