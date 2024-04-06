# Картинки NASA и Space X

Скрипт для скачивания разиличный картинкой из сайта [NASA](api.nasa.gov)

---

##   Установка виртуального окружения

Виртуальное окружение устанавливается для каждого проекта. Оно позволяет использовать определенные версии библиотек. Для того чтобы создать виртуальное окружение необходимо в терминале прописать код

```
python -m venv venv
```
После чего создасться папка venv, в которую можно будет устанавливать необходимые для проекта библиотеки

---

##  Требования

Требуется Python 3.0+, среда разработки, например Pycharm, а также ключ для запросов на сайт.


Для того чтобы получить ключ, необходимо пройти по ссылке [NASA](https://api.nasa.gov/), в котором пользователю нужно заполнить информацию о себе и предоставить почту, в которую ключ будет отправлен


__Переменные окружения__

Так как токен является одной из чувтствительных информаций, необходимо спрятать ее от публично доступной системы. Для решения этой задачи нужно создать файл .env, после чего в нем прописать все чувствительные данные, а сам файл доавить в другой файл .gitignore

* API_KEY


---

##  Запуск программы

Для запуска прогламмы необходимо в GitHub CODE скопировать [ссылку]() по HTTPS и в терминале среды разработки прописать код:

```
git clone dsfsdfsdfdsf.git
```
После чего установить все необходимые библиотеки также прописав код в терминале

```
python sldkflksd
```

Также необходимо прописать в .env файле ключ, который был послан на почту пользователя

---

##  Примечания

В скрипте даны 3 разные ссылки на которые отправляется запрос для получения различных видов картин: spacex_url, nasa_url, epic_info_url. 
На каждую из этих ссылок идет запрос внутри функций соответсвенно: 
* fetch_spacex_last_launch(spacex_url, demo_key),
* fetch_epic_lunch(epic_info_url, demo_key),
* fetch_nasa_last_lunch(nasa_url, demo_key)
Сохранения картинок в образующиеся папки с одноименнными названиями также происходят внутри каждой функций.

