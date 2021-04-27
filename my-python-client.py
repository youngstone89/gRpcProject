#!/usr/bin/env python3

import sys, wave, grpc, traceback
from time import sleep
from nuance.asr.v1.resource_pb2 import *
from nuance.asr.v1.result_pb2 import *
from nuance.asr.v1.recognizer_pb2 import *
from nuance.asr.v1.recognizer_pb2_grpc import *

# Declare a DLM that exists in a Mix project
travel_dlm = RecognitionResource(
    external_reference = ResourceReference(
        type='DOMAIN_LM',
        uri='urn:nuance-mix:tag:model/<context_tag>/mix.asr?=language=eng-USA'),
    reuse='HIGH_REUSE',
    weight_value=0.7)

# Declare an inline wordset for an entity in that DLM
places_wordset = RecognitionResource(
    inline_wordset='{"PLACES":[{"literal":"La Jolla","spoken":["la hoya"]},{"literal":"Llanfairpwllgwyngyll","spoken":["lan vire pool guin gill"]},{"literal":"Abington Pigotts"},{"literal":"Steeple Morden"},{"literal":"Hoyland Common"},{"literal":"Cogenhoe","spoken":["cook no"]},{"literal":"Fordoun","spoken":["forden"]},{"literal":"Llangollen","spoken":["lan-goth-lin","lhan-goth-luhn"]},{"literal":"Auchenblae"}]}',
    reuse='HIGH_REUSE')

# Send recognition request parameters and audio
def client_stream(wf):
    try:
        # Set recognition parameters
        init = RecognitionInitMessage(
            parameters = RecognitionParameters(
                language='en-US',
                audio_format=AudioFormat(pcm=PCM(sample_rate_hz=wf.getframerate())),
                result_type='FINAL',
                utterance_detection_mode='MULTIPLE',
                recognition_flags = RecognitionFlags(auto_punctuate=True)),
            # resources = [ travel_dlm, places_wordset ],
            client_data = {'company':'Aardvark','user':'Leslie'}
        )
        yield RecognitionRequest(recognition_init_message=init)

        # Simulate a realtime audio stream using an audio file
        print(f'stream {wf.name}')
        packet_duration = 0.020
        packet_samples = int(wf.getframerate() * packet_duration)
        for packet in iter(lambda: wf.readframes(packet_samples), b''):
            yield RecognitionRequest(audio=packet)
            sleep(packet_duration)
        print('stream complete')
    except CancelledError as e:
        print(f'client stream: RPC canceled')
    except Exception as e:
        print(f'client stream: {type(e)}')
        traceback.print_exc()

# Collect arguments from user
hostaddr = access_token = audio_file = None
try:
    hostaddr = sys.argv[1]
    access_token = sys.argv[2]
    audio_file = sys.argv[3]
except Exception as e:
    print(f'usage: {sys.argv[0]} <hostaddr> <token> <audio_file.wav>')
    exit(1)

# Check audio file attributes and open secure channel with token
with wave.open(audio_file, 'r') as wf:
    assert wf.getsampwidth() == 2, f'{audio_file} is not linear PCM'
    assert wf.getframerate() in [8000, 16000], f'{audio_file} sample rate must be 8000 or 16000'
    assert wf.getnchannels() == 1, f'{audio_file} is not a mono audio file'
    setattr(wf, 'name', audio_file)
    call_credentials = grpc.access_token_call_credentials(access_token)
    ssl_credentials = grpc.ssl_channel_credentials()
    channel_credentials = grpc.composite_channel_credentials(ssl_credentials, call_credentials)
    with grpc.secure_channel(hostaddr, credentials=channel_credentials) as channel:
        stub = RecognizerStub(channel)
        stream_in = stub.Recognize(client_stream(wf))
        try:
            # Iterate through messages returned from server
            for message in stream_in:
                if message.HasField('status'):
                    if message.status.details:
                         print(f'{message.status.code} {message.status.message} - {message.status.details}')
                    else:
                         print(f'{message.status.code} {message.status.message}')
                elif message.HasField('result'):
                    restype = 'partial' if message.result.result_type else 'final'
                    print(f'{restype}: {message.result.hypotheses[0].formatted_text}')
        except StreamClosedError:
            pass
        except Exception as e:
            print(f'server stream: {type(e)}')
            traceback.print_exc()