
####Активация виртуального окружения
```
source ~/tensor/venv_tensor/bin/activate
```
####Запуск всех тестов:
```
PYTHONPATH=. python -m unittest TestPages.TestPages
```
####Запуск теста 'Поиск Яндекс':
```
PYTHONPATH=. python -m unittest TestPages.TestPages.test_search_site_tensor
```
####Запуск теста 'Картинки на яндексе':
```
PYTHONPATH=. python -m unittest TestPages.TestPages.test_image
```

