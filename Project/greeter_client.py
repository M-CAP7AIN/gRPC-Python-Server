from __future__ import print_function

import logging

import grpc
import ServerBody_pb2
import ServerBody_pb2_grpc



def getModelList():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ServerBody_pb2_grpc.BodyStub(channel)
        response = stub.GetVideos(ServerBody_pb2.VideoRequest(filter='ListVideos'))
    print(response.json)


def getModelList1():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ServerBody_pb2_grpc.BodyStub(channel)
        response = stub.GetVideosX(ServerBody_pb2.VideoListXRequest(filter='ListVideos1'))
        #print(response.VideoList1[1])    
        print(response.VideoListX)   


if __name__ == '__main__':
    logging.basicConfig()
    getModelList1()
