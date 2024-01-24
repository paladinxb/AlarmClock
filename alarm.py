import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import pygame
import webbrowser

class AlarmClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Будильник")
        self.geometry("300x200")

        self.label = ttk.Label(self, text="Выберите время будильника:")
        self.label.pack(pady=10)

        self.time_entry = ttk.Entry(self)
        self.time_entry.insert(0, "HH:MM")
        self.time_entry.pack(pady=5)

        self.set_button = ttk.Button(self, text="Установить будильник", command=self.set_alarm)
        self.set_button.pack(pady=10)

        self.help_button = ttk.Button(self, text="Справка", command=self.show_help)
        self.help_button.pack(pady=10)

        # Замените путь на свой звуковой файл
        self.sound_file = "D:\\Coding\\Alarmclock\\Kanye West – On Sight.mp3"

    def set_alarm(self):
        alarm_time_str = self.time_entry.get()
        try:
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M").time()
            current_time = datetime.now().time()

            # Создаем объект datetime с текущей датой и временем будильника
            combined_datetime = datetime.combine(datetime.today(), alarm_time)

            # Проверяем, если будильник на следующий день, то прибавляем 1 день
            if combined_datetime < datetime.now():
                combined_datetime += timedelta(days=1)

            delta = combined_datetime - datetime.now()
            seconds_until_alarm = delta.seconds

            if seconds_until_alarm > 0:
                # Устанавливаем таймер для воспроизведения песни и отображения всплывающего окна
                self.after(seconds_until_alarm * 1000, self.play_alarm_sound)
                self.after(seconds_until_alarm * 1000, self.show_popup)
                self.label["text"] = "Будильник установлен"
            else:
                self.label["text"] = "Выберите будущее время"
        except ValueError:
            self.label["text"] = "Неправильный формат времени"

    def play_alarm_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.sound_file)
        pygame.mixer.music.play()

    def show_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Подъем!")
        popup.geometry("200x100")

        popup_label = ttk.Label(popup, text="Подъем!")
        popup_label.pack(pady=20)

        close_button = ttk.Button(popup, text="Закрыть", command=popup.destroy)
        close_button.pack()

    def show_help(self):
        # Замените путь на свой файл со справкой
        help_file_path = "D:\\Coding\\Alarmclock\\help.txt"
        
        try:
            webbrowser.open(help_file_path)
        except Exception as e:
            print(f"Ошибка открытия файла со справкой: {e}")

if __name__ == "__main__":
    app = AlarmClock()
    app.mainloop()
