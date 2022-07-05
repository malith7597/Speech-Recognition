from cmath import polar
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import requests
import time
import sys

filename = sys.argv[1]
API_KEY = "75e9f2ce5bb6411b963183d39bdad999"
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
headers = {"authorization": API_KEY, "content-type": "application/json"}


def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    headers = {'authorization': API_KEY}
    response = requests.post(upload_endpoint,
                             headers=headers,
                             data=read_file(filename))
    audio_url = response.json()['upload_url']
    return audio_url


# transcription
def transcribe(audio_url):
    json = {"audio_url": audio_url}
    transcript_response = requests.post(
        transcript_endpoint, json=json, headers=headers)
    job_id = transcript_response.json()['id']
    return job_id


# poll
# calling the functions
""" audio_url = upload(filename)
job_id = transcribe(audio_url)
print(job_id)
 """
# polling


def poll(job_id):
    polling_endpoint = transcript_endpoint+'/'+job_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()


def get_transcription_result_url(audio_url):
    transcription_id = transcribe(audio_url)
    while(True):
        data = poll(transcription_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
        print('Waiting 30 seconds')
        time.sleep(30)


def save_transcript(audio_url):
    data, error = get_transcription_result_url(audio_url)
    print(data)

    if data:
        text_filename = filename+'.txt'
        with open(text_filename, 'w') as f:
            f.write(data['text'])
        print('transcription is saved!')

    if error:
        print("Error!!", error)


audio_url = upload(filename)
save_transcript(audio_url)
