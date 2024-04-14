# PoliTech
Сервис автоматизации процессов сбора и анализа информации о представленности в ассортименте и уровне цен на социально значимые товары в магазинах и торговых сетях

## Стек технологий
Backend:
* Python, FastAPI, PostgreSQL, Docker

Frontend:
* JS, HTML, CSS

## Установка и запуск
1. Убедитесь, что у вас установлен [Docker](https://www.docker.com/).
2. Склонируйте данный репозиторий
    ```shell
    git clone https://github.com/kurorodev/controlling_prices_together
    ```
3. Перейдите в директорию проекта и запустите Docker Compose:
    ```shell
    docker compose up --build -d
    ```
4. После успешного запуска сервис будет доступен локально по адресу http://localhost:8000/.  
5. Для остановки работы сервиса воспользуйтесь следующей командой:
    ```shell
    docker compose down
    ```
