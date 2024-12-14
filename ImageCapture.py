import cv2
import face_recognition
import tkinter as tk
from tkinter import simpledialog, messagebox
import os

def detect_faces_from_image(image_path):
    """
    Обнаруживает лица на изображении.

    :param image_path: Путь к изображению, на котором нужно обнаружить лица.
    :type image_path: str
    :raises Exception: Если изображение не удается загрузить.
    """
    try:
        image = face_recognition.load_image_file(image_path)
    except Exception as e:
        print(f"Ошибка загрузки изображения: {e}")
        return

    rgb_image = image[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_image)
    image_with_boxes = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(image_with_boxes, (left, top), (right, bottom), (0, 255, 0), 2)

    number_of_faces = len(face_locations)
    text = f"faces: {number_of_faces}"
    font_scale = 1.5
    font_thickness = 3
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
    text_x = 10
    text_y = 30 + text_size[1]

    cv2.rectangle(image_with_boxes, (text_x - 10, text_y - text_size[1] - 10),
                  (text_x + text_size[0] + 10, text_y + 10),
                  (0, 0, 0), -1)

    cv2.putText(
        image_with_boxes,
        text,
        (text_x, text_y),
        cv2.FONT_HERSHEY_SIMPLEX,
        font_scale,
        (255, 255, 255),
        font_thickness
    )

    print(f"Количество найденных лиц: {number_of_faces}")
    cv2.imshow("Image Face Detection", image_with_boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()