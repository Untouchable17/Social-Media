
### Небольшая социальная сеть на Django

#### Инструменты разработки

<ul>
    <li>Python >= 3.7</li>
    <li>Django >= 1.1.2 </li>
    <li>PostGreSQL</li>
    <li>NGINX + Gunicorn</li>
</ul>

#### Установка:

<ol>
    <li>Клонировать репозиторий<pre><code>git clone [ссылка]</code></pre><br></li>
    <li>Создать виртуальное окружение и активируйте его<pre><code>python -m venv env</code></pre><br></li>
    <li>Установите все зависимости<pre><code>pip install -r requirements.txt</code></pre><br></li>
    <li>Подготовьте модели<pre><code>python manage.py makemigrations</code></pre><br>
    <li>Запустите миграции<pre><code>python manage.py migrate</code></pre><br>
    <li>Создайте суперпользователя<pre><code>python manage.py createsuperuser</code></pre><br>
    <li>Запустите сайт<pre><code>python manage.py runserver</code></pre><br></li>
</ol>
