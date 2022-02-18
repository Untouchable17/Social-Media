
### Небольшая социальная сеть на Django

#### Инструменты разработки

<ul>
    <li>Python</li>
    <li>Django</li>
    <li>DjangoRestFramework</li>
    <li>Docker</li>
    <li>NGINX + Gunicorn</li>
</ul>

#### Установка:

В файле .env заполните необходимые поля. Если вам нужно запустить сайт на продакшане, то в докер файле укажите пользователя в базе данных и соответствующий пароль

<ol>
    <li>Клонировать репозиторий<pre><code>git clone https://github.com/Untouchable17/Social-Media.git</code></pre><br></li>
    <li>Создайте виртуальное окружение и активируйте его<pre><code>python -m venv env</code></pre><br></li>
    <li>Установите все необходимые зависимости в проекте<pre><code>pip install -r requirements.txt</code></pre><br></li>
    <li>В файле .env заполните все необходимые поля<pre><code>.env</code></pre><br></li>
    <li>Подготовьте модели к миграции<pre><code>python manage.py makemigrations</code></pre><br>
    <li>Запустите миграции<pre><code>python manage.py migrate</code></pre><br>
    <li>Создайте суперпользователя<pre><code>python manage.py createsuperuser</code></pre><br>
</ol>

#### Запуск на локальном сервере

> Запустите сайт<pre><code>python manage.py runserver</code></pre><br></li>

#### Запуск на продакшане

> В докер файле заполните поля для пользователя в базе данных
> Запустите bash файл `entrypoint.sh`

