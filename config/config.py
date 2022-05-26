import os
import cv2

MODEL = 'hog'
DATAPATH = r'/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/face_recognition/'
KNOWN_PATH = os.path.join(DATAPATH,'known_face')
INPUT_PATH = os.path.join(DATAPATH, 'input_face')
VIDEO_PATH = r'/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/video_for_vision_experiment'
VIDEO = os.path.join(VIDEO_PATH, 'Jeff_video.mp4')
COLOR = cv2.COLOR_BGR2RGB
FONT = cv2.FONT_HERSHEY_SIMPLEX
