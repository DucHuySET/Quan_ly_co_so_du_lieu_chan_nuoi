# Bài tập lớn môn học: Kỹ thuật phần mềm ứng dụng. 
Đề tài: xây dựng cơ sở dữ liệu quản lý chăn nuôi

Giảng viên hướng dẫn: ThS. VŨ SONG TÙNG

Nhóm thực hiện:  
TRẦN BÁCH CHIẾN - 20203335 <br />
ĐỖ NGỌC HIẾU - 20203418 <br />
NGUYỄN ĐỨC HUY - 20203450 <br />
LÊ ĐÌNH THỰC - 20203599 <br />
NGUYỄN VĂN TRÀ - 20203773

# Hướng dẫn làm việc với project
1. Instalation :
- Clone this repository, you should use a virtual environment to store your Django project’s
```shell
$ git clone https://github.com/DucHuySET/Quan_ly_co_so_du_lieu_chan_nuoi.git
$ cd <folder>
```
- Install the Django code with Pip:
```shell
$ python -m pip install Django
```
- Database: PostGresQL and change information about DATABASE in setting.py. You can use SQLite or other Database. Read docs: https://docs.djangoproject.com/en/4.1/ref/databases/ to get more informations.
```python

Using database with sqlite3 for python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

- Install other dependencies:
```shell
$ pip install db-sqlite3
```
2. Run Project:
- Make migrations:
```shell
$ python manage.py makemigrations <app_name> 
Can try: app_name = App
```
- Migrate:
```shell
$ python manage.py migrate
```
- Create a superuser (Admin account, User account can be create by Admin Account in web): 
```shell
$ python manage.py createsuperuser
```
- Run Server (Deploy):
```shell
$ python manage.py runserver
```
- Then copy url to browser, example: http://127.0.0.1:8000/
