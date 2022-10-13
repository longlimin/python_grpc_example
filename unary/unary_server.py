import grpc
from concurrent import futures
import time
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2


class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        print("Server: Received GetServerResponse message. Processing...")
        # get the string from the incoming request
        print("-- Request: " + str(request))
        # print("-- Context: " + str(context))
        message = request.message
        result = f'Server: Hello Client! I received your message: "{message}". Yes, I am running and healthy!'
        result = {'message': result, 'received': True}

        print(f"-- Responding to Client with message: \"{result.get('message')}\"")
        return pb2.MessageResponse(**result)


def serve():
    print("Server: Serving...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server: Starting...")
    server.start()
    print("Server: Started")
    server.wait_for_termination()
    print("Server: Terminated")


if __name__ == '__main__':
    serve()
