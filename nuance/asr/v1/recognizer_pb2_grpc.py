# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nuance.asr.v1 import recognizer_pb2 as nuance_dot_asr_dot_v1_dot_recognizer__pb2


class RecognizerStub(object):
    """
    Streaming recognition service API.  
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recognize = channel.stream_stream(
                '/nuance.asr.v1.Recognizer/Recognize',
                request_serializer=nuance_dot_asr_dot_v1_dot_recognizer__pb2.RecognitionRequest.SerializeToString,
                response_deserializer=nuance_dot_asr_dot_v1_dot_recognizer__pb2.RecognitionResponse.FromString,
                )


class RecognizerServicer(object):
    """
    Streaming recognition service API.  
    """

    def Recognize(self, request_iterator, context):
        """Starts a recognition request and returns a response. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecognizerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Recognize': grpc.stream_stream_rpc_method_handler(
                    servicer.Recognize,
                    request_deserializer=nuance_dot_asr_dot_v1_dot_recognizer__pb2.RecognitionRequest.FromString,
                    response_serializer=nuance_dot_asr_dot_v1_dot_recognizer__pb2.RecognitionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nuance.asr.v1.Recognizer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Recognizer(object):
    """
    Streaming recognition service API.  
    """

    @staticmethod
    def Recognize(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/nuance.asr.v1.Recognizer/Recognize',
            nuance_dot_asr_dot_v1_dot_recognizer__pb2.RecognitionRequest.SerializeToString,
            nuance_dot_asr_dot_v1_dot_recognizer__pb2.RecognitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
