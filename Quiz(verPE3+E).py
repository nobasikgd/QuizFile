import tkinter as tk
from tkinter import messagebox
import random


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение для изучения компонентов компьютера")
        self.root.geometry("700x500")
        self.root.minsize(650, 450)

        # Центрируем окно при запуске
        self.center_window()

        # Создаем контейнер для фреймов
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        # Настраиваем веса для растягивания
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Создаем все страницы
        for F in (StartPage, SecondPage, QuizPage, TheoryPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

        # Сбрасываем викторину при каждом входе на страницу с викториной
        if page_name == "QuizPage":
            frame.reset_quiz()

    def center_window(self):
        """Центрирует окно на экране"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Настраиваем веса для растягивания
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        label = tk.Label(self, text="Приложение для изучения компонентов компьютера", font=("Arial", 18))
        label.grid(row=1, column=1, pady=40, sticky="n")

        # Фрейм для кнопок с центрированием
        button_frame = tk.Frame(self)
        button_frame.grid(row=2, column=1, sticky="n")

        btn_next = tk.Button(button_frame, text="Начать",
                             command=lambda: controller.show_frame("SecondPage"),
                             width=15, height=2, font=("Arial", 14))
        btn_next.pack(pady=10)

        btn_exit = tk.Button(button_frame, text="Выход",
                             command=self.quit_app,
                             width=15, height=2, font=("Arial", 14))
        btn_exit.pack(pady=10)

    def quit_app(self):
        if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
            self.controller.root.destroy()


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Настраиваем веса для растягивания
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        label = tk.Label(self, text="Выберите режим", font=("Arial", 18))
        label.grid(row=1, column=1, pady=20, sticky="n")

        # Фрейм для кнопок с центрированием
        button_frame = tk.Frame(self)
        button_frame.grid(row=2, column=1, sticky="n")

        btn_theory = tk.Button(button_frame, text="Теория",
                               command=lambda: controller.show_frame("TheoryPage"),
                               width=15, height=2, font=("Arial", 14))
        btn_theory.pack(pady=10)

        btn_quiz = tk.Button(button_frame, text="Практика",
                             command=lambda: controller.show_frame("QuizPage"),
                             width=15, height=2, font=("Arial", 14))
        btn_quiz.pack(pady=10)

        btn_back = tk.Button(self, text="Назад",
                             command=lambda: controller.show_frame("StartPage"),
                             width=10)
        btn_back.grid(row=3, column=1, pady=10, sticky="s")


class QuizPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Сохраняем исходный цвет фона
        self.original_bg = self.cget('bg')

        # Настраиваем веса для растягивания
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Оригинальные вопросы (не перемешанные)
        self.original_questions = [
            {
                "question": "Как называется 'мозг' компьютера?",
                "options": ["Процессор", "Видеокарта", "Жесткий диск", "Материнская плата"],
                "answer": "Процессор",
            },
            {
                "question": "Правильное название скорости работы процессора?",
                "options": ["Тактовая частота", "Оперативная память", "Вычислительная мощность", "Быстродействие"],
                "answer": "Тактовая частота",
            },
            {
                "question": "Название основного хранилища данных в компьютере?",
                "options": ["Чипсет", "Жесткий диск", "RAM", "DIMM"],
                "answer": "Жесткий диск",
            },
            {
                "question": "Какой компонент отвечает за формирование изображения на мониторе?",
                "options": ["Монитор", "Видеокарта", "Материнская плата", "Процессор"],
                "answer": "Видеокарта",
            },
            {
                "question": "Какой тип диска не имеет подвижных частей?",
                "options": ["HDD", "DRAM", "SSD", "NVMe"],
                "answer": "SSD",
            },
            {
                "question": "Какое название у основного радиатора с вентилятором на процессоре?",
                "options": ["Сокет", "Кулер", "Ригель", "СНиП"],
                "answer": "Кулер",
            },
            {
                "question": "Операционная система в компьютере по умолчанию?",
                "options": ["ее нет", "Linux", "DOS", "Windows"],
                "answer": "DOS",
            },
            {
                "question": "На что указывает цвет разъема USB?",
                "options": ["Объем энергопотребления", "Ничего не указывает", "Типы данных для передачи", "Скорость передачи данных"],
                "answer": "Скорость передачи данных",
            },
            {
                "question": "Какой компонент служит для отображения изображения?",
                "options": ["Дисплей", "Матрица", "Клавиатура", "Сканер"],
                "answer": "Дисплей",
            },
            {
                "question": "Какое устройство преобразует ток из розетки в стабильное напряжение?",
                "options": ["Блок питания", "Адаптер", "Кабель питания", "Никакое, напряжение уже стабильное"],
                "answer": "Блок питания",
            },
            {
                "question": "Для чего нужна оперативная память (ОЗУ)?",
                "options": ["Для хранения личных данных", "Для временного хранения данных программ", "Для КЭШа операционной системы", "Для обработки графики"],
                "answer": "Для временного хранения данных программ",
            },
            {
                "question": "Название основного разъема подключения монитора к видеокарте?",
                "options": ["USB-C", "HDMI", "Ethernet", "VGA"],
                "answer": "HDMI",
            },
            {
                "question": "Что такое чипсет?",
                "options": ["Часть процессора, отвечающая за передачу температуры", "Микросхемы, связывающие компоненты платы", "Графический чип", "Часть оптического привода"],
                "answer": "Микросхемы, связывающие компоненты платы",
            },
            {
                "question": "В чем разница между архитектурами X86 и ARM?",
                "options": ["x86 - быстрый, но однопоточный, ARM - медленный, но многопотоковый", "x86 - для высокой производительности, ARM - для энергоэффективности", "x86 использует только Windows, ARM - только Linux", "Они отвечают за схожие задачи"],
                "answer": "x86 - для высокой производительности, ARM - для энергоэффективности",
            },
            {
                "question": "Что такое КЭШ-память процессора (L1, L2, L3)?",
                "options": ["Данные неиспользуемых программ для быстрого открытия", "Сверхбыстрая память для часто используемых данных", "Резервная копия оперативной памяти", "Память для хранения основных настроек BIOS"],
                "answer": "Сверхбыстрая память для часто используемых данных",
            },
            {
                "question": "Какие два основных производителя процессоров для ПК?",
                "options": ["NVIDIA и AMD", "Intel и AMD", "Samsung и Qualcomm", "Apple и Microsoft"],
                "answer": "Intel и AMD",
            },
            {
                "question": "Какие типы опертивной памяти являются современными стандартами?",
                "options": ["DDR2 и DDR3", "SD-RAM и RD-RAM", "DDR4 и DDR5", "SDRAM и VRAM"],
                "answer": "DDR4 и DDR5",
            },
            {
                "question": "Какое значение имеет аббревиатура RAID?",
                "options": ["Rapid Access Internet Device", "Redundant Array of Independent Disks", "Random Array of Integrated Devices", "Read And Insert Data"],
                "answer": "Redundant Array of Independent Disks",
            },
            {
                "question": "Что значит параметр TDP у процессора и видеокарты?",
                "options": ["Total Data Performance", "Thermal Design Power", "Turbo Drive Mode", "Typical Device Profile"],
                "answer": "Thermal Design Power",
            },
            {
                "question": "Что такое стандарт блока питания (Bronze, Gold, Platinum)?",
                "options": ["Показатель КПД", "Показатель максимальной выходной мощности", "Уровень создаваемого шума", "Показатель срока службы"],
                "answer": "Показатель КПД",
            },
            {
                "question": "Почему GDDR память используется в видеокартах?",
                "options": ["Потому что энергоэффективна", "Потому что нужна для работ с широкими шинами", "Потому что имеет минимальную задержку", "Потому что имеет низкую номинальную частоту "],
                "answer": "Потому что нужна для работ с широкими шинами",
            },
            {
                "question": "технология одновременной многопоточности (SMT), известная как Hyper-Threading у Intel, позволяет:",
                "options": ["Увеличить тактовую частоту ядра", "Ядру обрабатывать два потока", "Отключить неиспользуемые ядра", "динамически изменять КЭШ L3"],
                "answer": "Ядру обрабатывать два потока",
            },
            {
                "question": "По каким двум шинам могут быть подключены SSD к М2?",
                "options": ["SATA", "PCle", "SATA III или PCl Express (NVMe)", "USB 3.2 или Thunderbolt"],
                "answer": "SATA III или PCl Express (NVMe)",
            },
            {
                "question": "Ключевое различие между видеокартами для игр и для моделирования?",
                "options": ["Игровые карты имеют больше видеопамяти", "Профессиональные карты тактируются на более высоких частотах", "Профессиональные карты имеют поддержку ECC-памяти", "игровые карты основаны на более старшем техпроцессе"],
                "answer": "Профессиональные карты имеют поддержку ECC-памяти",
            },
            {
                "question": "Что означает тайминг оперативной памяти (например CL16-18-18-36)?",
                "options": ["Частоту памяти в различных режимах", "Задержку работы памяти", "Порядок инициализации модулей памяти","Уровень напряжения"],
                "answer": "Задержку работы памяти",
            },
            {
                "question": "В современных процессорах северный мост был интегрирован в кристалл CPU. Какие два контроллера теперь находятся непосредственно в процессоре?",
                "options": ["SATA и Ethernet", "Контроллер оперативной памяти и PCl Express", "Контроллер USB и питания", "Контроллер аудио и сети"],
                "answer": "Контроллер оперативной памяти и PCl Express",
            },
            {
                "question": "Что означает количество ядер в процессоре?",
                "options": ["Скорость выполнения одной задачи", "Максимальное количество одновременно выполняемых задач", "Размер встроенной памяти", "Количество программ для установки"],
                "answer": "Максимальное количество одновременно выполняемых задач",
            },
            {
                "question": "Что такое сокет (Socket)?",
                "options": ["Разъем для подключения монитора", "Разъем для установки процессора", "Порт для оперативной памяти", "Разъем для блока питания"],
                "answer": "Разъем для установки процессора",
            },
            {
                "question": "Для чего нужна термопаста при установке процессора?",
                "options": ["Для скрепления его с сокетом", "Для защиты от влаги", "Для улучшения передачи тепла", "Для электрической изоляции процессора"],
                "answer": "Для улучшения передачи тепла",
            },
            {
                "question": "При экстремальном охлаждение возникает проблема 'точки росы'. Чем она опасна для ПК?",
                "options": ["Теплоотводящее основание трескается от перепада температур", "Из-за низких температур и конденсата происходит короткое замыкание", "Термопаста теряет свои свойства", "Критически замедляется передача сигналов между компонентами"],
                "answer": "Из-за низких температур и конденсата происходит короткое замыкание",
            }
        ]

        # Основной контент в центре
        self.content_frame = tk.Frame(self, bg=self.original_bg)
        self.content_frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=10)

        # Используем grid для основного контента для лучшего контроля
        self.content_frame.grid_rowconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        self.lbl_question = tk.Label(self.content_frame, text="", font=("Arial", 12),
                                     wraplength=400, justify="center", bg=self.original_bg)
        self.lbl_question.grid(row=0, column=0, pady=20, sticky="ew")

        # Фрейм для вариантов ответов с выравниванием по левому краю
        self.options_frame = tk.Frame(self.content_frame, bg=self.original_bg)
        self.options_frame.grid(row=1, column=0, pady=10, sticky="w")

        self.var_answer = tk.StringVar()
        self.radio_buttons = []

        # Создаем радиокнопки с выравниванием по левому краю
        for i in range(4):
            rb = tk.Radiobutton(self.options_frame, text="", variable=self.var_answer,
                                value="", font=("Arial", 10), anchor="w", justify="left",
                                bg=self.original_bg)
            rb.pack(fill="x", pady=5, anchor="w")
            self.radio_buttons.append(rb)

        # Фрейм для кнопок управления викториной с центрированием
        self.control_frame = tk.Frame(self.content_frame, bg=self.original_bg)
        self.control_frame.grid(row=2, column=0, pady=15, sticky="")

        # Центрируем кнопки
        self.btn_submit = tk.Button(self.control_frame, text="Ответить",
                                    command=self.check_answer, width=15, font=("Arial", 12))
        self.btn_submit.pack(pady=5)

        self.btn_restart = tk.Button(self.control_frame, text="Начать заново",
                                     command=self.reset_quiz, width=15)
        self.btn_restart.pack(pady=5)

        self.lbl_result = tk.Label(self.content_frame, text="", font=("Arial", 12),
                                   justify="center", bg=self.original_bg)
        self.lbl_result.grid(row=3, column=0, pady=10, sticky="ew")

        self.lbl_score = tk.Label(self.content_frame, text="", font=("Arial", 12, "bold"),
                                  justify="center", bg=self.original_bg)
        self.lbl_score.grid(row=4, column=0, pady=5, sticky="ew")

        self.btn_back = tk.Button(self, text="Назад",
                                  command=lambda: controller.show_frame("SecondPage"),
                                  width=10)
        self.btn_back.grid(row=4, column=1, pady=10, sticky="s")

        # Инициализируем викторину
        self.reset_quiz()

    def shuffle_questions(self):
        """Перемешивает вопросы и варианты ответов"""
        # Выбираем случайные 10 вопросов из всех доступных
        selected_questions = random.sample(self.original_questions, min(15, len(self.original_questions)))

        # Перемешиваем порядок вопросов
        random.shuffle(selected_questions)

        # Перемешиваем варианты ответов для каждого вопроса
        for question in selected_questions:
            # Сохраняем правильный ответ
            correct_answer = question["answer"]

            # Перемешиваем варианты ответов
            options = question["options"][:]
            random.shuffle(options)

            # Обновляем вопрос с перемешанными вариантами
            question["options"] = options

            # Правильный ответ остается тем же (но его позиция изменилась)
            question["answer"] = correct_answer

        return selected_questions

    def reset_quiz(self):
        """Сбрасывает викторину к начальному состоянию"""
        # Генерируем новый набор перемешанных вопросов
        self.questions = self.shuffle_questions()

        self.current_question = 0
        self.score = 0
        self.answer_submitted = False  # Флаг, указывающий, был ли ответ на текущий вопрос

        # Восстанавливаем все элементы интерфейса
        self.lbl_question.config(font=("Arial", 12), bg=self.original_bg)
        self.lbl_result.config(text="", bg=self.original_bg)
        self.lbl_score.config(text="", bg=self.original_bg)

        # Сбрасываем цвет фона всей страницы к стандартному
        self.config(bg=self.original_bg)
        self.content_frame.config(bg=self.original_bg)
        self.options_frame.config(bg=self.original_bg)
        self.control_frame.config(bg=self.original_bg)

        # Сбрасываем цвет радиокнопок
        for rb in self.radio_buttons:
            rb.config(bg=self.original_bg)

        # Показываем варианты ответов
        self.options_frame.grid(row=1, column=0, pady=10, sticky="w")

        # Показываем кнопку "Ответить" и скрываем "Начать заново"
        self.btn_submit.pack(pady=5)
        self.btn_restart.pack_forget()

        # Загружаем первый вопрос
        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.lbl_question.config(text=f"Вопрос {self.current_question + 1}/{len(self.questions)}:\n{q['question']}")

            # Заполняем варианты ответов
            for i in range(4):
                self.radio_buttons[i].config(text=q["options"][i], value=q["options"][i])

            self.var_answer.set(None)
            self.lbl_result.config(text="")
            self.answer_submitted = False  # Сбрасываем флаг при загрузке нового вопроса

            # Включаем кнопку "Ответить"
            self.btn_submit.config(state="normal")
        else:
            self.show_final_results()

    def check_answer(self):
        # Проверяем, был ли уже ответ на этот вопрос
        if self.answer_submitted:
            return

        if not self.var_answer.get():
            messagebox.showwarning("Ошибка", "Выберите вариант ответа!")
            return

        # Устанавливаем флаг, что ответ был дан
        self.answer_submitted = True

        # Отключаем кнопку "Ответить" до загрузки следующего вопроса
        self.btn_submit.config(state="disabled")

        if self.var_answer.get() == self.questions[self.current_question]["answer"]:
            self.score += 1
            self.lbl_result.config(text="Правильно!", fg="green")
        else:
            correct_answer = self.questions[self.current_question]["answer"]
            self.lbl_result.config(text=f"Неправильно! Правильный ответ: {correct_answer}", fg="red")

        # Обновляем счет после каждого ответа
        self.lbl_score.config(text=f"Счет: {self.score}/15")

        self.current_question += 1
        self.after(1500, self.load_question)

    def show_final_results(self):
        result_text = f"Викторина завершена!\nПравильных ответов: {self.score}/{len(self.questions)}"
        percentage = (self.score / len(self.questions)) * 100

        if percentage >= 80:
            result_text += "\nОтличный результат!"
            bg_color = "#90EE90"  # Светло-зеленый
        elif percentage >= 60:
            result_text += "\nХороший результат!"
            bg_color = "#FFD700"  # Золотой (оранжевый)
        else:
            result_text += "\nПопробуйте еще раз!"
            bg_color = "#FFB6C1"  # Светло-красный

        self.lbl_question.config(text=result_text, font=("Arial", 14, "bold"), bg=bg_color)

        # Устанавливаем цвет фона для всей страницы
        self.config(bg=bg_color)
        self.content_frame.config(bg=bg_color)
        self.lbl_result.config(bg=bg_color)
        self.lbl_score.config(bg=bg_color)
        self.control_frame.config(bg=bg_color)

        # Устанавливаем цвет фона для радиокнопок (хотя они скрыты)
        for rb in self.radio_buttons:
            rb.config(bg=bg_color)

        # Скрываем варианты ответов
        self.options_frame.grid_remove()

        # Скрываем кнопку "Ответить" и показываем "Начать заново"
        self.btn_submit.pack_forget()
        self.btn_restart.pack(pady=5)

        self.lbl_result.config(text="Нажмите 'Начать заново', чтобы пройти викторину еще раз")


class TheoryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Настраиваем веса для растягивания
        self.grid_rowconfigure(1, weight=1)  # Текст занимает все пространство
        self.grid_columnconfigure(0, weight=1)

        label = tk.Label(self, text="Теоретический материал", font=("Arial", 16))
        label.grid(row=0, column=0, pady=20, sticky="n")

        # Фрейм для текста с прокруткой
        text_frame = tk.Frame(self)
        text_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        text_frame.grid_rowconfigure(0, weight=1)
        text_frame.grid_columnconfigure(0, weight=1)

        text_widget = tk.Text(text_frame, wrap="word", font=("Arial", 11),
                              padx=10, pady=10, spacing2=5)

        scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)

        text_widget.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        theory_text = """
                                                        Что такое компьютер?


Компьютер — это программируемое электронное устройство, предназначенное для обработки, хранения и передачи информации. Его работу обеспечивает набор взаимосвязанных компонентов, каждый из которых выполняет свою уникальную функцию.

                1. Центральный процессор (ЦП)

Основная функция:
 Выполнение инструкций программ. Он производит арифметические и логические операции, управляет потоками данных между компонентами.

Ключевые характеристики:

Тактовая частота: 
Измеряется в Гигагерцах (ГГц). Показывает, сколько операций процессор может выполнить за секунду. Чем выше, тем быстрее (в целом).

Количество ядер: 
Современные процессоры имеют несколько ядер (2, 4, 8, 16 и более). Каждое ядро может обрабатывать свой набор инструкций, что повышает общую производительность в многозадачных сценариях.

Кэш-память: 
Сверхбыстрая память внутри процессора для хранения часто используемых данных. Уменьшает время ожидания при обращении к оперативной памяти.
Имеет три уровня: 
L1, L2, L3 - Хранят данные, к которым процессор обращается наиболее часто. Являются буфером между процессором и RAM. Между уровнями разница в скорости доступа к ним процессором.

Встроенные контроллеры конвертируют сигналы в обрабатываемый другими компонентами формат.
Примеры контроллеров:

Контроллер оперативной памяти:
Встроен. Позволяет минимизировать задержку при обращении к RAM

Контроллер системы хранения данных:
Подключение накопителей через PCle-каналы (пример: NVMe и SATA)

Контроллер периферийных устройств:
Получают команды от процессора через шины (пример: PCl Express и DMI)
Периферийными контроллерами могут быть: USB-контроллеры, сетевые адаптеры, и т.д.

Контроллеры прерываний:
Обрабатывают запросы на прерывание процессов, маскирование запросов, приоритеты выполнения запросов

Основными производителями процессоров для ПК на 2025 год являются:
Intel и AMD
А также другие:
NVIDIA, Apple и т.д.


                2. Материнская плата

Основная функция: 
Соединяет все компоненты компьютера в единое целое. Обеспечивает их взаимодействие и питание.

Ключевые элементы на ней:
Сокет (Socket): Разъем для установки процессора.
Слоты оперативной памяти (DIMM): Для установки модулей ОЗУ.
Слоты расширения (PCIe): Для установки видеокарты, звуковой карты, сетевого адаптера.
Разъемы SATA и M.2: Для подключения накопителей (HDD, SSD).

Чипсет: 
"Контролер-распределитель", который управляет потоками данных между процессором и другими компонентами.

                3. Оперативная память (ОЗУ)

Основная функция: 
Временное хранение данных и инструкций, с которыми процессор работает в данный момент. Быстрая, но энергозависимая (стирается при выключении питания).

Ключевые характеристики:

Объем: 
Измеряется в Гигабайтах (ГБ). Чем больше объем, тем больше программ и данных можно загрузить для быстрой работы.

Частота: 
Скорость обмена данными с процессором.

Тип: 
DDR3, DDR4, DDR5. Каждое новое поколение быстрее и энергоэффективнее.

Латентность(тайминги):
Время, затрачиваемое для выполнения команды или сигнала. пример: CL18(18-22-22-42)

                4. Накопители данных (ПЗУ)
Основная функция: 
Постоянное хранение всех данных: операционной системы, программ, пользовательских файлов.

Основные типы:

HDD (Жесткий диск): 
Использует магнитные пластины и считывающие головки. Дешевый, большой объем, но медленный и чувствительный к вибрациям.

SSD (Твердотельный накопитель): 
Использует флеш-память (как в USB-флешках). Очень высокая скорость чтения/записи, бесшумный, устойчив к ударам. Дороже HDD.

NVMe SSD:
Подвид SSD, подключаемый через скоростной разъем M.2. Самый быстрый тип накопителей на потребительском рынке.

                5. Видеокарта (Графический процессор, GPU)
                
Основная функция:
Обработка и формирование графического изображения для вывода на монитор. Второй по важности процессор в компьютере.

Состоит из:

Графический процессор (GPU): 
Специализированный процессор, оптимизированный для сложных математических расчетов, необходимых для рендеринга 3D-графики.

Видеопамять (VRAM): 
Быстрая память для хранения текстур, кадров и других графических данных.

Также имеет:
TDP (Thermal Design power) - показатель энергопотребления видеокарты [Вт].
также TDP может обозначаться максимальное выделяемое тепло и напряженность работы чипа

Для чего критически важна: Игры, монтаж видео, 3D-моделирование, машинное обучение.

                6. Блок питания (БП)

Основная функция: 
Преобразует переменный ток из розетки (220В) в постоянный ток низкого напряжения (+12В, +5В, +3.3В), необходимый для работы компонентов компьютера.

Ключевая характеристика:

Мощность: 
Измеряется в Ваттах (Вт). Должна быть достаточной для питания всех компонентов, особенно процессора и видеокарты.

Важность: 
Качественный блок питания — залог стабильности и долговечности всего компьютера.

Имеет уровни сертификации в рамках международного стандарта 80 Plus. Они обозначают КПД устройства при различных нагрузках.
Примеры:

Bronze - КПД 82%
Silver - КПД 85%
Gold - КПД 87%
Platinum - КПД 89%
Titanium - КПД 90%

                7. Система охлаждения
                
Основная функция: 
Отвод тепла от нагревающихся компонентов (ЦП, ГП), предотвращая их перегрев и повреждение.

Типы:

Воздушное (кулеры): 
Радиатор + вентилятор. Самый распространенный тип.

Жидкое (СЖО): 
Более эффективная и тихая система, использующая жидкость и радиаторы для отвода тепла.

                8. Корпус
Основная функция: 
Физическое размещение и защита всех внутренних компонентов. Обеспечивает вентиляцию и эстетический вид.

Важные аспекты: 
Форм-фактор (должен соответствовать материнской плате), продуманность системы вентиляции, качество сборки.


                                        Как все работает вместе (простой пример):

Вы нажимаете кнопку мыши, чтобы открыть программу.

Сигнал от мыши поступает на материнскую плату.

Процессор, получив сигнал, обращается к оперативной памяти, чтобы найти, где на жестком диске хранится нужная программа.

Процессор отправляет команду жесткому диску скопировать данные программы в быструю оперативную память.

Процессор начинает выполнять код программы из оперативной памяти.

Если программа имеет графический интерфейс, процессор делегирует задачи по отрисовке изображения видеокарте.

Видеокарта формирует кадр и отправляет его на монитор.

Вы видите, как программа открылась.

                                                            Интересно:
                                
При резком перепаде температур устройство будет повреждено:

Экстремальное охлаждение вызывает проблему 'точки росы', при которой обильно образуется конденсат. Большое количество конденсата может вызвать короткое замыкание.

Экстремальный нагрев (до температур выше 100 градусов цельсия) Вызывает:
Ускорение износа или полный выход из строя отдельных компонентов ПК,
Снижение производительности,
Случайные зависания и прочую нестабильность.

Операционной системой по умолчанию на большинстве устройств является DOS - Disk Operating System.

RAID - Технология виртуализации данных, которая объединяет несколько физических дисковых устройств в логический модуль для повышения отказоустойчивости и (или) производительности.

Цвет разъема SSD показывает скорость передачи данных им, однако это не является сертифицированным подтверждением и варьируется от модели к модели.


"""

        text_widget.insert("1.0", theory_text)
        text_widget.config(state="disabled")

        btn_back = tk.Button(self, text="Назад",
                             command=lambda: controller.show_frame("SecondPage"),
                             width=10)
        btn_back.grid(row=2, column=0, pady=10, sticky="s")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()