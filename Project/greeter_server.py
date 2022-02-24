from concurrent import futures
import logging
from operator import mod

import grpc
import ServerBody_pb2
import ServerBody_pb2_grpc

import json 
import VideoModel

class Body(ServerBody_pb2_grpc.BodyServicer):

    def GetVideos(self, request, context):
        if(request.filter in "ListVideos"):
            buildJSON = json.dumps(VideoModel.getVideoList())
            return ServerBody_pb2.VideoReply(json=buildJSON)
        else:
            return ServerBody_pb2.VideoReply(json=json.dumps({"state" :"false"}))

    def GetVideosX(self, request, context):
        ReplayData = []
        modelSource = None

        if(request.filter in "ListVideos1"):
            modelSource = VideoModel.getVideoList1()
        if(request.filter in "ListVideos2"):
            modelSource = VideoModel.getVideoList2()
        if(request.filter in "ListVideos3"):
            modelSource = VideoModel.getVideoList3()

        for mdl in modelSource:
            model = ServerBody_pb2.VideoListXModel()
            model.ID =              mdl['ID']
            model.Name =            mdl['Name']
            model.Description =     mdl['Description']
            model.Picture =         mdl['Picture']
            model.Views =           mdl['Views']
            ReplayData.append(model)

        return ServerBody_pb2.VideoListXReply(VideoListX=ReplayData)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ServerBody_pb2_grpc.add_BodyServicer_to_server(Body(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running... :50051")
    print("ServerBody_pb2.VideoListXRequest(filter='ListVideos1')")
    print("ServerBody_pb2.VideoListXRequest(filter='ListVideos2')")
    print("ServerBody_pb2.VideoListXRequest(filter='ListVideos3')")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
