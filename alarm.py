import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import pygame
import webbrowser
import os
import sys

class AlarmClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Будильник")
        self.geometry("400x300")

        self.label = ttk.Label(self, text="Выберите время будильника:")
        self.label.pack(pady=10)

        self.time_entry = ttk.Entry(self)
        self.time_entry.insert(0, "             HH:MM")
        self.time_entry.pack(pady=5)

        self.set_button = ttk.Button(self, text="Установить будильник", command=self.set_alarm)
        self.set_button.pack(pady=10)
        self.label = ttk.Label(self, text="Установленные будильники")
        self.label.pack(pady=10)

        self.help_button = ttk.Button(self, text="Справка", command=self.show_help)
        self.help_button2 = ttk.Button(self, text="Лицензионне соглашение", command=self.show_lisence)

        self.help_button.pack(pady=10)
        self.help_button2.pack(pady=10)
        button = tk.Button(self, text="GitHub разработчика", command=self.open_website)

# Размещаем кнопку на главном окне
        button.pack()
        # Замените путь на свой звуковой файл
        self.sound_file = "Kanye West – On Sight.mp3"

    def set_alarm(self):
        alarm_time_str = self.time_entry.get().strip()  # Strip leading and trailing spaces
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
                # Reset the label text after the alarm triggers
                self.after((seconds_until_alarm + 5) * 1000, lambda: self.label.config(text="Установите будильник"))
            else:
                self.label["text"] = "Выберите будущее время"
                # Reset the label text after 5 seconds
                self.after(5000, lambda: self.label.config(text="Установите будильник"))
        except ValueError:
            self.label["text"] = "Неправильный формат времени"


    def play_alarm_sound(self):
        pygame.mixer.init()

        # Access the bundled file if running from the executable
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        sound_path = os.path.join(base_path, self.sound_file)

        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()

    def show_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Подъем!")
        popup.geometry("200x100")

        popup_label = ttk.Label(popup, text="Подъем!")
        popup_label.pack(pady=20)

        close_button = ttk.Button(popup, text="Закрыть", command=lambda: self.close_popup(popup))
        close_button.pack()

        # Bind the destruction of the popup to the window close event
        popup.protocol("WM_DELETE_WINDOW", lambda: self.close_popup(popup))

    def close_popup(self, popup):
        pygame.mixer.music.stop()  # Stop the music when closing the popup
        popup.destroy()

    def show_help(self):
        popup = tk.Toplevel(self)
        # Замените путь на свой файл со справкой
        popup_label = ttk.Label(popup, text="Автор программы - Харьковец Илья\nВерсия - 1.0.0!\nБудильник\nЧтобы установить будильник нужно \nввести время в нужном в формате, и нажать кнопку Установить будильник")
        popup_label.pack(pady=20)
        """try:
            #webbrowser.open(help_file_path)
        except Exception as e:
            print(f"Ошибка открытия файла со справкой: {e}")"""
    def show_lisence(self):
        popup1 = tk.Toplevel(self)
        popup_label2 = ttk.Label(popup1, text="""ЛИЦЕНЗИОННОЕ СОГЛАШЕНИЕ

        ВНИМАНИЕ: ПРОЧИТАЙТЕ ДАННОЕ СОГЛАШЕНИЕ ВНИМАТЕЛЬНО, ПЕРЕД ТЕМ КАК ИСПОЛЬЗОВАТЬ ДАННОЕ ПРИЛОЖЕНИЕ.

        ЛИЦЕНЗИЯ
        1.1 Предоставление прав: Настоящим, разработчик предоставляет вам ограниченную, неисключительную, непередаваемую лицензию на установку, 
        использование и воспроизведение приложения "Будильник" (далее – "Приложение").
        1.2 Ограничения: Вы не имеете права модифицировать, декомпилировать, дизассемблировать, обратно разрабатывать, создавать производные работы, 
        распространять, лицензировать, передавать или продавать любые компоненты Приложения или использовать их в коммерческих целях без предварительного письменного согласия разработчика.

        АВТОРСКИЕ ПРАВА
        2.1 Владение правами: Разработчик остается владельцем всех прав на интеллектуальную собственность в отношении Приложения, включая, но не ограничиваясь, авторские права.
        2.2 Защита прав: Вы соглашаетесь не совершать действий, направленных на нарушение авторских прав или интеллектуальной собственности разработчика в отношении Приложения.

        ГАРАНТИИ И ОТВЕТСТВЕННОСТЬ
        3.1 Отказ от гарантий: Приложение предоставляется "как есть" без каких-либо гарантий, явных или подразумеваемых. 
        Разработчик не гарантирует бесперебойную работу Приложения или его соответствие вашим требованиям.
        3.2 Ограничение ответственности: Разработчик не несет ответственности за любые убытки или ущерб, возникшие в результате использования или невозможности использования Приложения, 
        даже если разработчик был уведомлен о возможности такого ущерба.

        ЗАВЕРЕНИЕ И РАСТОРЖЕНИЕ
        4.1 Заверение: Вы заверяете, что вы будете использовать Приложение только в соответствии с применимыми законами и положениями настоящего Лицензионного соглашения.
        4.2 Расторжение: Разработчик оставляет за собой право расторгнуть данную лицензию в случае вашего нарушения какого-либо условия настоящего Соглашения.

        ЗАКЛЮЧИТЕЛЬНЫЕ ПОЛОЖЕНИЯ
        5.1 Применимое право: Данное Соглашение регулируется законами той юрисдикции, в которой разработчик зарегистрирован.
        5.2 Изменения: Разработчик оставляет за собой право изменять условия настоящего Соглашения. Изменения вступают в силу с момента их публикации на официальном веб-сайте разработчика.

        5.3 Полное соглашение: Настоящее Соглашение представляет собой полное соглашение между вами и разработчиком 
        относительно предмета Соглашения и заменяет все предыдущие устные или письменные соглашения между вами и разработчиком.""")
        popup_label2.pack(pady=20)
    def open_website(self):
        webbrowser.open("https://github.com/paladinxb")

if __name__ == "__main__":
    app = AlarmClock()
    app.mainloop()
