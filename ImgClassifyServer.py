import ImgClassify_pb2_grpc as users_service
import ImgClassify_pb2 as users_messages
import grpc
import time
import concurrent.futures as futures

_ONE_DAY_IN_SECONDS = 24*60*60


class UsersService(users_service.ClassifyServiceServicer):

    def ClassifyImages(self, request_iterator, context):
        for new_img in request_iterator:
            print('img_received')
            print(new_img.num_img)
            classified = users_messages.classified(
                num_img=233, classes='classified'
            )
            yield classified


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_service.add_ClassifyServiceServicer_to_server(UsersService(), server)
    server.add_insecure_port('localhost:8080')
    server.start()
    try:
        while 1:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
