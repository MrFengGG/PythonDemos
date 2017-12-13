import cv2
import numpy
import time

class CaptureManager(object):
    def __init__(self,capture,previewWindowManager = None,shouldMirrorPreview = False):
        self.previewWindowManager = previewWindowManager
        self.shouldMirrorPreview = shouldMirrorPreview

        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFilename = None
        self.videoFilename = None
        self._videoEcoding = None
        self._videoWriter = None

        self.startTime = None
        self.framesElapsed = int(0)
        self.fpsEstimate = None
        

