# ML model API example

Этот проект содержит пример модели машинного обучения - логистическая регрессия. Модель интегрирована в API, которое можно легко развернуть с помощью Docker.

## Структура репозитория

/model: Содержит скрипты для обучения модели и сохраненную модель.  
/app: Содержит Flask приложение для API и Dockerfile.  
/tests: Тесты для API.  
requirements.txt: Зависимости для проекта.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/your_username/repo-name.git
cd repo-name
```

2. Установите зависимости:

```bash
pip install -r requirements.txt

```

## Обучение модели

Перейдите в директорию model и запустите скрипт для обучения:

```bash
cd model
python train_model.py
```

После выполнения этого скрипта, модель будет сохранена как model.pkl.

## Запуск API

1. Соберите Docker-образ:

```bash
cd app
docker build -t prediction_api .
```

2. Запустите контейнер:

```bash
docker run -p 5000:5000 prediction_api
```

API теперь доступно на <http://localhost:5000>.  

## Тестирование

Перейдите в директорию tests и выполните тесты:

```bash
cd tests
python test_api.py
```

## Контрибьютинг

Если вы нашли ошибку или хотите предложить улучшение, пожалуйста, создайте issue или pull request. Вы также можете связаться со мной через мои социальные сети.
