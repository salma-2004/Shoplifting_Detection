from django.db import models

# Create your models here.
import tensorflow as tf
import numpy as np
import cv2

IMAGE_HEIGHT, IMAGE_WIDTH = 64, 64
SEQUENCE_LENGTH = 20
MODEL_PATH = "detection/model/convLSTM_shoplifting_model.h5"

model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_video(video_path):
    frames_list = []
    video_reader = cv2.VideoCapture(video_path)
    video_frames_count = int(video_reader.get(cv2.CAP_PROP_FRAME_COUNT))
    skip_frames_window = max(int(video_frames_count/SEQUENCE_LENGTH), 1)

    for frame_counter in range(SEQUENCE_LENGTH):
        video_reader.set(cv2.CAP_PROP_POS_FRAMES, frame_counter * skip_frames_window)
        success, frame = video_reader.read()
        if not success:
            break
        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH)) / 255.0
        frames_list.append(resized_frame)

    video_reader.release()

    return np.array(frames_list[:SEQUENCE_LENGTH], dtype=np.float32)

def predict(video_path):
    input_video = preprocess_video(video_path)
    input_video = np.expand_dims(input_video, axis=0)
    prediction = model.predict(input_video)[0]
    return {"shoplifting_probability": float(prediction)}
