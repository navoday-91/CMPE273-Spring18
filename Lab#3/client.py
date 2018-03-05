import grpc, time, sys
import drone_pb2_grpc
import drone_pb2

drones = {}
droneid = 0

def move_stub(r):
    global i
    i = 0
    print('Client ID: ', r.num, 'connected to server')
    global droneid
    droneid = r.num
    print('Received ', r.coords)
    print('Moving to ', r.coords)
    drones[i] = {'ID': r.num, 'Coordinates': r.coords}
    print(drones[i])
    i += 1


def adjust_stub(r):
    global droneid
    if droneid == r.num:
        d = {'ID': r.num, 'Coordinates': r.coords}
        print('Received ', r.coords)
        print('Moving to ', r.coords)
        print(d)


def run():
    channel = grpc.insecure_channel('localhost:3000')
    stub = drone_pb2_grpc.MoveDroneStub(channel)
    response = stub.move(drone_pb2.Request())
    for r in response:
        if r.mode == 'M' or (not r.mode):
            move_stub(r)
        elif r.mode == 'A':
            adjust_stub(r)

    while True:
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            sys.exit()


if __name__ == '__main__':
    run()
