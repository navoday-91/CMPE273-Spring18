from __future__ import print_function
import threading
import grpc, time
import drone_pb2_grpc
from drone_pb2 import Request
import sys,tty,termios


class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
                if ch == '\x1b' or ch == 'b':
                    ch += sys.stdin.read(2)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def gen(stub):
    name = ""
    k = 0
    prompt = False
    while 1:
        req = ""
        if k == 0:
            i = input("\nEnter 'q' to exit or... \nEnter a name for your drone: \n")
        elif k == 1:
            i = input("\nEnter starting coordinates (x,y,z) separated by comma e.g. 1,1,1:\n")
        else:
            if prompt == False:
                print("\nUse Arrow Keys to control and \"bye\" to quit: \n")
                prompt = True
            inkey = _Getch()
            key = inkey()
            if key == '\x1b[A':
                i = "0,1,0"
            elif key == '\x1b[B':
                i = "0,-1,0"
            elif key == '\x1b[C':
                i = "1,0,0"
            elif key == '\x1b[D':
                i = "-1,0,0"
            elif key == 'w':
                i = "0,0,1"
            elif key == 's':
                i = "0,0,-1"
            else:
                i = "q"

        if i == "q":
            yield Request(coordinates="Quit,"+name)
            print("Goodbye!")
            break
        try:
            if k > 1:
                req = str(i)
            else:
                if k == 1:
                    req = "Start,"+name+","+str(i)
                    k += 1
                if k == 0:
                    req = "Register,"+str(i)
                    name = str(i)
                    k += 1
        except ValueError:
            continue
        yield Request(coordinates=req)
        if k == 2:
            thread = threading.Thread(target=statcheck, args=(name,stub))
            thread.daemon = True
            thread.start()
            k += 1

        time.sleep(0.1)


def statcheck(name,stub):
    prev = [0, 0, 0]
    while True:
        current = [r.coordinates for r in stub.adjust(Request(coordinates=name))]
        if current != prev and len(current) > 0:
            print("New Position -", ",".join(current))
            prev = current[:]

def run():
    channel = grpc.insecure_channel('localhost:3000')
    stub = drone_pb2_grpc.DroneControlStub(channel)
    it = stub.movement(gen(stub))
    try:
        for r in it:
            print(r.coordinates)

    except Exception as err:
        print(err)



if __name__ == '__main__':
    #job_for_another_core = multiprocessing.Process(name='background_process', target=mapplot.plotmymap, args=())
    #job_for_another_core.daemon = True
    #job_for_another_core.start()
    #mainprocess = multiprocessing.Process(target=run, args=())
    #mainprocess.daemon = False
    #mainprocess.start()
    run()
