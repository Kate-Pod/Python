# Исследование: Музыка больших городов
Яндекс.Музыка — это крупный продукт с огромным запасом данных для исследований. Команды таких сервисов для поддержания интереса к продукту и привлечения новых пользователей часто проводят исследования про пользователей. Чтобы удержать клиентов и привлечь новых, сделать бренд более узнаваемым, команда сервиса проводит исследования аудитории, и публикует интересные результаты. Например, интересно сравнить тексты, сочинённые нейросетью, с произведениями настоящих рэперов.
Есть исследование, которое напоминает наше: о музыкальных предпочтениях в разных городах России.
Итак, вопрос вам: как музыка, которая звучит по дороге на работу в понедельник утром, отличается от той, что играет в среду или в конце рабочей недели? Возьмите данные для Москвы и Петербурга. Сравните, что и в каком режиме слушают их жители.
План исследования
Получение данных. Прочитайте данные, ознакомьтесь с ними.
Предобработка данных. Избавьтесь от дубликатов, проблем с названиями столбцов и пропусками.
Анализ данных. Ответьте на основные вопросы исследования, подготовьте отчётную таблицу или опишите полученный результат.
Подведение итогов. Просмотрите выполненную работу и сформулируйте выводы.

## Этап 1. Получение данных
Изучите данные, предоставленные сервисом для проекта.
Импортируйте библиотеку pandas и прочитайте данные из файла music_project.csv.
Путь к файлу: /datasets/music_project.csv
  
import pandas as pd
df = pd.read_csv('/datasets/music_project.csv')
df.head(10) # <получение общей информации о данных в таблице df>
df.info()# <получение общей информации о данных в таблице df>

##Этап 2. Предобработка данных
