import time
import grpc
import drone_pb2
import drone_pb2_grpc
import json

from concurrent import futures

filepath = "/Users/nitomar/PycharmProjects/SP-18/Sithu - CMPE 273/Assignment-1/.ipynb_checkpoints/serverdata.json"


Drones = {}
Drones_Path = {}
class DroneServer(drone_pb2_grpc.DroneControlServicer):
    def adjust(self, r, context):
        if r.coordinates in Drones:
            yield drone_pb2.Response(coordinates=", ".join([str(c) for c in Drones[r.coordinates]]))
    def movement(self, request, context):
        f = open(filepath, "w")
        json.dump(Drones_Path,f)
        f.flush()
        for r in request:
            req = r.coordinates.split(',')
            if req[0] == "Register":
                if req[1] in Drones:
                    yield drone_pb2.Response(coordinates="Name already occupied, Quit and try again!")
                else:
                    Drones[req[1]] = [0,0,0]
                    Drones_Path[req[1]] = []
                    print("Client Joined: "+req[1])
                    yield drone_pb2.Response(coordinates="You are registered! Welcome "+req[1])
            elif req[0] == "Start":
                Drones[req[1]] = [req[2],req[3],req[4]]
                Drones_Path[req[1]].append([req[2],req[3],req[4]])
                f = open(filepath, "w")
                json.dump(Drones_Path, f)
                f.flush()
                yield drone_pb2.Response(coordinates="You are starting at - " + ",".join(Drones[req[1]]))
            elif req[0] == "Quit":
                print("Client Exit: "+req[1])
                del Drones[req[1]]
                del Drones_Path[req[1]]
                open(filepath, 'w').close()
                f = open(filepath, "w")
                json.dump(Drones_Path, f)
                f.flush()
            else:
                for drone in Drones:
                    l = Drones[drone]
                    change = r.coordinates.split(",")
                    l[0] = str(int(l[0]) + int(change[0]))
                    l[1] = str(int(l[1]) + int(change[1]))
                    l[2] = str(int(l[2]) + int(change[2]))
                    Drones[drone] = l
                    Drones_Path[drone].append(l[:])
                    open(filepath, 'w').close()
                    f = open(filepath,"w")
                    json.dump(Drones_Path,f)
                    f.flush()
                yield drone_pb2.Response(coordinates="")


def run(host, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    drone_pb2_grpc.add_DroneControlServicer_to_server(DroneServer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', 3000)