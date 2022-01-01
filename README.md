### MEMBANGUNG SEBUAH APLIKASI 'TORANG-BISA-APA' MENGGUNAKAN DJANGO V3.2.7
Aplikasi ini adalah proyek pribadi untuk memulai sesuatu pada 2022. Aplikasi
ini diharapkan akan dapat memfasilitasi para developers, creators dan creative
Indonesia untuk memamerkan hasil karya mereka.

Mulai dibangun pada: 01/01/2022 pukul 17:00:00 wib.
Oleh: I Nyoman Gurnitha


### 01. INISIAL SETUP
----------------------

        Steps:

        1. Gambar 01/01
           - Menginstal Sublime Text Editor
           - Membuat workspace django-2022
           - Menginstal Cmder Terminal
        2. Gambar 01/02
           - Membuat root folder
           - Memeriksa hasil
           - Masuk ke root folder
           - Membuat file: .gitignore
           - Membuat file: README.md  
        3. Gambar 01/03
           - Memastikan python sudah terinstal pada PC
           - Memastikan pip sudah terinstal pada PC
           - Memastikan mysql database sudah terinstal pada PC
           - Memastikan postgres database sudah terinstal pada PC 
        4. Gambar 01/04 dan 01/05
           - Membuat remote repositori pada Github
        5. Gambar 01/06
           - Mengisi daftar file yang akan diignore oleh Git
        6. Gambar 01/07
           - Membuat catatan pada README.file
        7. Gambar 01/08
           - Membuat lokal repositori

        new file:   .gitignore
        new file:   README.md



### 02. MENGINSTAL DJANGO
-------------------------

#### 02.1 Menginstal Django Framework

        Steps:

        1. Lihat gambar 02/01

        modified:   README.md



### 03. MEMBUAT DJANGO PROYEK
-----------------------------

#### 03.1 Membuat django proyek 'config'

        Steps:

        1. Memastikan venv39327 dalam keadaan aktif
        2. Membuat djangp proyek
        3. Memerikas hasilnya
        4. Jalankan server 
        5. Buka browser untuk melihat hasilnya

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py



### 04. MEMBUAT DJANGO APP
--------------------------

#### 04.1 Membuat django app dengan nama 'projects'

        Steps:

        1. Membuat django app 'projecs'
        2. Memeriksa hasilnya
        3. Meregistrasi projects pada config/settings.py
        4. Jalankan server untuk menguji hasilnya

        modified:   README.md
        modified:   config/settings.py
        new file:   projects/__init__.py
        new file:   projects/admin.py
        new file:   projects/apps.py
        new file:   projects/migrations/__init__.py
        new file:   projects/models.py
        new file:   projects/tests.py
        new file:   projects/views.py



### 05. SETTING UP DATABASE
---------------------------

#### 05.1 Membuat postgresql database

        Steps:

        1. Login ke postgres server
        2. Membuat database
        3. Memeriksa hasilnya
        4. Menginstal postgres driver psycopg2-binary==2.8.6

        modified:   README.md


#### 05.2 Mensetup django-environ

        Steps:

        1. Menginstal django-environ
        2. Membuat .env file
        3. Mensetup variabel pada .env file

        modified:   README.md


#### 05.3 Mensetup environment pada settings.py file

        Steps:

        1. Menginisiasi environment pada settings.py
        2. Memodifikasi SECRET_KEY

        modified:   README.md
        modified:   config/settings.py
