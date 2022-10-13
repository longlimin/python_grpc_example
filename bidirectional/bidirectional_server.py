from concurrent import futures

import grpc
import bidirectional.bidirectional_pb2_grpc as bidirectional_pb2_grpc


class BidirectionalService(bidirectional_pb2_grpc.BidirectionalServicer):

    def GetServerResponse(self, request_iterator, context):
        print("Server: Received client request...")
        for message in request_iterator:
            print(f" -- Client: {message}")
            print(" -- Server: Responding...")
            print("-------------------------")
            yield message


def serve():
    print("Server: Serving ...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bidirectional_pb2_grpc.add_BidirectionalServicer_to_server(BidirectionalService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server: Starting ...")
    server.start()
    print("Server: Started")
    server.wait_for_termination()
    print("Server: Terminated")


if __name__ == '__main__':
    serve()
