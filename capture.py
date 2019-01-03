import logging

import multiprocessing
import time
from multiprocessingloghandler import ChildMultiProcessingLogHandler
import threading
from fedstream import FedStream
import pyaudio
import array
import Queue
import io
import os
import sys
import grpc  # for error types returned by the client
from google.cloud import speech

# Setup audio and cloud speech
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
FRAMES_PER_BUFFER = 4096
PAUSE_LENGTH_SECS = 1.0
MAX_BUFFERED_SAMPLES = 1
PAUSE_LENGTH_IN_SAMPLES = int((PAUSE_LENGTH_SECS * RATE / FRAMES_PER_BUFFER) + 0.5)
SAMPLE_RETRY_DELAY_SECS = 0.1

# This is how many samples to take to find the lowest sound level
SILENCE_TRAINING_SAMPLES = 10

class SpeechRecognizer(multiprocessing.Process):
    def __init__(self, transcript, log_queue, logging_level):
        multiprocessing.Process.__init__(self)
        self._log_queue = log_queue
        self._logging_level = logging_level
        self._exit = multiprocessing.Event()
        self._suspend_listening = multiprocessing.Event()
        self._transcript, _ = transcript
        self._stop_capturing = False
        self._stop_recognizing = False
        self._audio_buffer = Queue.Queue()

    def stop(self):
        logging.debug("***background received shutdown")
        self._exit.set()

    def captureSound(self):
        logging.debug("starting capturing")
        mic_stream = self._audio.open(format=FORMAT, channels=CHANNELS,
            rate=RATE, input=True,
            frames_per_buffer=FRAMES_PER_BUFFER)

        self.trainSilence(mic_stream)
            samples += 1
            volume = 0
            try:
                data = mic_stream.read(FRAMES_PER_BUFFER)
                if self._stop_listening:
                    continue
                volume = max(array.array('h', data))
                logging.debug("Volume max {}".format(volume))
            except IOError, e:
                logging.exception("IOError capturing audio")
        logging.debug("ending sound capture")
        # stop Recording
        mic_stream.stop_stream()
        mic_stream.close()
        self._audio.terminate()
        logging.debug("stopped capturing")

def main():
    self._audio = pyaudio.PyAudio()
    logging.debug("recognizer process active")
    self._recognizer.start()
    self._suspend_listening.clear()
    self._capturer.start()
    self._exit.wait()

