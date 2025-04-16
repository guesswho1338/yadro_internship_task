# используем легковесный базовый образ специально под python, wget нам не нужен понадобится для работы, поэтому устанавливать пакеты не придется
FROM python:3.13.3-slim

# чтобы работал относительный путь в bash скрипте
WORKDIR /tmp

COPY search_path.sh /tmp/
COPY search_advanced.py /tmp/
COPY config.txt /tmp/

# объединяем команды, чтобы уменьшить количество слоев образа(то есть размера образа)
RUN chmod +x /tmp/search_path.sh /tmp/search_advanced.py

# в задании было написано, что это Dockerfile для запуска скриптов, поэтому для обычного запуска контейнера добавим для наглядности выполнение скриптов
CMD ["/bin/bash", "-c", "/tmp/search_path.sh && python3 /tmp/search_advanced.py /tmp/config.txt log"]


