import cv2
import face_recognition
import tkinter as tk
from tkinter import simpledialog, messagebox
import os

def main():
    """
    Главная функция, которая запускает приложение и позволяет выбрать режим работы программы.

    :raises ValueError: Если сделан неверный выбор в меню.
    """
    root = tk.Tk()
    root.withdraw()

    default_image_path = "image_test.jpg"
    if not os.path.exists(default_image_path):
        print(f"Файл {default_image_path} не найден в папке с кодом.")
        messagebox.showerror("Ошибка", f"Файл {default_image_path} не найден в папке с кодом.")
        return

    while True:
        choice = simpledialog.askstring(
            "Выбор режима",
            "Выберите режим нейросети:\n1 - Обнаружение лиц с веб-камеры\n2 - Обнаружение лиц на изображении\n3 - Выход",
        )

        if choice == '1':
            print("Запуск обнаружения лиц с веб-камеры...")
            detect_faces_from_webcam()

        elif choice == '2':
            print(f"Использование изображения: {default_image_path}")
            detect_faces_from_image(default_image_path)

        elif choice == '3':
            print("Выход из программы.")
            messagebox.showinfo("Выход", "Выход из программы.")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")
            messagebox.showerror("Ошибка", "Неверный ввод, попробуйте снова.")
            raise ValueError


if __name__ == "__main__":
    main()