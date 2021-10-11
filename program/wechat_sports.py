## utf-8
import subprocess

class altera_system_console:
    def __init__(self):
        sc_path = r'wechat.exe'
        self.console = subprocess.Popen(sc_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def read_output(self):
        return self.console.stdout.read1(100).decode('utf-8')

    def cmd(self, cmd_string):
        self.console.stdin.write(bytes(cmd_string+'\n','utf-8'))
        self.console.stdin.flush()

def set_step(step, username, password):
    c = altera_system_console()
    print(c.read_output())
    c.cmd(step)
    print(c.read_output())
    c.cmd(username)
    print(c.read_output())
    c.cmd(password)
    print(c.read_output())

if __name__ == '__main__':
    set_step("88888", "13550345266", "133Fzy09962659")