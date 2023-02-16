from concurrent import futures
import logging
from operator import mod
from traceback import print_list

import grpc
import ServerBody_pb2
import ServerBody_pb2_grpc

import json 
import VideoModel

class Body(ServerBody_pb2_grpc.BodyServicer):
    
    def getModelData(self, modelSource):
        ReplayData = []
        for mdl in modelSource:
            model = ServerBody_pb2.VideoListXModel()
            model.ID =              mdl['ID']
            model.Name =            mdl['Name']
            model.Description =     mdl['Description']
            model.Picture =         mdl['Picture']
            model.Category =        mdl['Category']
            model.Views =           mdl['Views']
            model.Year =            mdl['Year']
            model.Director =        mdl['Director']
            model.Cast =            mdl['Cast']
            ReplayData.append(model)
        return ReplayData


    def GetVideosX(self, request, context):
        modelSource = None

        if(request.filter in "All"):
            modelSource = VideoModel.getVideoList()
        else:
            modelSource = [model for model in VideoModel.getVideoList() if model["Category"] == request.filter]

        ReplayData = self.getModelData(modelSource)
        
        return ServerBody_pb2.VideoListXReply(VideoListX=ReplayData)


    def SearchVideosX(self, request, context):
        modelSource = None

        requestFilter = str(request.filter.lower()).split()

        modelSource = [model for model in VideoModel.getVideoList() if any(ele in model["Name"].lower() for ele in requestFilter)]
        
        ReplayData = self.getModelData(modelSource)

        return ServerBody_pb2.VideoListXReply(VideoListX=ReplayData)


    def GetHeadersX(self, request, context):
        ReplayData = []
        modelSource = None

        modelSource = VideoModel.getVideoHeaders()

        for mdl in modelSource:
            model = ServerBody_pb2.VideoHeaderXModel()
            model.ID_VIDEO =        mdl['ID_VIDEO']
            model.Name =            mdl['Name']
            model.Description =     mdl['Description']
            model.Picture =         mdl['Picture']
            ReplayData.append(model)

        return ServerBody_pb2.VideoHeaderXReply(VideoHeaderX=ReplayData)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ServerBody_pb2_grpc.add_BodyServicer_to_server(Body(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running... :50051")
    print("Videos", "filter", [VideoModel.C_ALL, VideoModel.C_SERIALS, VideoModel.C_FANTASY, VideoModel.C_ACTION, VideoModel.C_COMEDY, VideoModel.C_DRAMA, VideoModel.C_POPULAR, VideoModel.C_HORROR])
    print("Headers")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
