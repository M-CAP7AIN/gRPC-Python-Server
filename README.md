# gRPC Server

This is a sample protobuf (proto3) file for a gRPC server that provides two methods for retrieving and searching video data. 

## Service Definition

The `Body` service contains the following RPC methods:

1. `GetVideosX`: Retrieves a list of videos that match a given filter.
2. `SearchVideosX`: Searches for videos that match a given filter.

Both methods take a `VideoListXRequest` object as input and return a `VideoListXReply` object as output.

Additionally, the `Body` service contains the `GetHeadersX` method, which retrieves header information for a given video. This method takes a `VideoHeaderXRequest` object as input and returns a `VideoHeaderXReply` object as output.

## Message Definitions

The `VideoListXRequest` and `VideoHeaderXRequest` messages both contain a single field, `filter`, which is used to filter the results of the corresponding method.

The `VideoListXReply` message contains a repeated field, `VideoListX`, which is a list of `VideoListXModel` objects. Each `VideoListXModel` object represents a single video and contains the following fields:

- `ID`: An integer ID for the video.
- `Name`: The name of the video.
- `Description`: A brief description of the video.
- `Picture`: A URL pointing to an image of the video.
- `Category`: The category of the video.
- `Views`: The number of views the video has received.
- `Year`: The year the video was released.
- `Director`: The name of the video's director.
- `Cast`: A comma-separated list of actors in the video.

The `VideoHeaderXReply` message contains a repeated field, `VideoHeaderX`, which is a list of `VideoHeaderXModel` objects. Each `VideoHeaderXModel` object represents a header for a single video and contains the following fields:

- `ID`: An integer ID for the header.
- `ID_VIDEO`: An integer ID for the corresponding video.
- `Name`: The name of the video.
- `Description`: A brief description of the video.
- `Picture`: A URL pointing to an image of the video.

## Model

The `VideoModel.py` is a Python script that stores data of gRPC.


# Installation

To use this proto file, you will need to generate client and server code using a protobuf compiler. Once you have generated the code, you can use the `Body` service to retrieve and search for video data.

To run this project, you need to install gRPC and its dependencies. You can install them using pip:

```
pip install grpcio
pip install grpcio-tools
pip install protobuf
```

## Usage

This project includes a `buildProto.bat` file in `Project` folder that generates Python code from the Protocol Buffer definition file (`ServerBody.proto`). You can run it to generate the necessary files:

```
buildProto.bat
```

This will generate the `greeter_pb2.py` and `greeter_pb2_grpc.py` files.

To run the gRPC server, use the `greeter_server.py` script:

```
python greeter_server.py
```

This will start the server on port `50051`.

To run the gRPC client, use the `greeter_client.py` script:

```
python greeter_client.py
```

This will send a request to the server and print the response.




# Android Application 

This is (https://github.com/amirhusseinSSoori/Grpc_Redux_Movies_Compose) an Android sample application that demonstrates the use of gRPC and Redux architecture with Jetpack Compose to display a list of movies and their details.
