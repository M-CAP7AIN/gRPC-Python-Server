from __future__ import print_function

import logging

import grpc
import ServerBody_pb2
import ServerBody_pb2_grpc

import VideoModel

def getModelList():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ServerBody_pb2_grpc.BodyStub(channel)
        response = stub.GetVideosX(ServerBody_pb2.VideoListXRequest(filter=VideoModel.C_ALL))  
        print(response.VideoListX)   

def SearchModelList():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ServerBody_pb2_grpc.BodyStub(channel)
        response = stub.SearchVideosX(ServerBody_pb2.VideoListXRequest(filter="Spider"))  
        print(response.VideoListX)   


def getModelHeaders():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ServerBody_pb2_grpc.BodyStub(channel)
        response = stub.GetHeadersX(ServerBody_pb2.VideoHeaderXRequest())
        print(response.VideoHeaderX)   


if __name__ == '__main__':
    logging.basicConfig()
    print("\n\n", "ListVideos") 
    getModelList()
    print("\n\n", "ListHeader") 
    getModelHeaders()
    print("\n\n", "SearchVideo") 
    SearchModelList()
    
