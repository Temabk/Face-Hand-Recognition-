import cv2
import face_recognition
import tkinter as tk
from tkinter import simpledialog, messagebox
import os


def process_frame(frame, face_locations):
    """
    Обрабатывает один кадр, распознает лица и обновляет список face_locations.

    :param frame: Кадр видео (или изображение), в котором нужно найти лица.
    :type frame: numpy.ndarray
    :param face_locations: Список для хранения координат найденных лиц.
    :type face_locations: list
    :raises TypeError: Если кадр передан как None
    """
    if frame is None:
        raise TypeError("Кадр не может быть None")

    rgb_frame = frame[:, :, ::-1]
    detected_faces = face_recognition.face_locations(rgb_frame)
    face_locations.clear()
    face_locations.extend(detected_faces)


def detect_faces_from_webcam():
    """
    Обнаруживает лица с веб-камеры в реальном времени.

    :raises ValueError: Если не удается открыть веб-камеру.
    """
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Не удалось открыть веб-камеру.")
        raise ValueError("Не удалось открыть веб-камеру")

    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    frame_skip = 3
    frame_count = 0
    face_locations = []

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Не удалось получить кадр с веб-камеры.")
            break

        if frame_count % frame_skip == 0:
            process_frame(frame, face_locations)

        for top, right, bottom, left in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        number_of_faces = len(face_locations)
        text = f"Faces: {number_of_faces}"
        font_scale = 1.5
        font_thickness = 3
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
        text_x = 10
        text_y = 30 + text_size[1]

        cv2.rectangle(frame, (text_x - 10, text_y - text_size[1] - 10),
                      (text_x + text_size[0] + 10, text_y + 10),
                      (0, 0, 0), -1)
        cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX,
                    font_scale, (255, 255, 255), font_thickness)

        cv2.imshow('Webcam Face Detection', frame)
        frame_count += 1

        if cv2.waitKey(1) & 0xFF == 27:
            break

    video_capture.release()
    cv2.destroyAllWindows()