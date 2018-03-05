import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
            k=inkey()
            if k!='':break
        if k=='\x1b[A':
                i = "0,1,0"
        elif k=='\x1b[B':
                i = "0,-1,0"
        elif k=='\x1b[C':
                i = "1,0,0"
        elif k=='\x1b[D':
                i = "-1,0,0"
        else:
                return False
        return True

def main():
        flag = True
        while flag:
            flag = get()

if __name__=='__main__':
        main()