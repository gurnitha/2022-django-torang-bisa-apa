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


#### 05.4 Mensetup database pada settings.py

        Steps:

        1. Mensetup database kredensial
        2. Jalankan server untuk menguji hasilnya

        modified:   README.md
        modified:   config/settings.py



### 06. DJANGO ADMIN
--------------------

#### 06.1 Mengaktifkan Django Admin

        Steps:

        1. Membuat migrasi 
        2. Menjalankan migrasi
        3. Jalankan server
        4. Memeriksa hasilnya

        modified:   README.md


#### 06.2 Membuat superuser

        Steps:

        1. Membuat superuser 
        2. Jalankan server
        3. Login sebagai superuser
        4. Sekilas tampilan Admin Panel

        modified:   README.md
        modified:   config/settings.py



### 07. DJANGO MODEL
--------------------

#### 07.1 Membuat model dengan nama Project

        Steps:

        1. Buka file: projects/model.py dan buat model Project
        2. Membuat migrasi 
        3. Memeriksa hasil perintah migrasi
        4. Menjalankan migrasi
        5. Memeriksa hasil perintah migrasi
        
        BEGIN;
        --
        -- Create model Project
        --
        CREATE TABLE `projects_project` (
                `title` varchar(200) NOT NULL, 
                `description` longtext NULL, 
                `demo_link` varchar(2000) NULL, 
                `source_link` varchar(2000) NULL, 
                `created` datetime(6) NOT NULL, 
                `id` char(32) NOT NULL PRIMARY KEY
        );
        COMMIT; 

        modified:   README.md
        new file:   projects/migrations/0001_initial.py
        modified:   projects/models.py


#### 07.2 Meregistrasi model Project pada admin.py

        Steps:

        1. Buka file: projects/admin.py impor dan daftarkan model Project
        2. Jalankan server untuk memeriksa hasilnya
        3. Buka Admin Panel untuk memeriksa hasilnya

        modified:   README.md
        modified:   projects/admin.py  


#### 07.3 Menampilkan nama proyek pada Admin Panel

        Steps:

        1. Update model Project
        2. Refresh browser dan lihat hasilnya

        modified:   README.md
        modified:   projects/models.py  


#### 07.4 Membuat model dengan nama Review

        Steps:

        1. Buka file: projects/model.py dan buat model Review
        2. Membuat migrasi 
        3. Memeriksa hasil perintah migrasi
        4. Menjalankan migrasi
        5. Memeriksa hasil perintah migrasi pada database
        6. Memeriksa sqlmigrate
        7. Register model Review pada projects/admin.py
        8. Jalankan server
        9. Memeriksa hasilnya pada admin panel

        modified:   README.md
        modified:   projects/admin.py
        new file:   projects/migrations/0002_review.py
        modified:   projects/models.py


#### 07.4 Membuat model dengan nama Tag

        Steps:

        1. Buka file: projects/model.py dan buat model Tag
        2. Membuat migrasi 
        3. Menjalankan migrasi
        4. Menjalankan sqlmigrate
        5. Register model Tag pada projects/admin.py
        6. Jalankan server
        7. Memeriksa hasilnya pada admin panel

        modified:   README.md
        modified:   projects/admin.py
        new file:   projects/migrations/0003_tag.py
        modified:   projects/models.py


#### 07.5 Membuat hubungan OneToMany antara model Project and Review

        Steps:

        1. Menambahkan kolom project pada model Review
        2. Membuat migrasi
        3. Menambahkan 'id' project pada tabel Review
        4. Menjalankan migrasi
        5. Menjalankan sqlmigrate
        6. Jalankan server untuk menguji hasilnya
        7. Melihat tabel review pada admin panel 


        modified:   README.md
        new file:   projects/migrations/0004_review_project.py
        modified:   projects/models.py


#### 07.6 Membuat hubungan ManyToMany antara model Project and Tags

        Steps:

        1. Menambahkan beberapa kolom dan kolom tags pada model Project
        2. Membuat migrasi
        3. Menjalankan migrasi
        4. Menjalankan sqlmigrate
        5. Jalankan server untuk menguji hasilnya
        6. Melihat tabel review pada admin panel 


        modified:   README.md
        new file:   projects/migrations/0005_auto_20220103_1018.py
        modified:   projects/models.py



### 08. MEMBUAT STATIC PAGES
----------------------------

#### 08.1 Membuat halaman daftar proyek

        Steps:

        0. Mingimpor os 
        1. Mengaktifkan django templates
        2. Membuat folder: ./templates/projects
        3. Membuat file: projects/templates/projects/projects.html
        4. Menambahkan html template pada projects.html
        -----
        5. Membuat method projects_view
        -----
        6. Membuat urls: projects/urls.py
        7. Register rojects/urls.py pada config/urls.py
        -----
        8. Jalankan server
        9. Lihat hasilnya pada browser

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   projects/templates/projects/projects.html
        new file:   projects/urls.py
        modified:   projects/views.py


#### 08.2 Membuat halaman singel proyek

        Steps:

        1. Membuat file baru: projects/templates/projects/project_single.html
        2. Menambahkan html template pada project_single.html
        -----
        3. Membuat method project_single_view
        -----
        4. Membuat path untuk project_single
        -----
        5. Jalankan server
        6. Lihat hasilnya pada browser

        modified:   README.md
        new file:   projects/templates/projects/project_single.html
        modified:   projects/urls.py
        modified:   projects/views.py


#### 08.3 Membuat Navigasi

        Steps:

        1. Membuat navbar pada projects.html
        2. Membuat link pada projects.html
        3. Membuat navbar pada project_single.html
        4. Membuat link pada project_single.html
        5. Buka browser untuk melihat hasilnya

        modified:   README.md
        new file:   projects/templates/projects/project_single.html
        modified:   projects/templates/projects/projects.html



### 09. BASE TEMPLATE DAN TEMPLATE INHERITANCE
----------------------------------------------

#### 09.1 Membuat base template

        Steps:

        1. Membuat folder: ./templates
        2. Membuat file: ./templates/base.html
        3. Membuat base templae

        modified:   README.md
        new file:   templates/base.html


#### 09.2 Menggabungkan base template dengan projects dan project_single

        Steps:

        1. Modifikasi base.html 
        2. Extends base template pada projects page
        3. Modifikasi projects page
        ----
        4. Extends base template pada project_single page
        5. Modifikasi project_single page
        ----
        6. Buka browser untuk melihat hasilnya

        modified:   README.md
        modified:   config/settings.py
        modified:   projects/templates/projects/project_single.html
        modified:   projects/templates/projects/projects.html
        modified:   templates/base.html


#### 09.3 Menggunakan teknik template inheritance

        Steps:

        1. Membuat shared folder: templates/shared
        2. Membuat file: templates/shared/navbar.html
        3. Membuat file: templates/shared/footer.html
        4. Memindahkan navbar codes ke file shared/navbar.html
        5. Memindahkan footer codes ke file shared/footer.html
        6. Include shared/navbar.html pada base.html
        7. Include shared/footer.html pada base.html
        8. Buka browser untuk melihat hasilnya

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/shared/footer.html
        new file:   templates/shared/navbar.html



### 10. RENDERING DATA STATIC
-----------------------------

#### 10.1 Rendering message dari projects_view ke home page

        Steps:

        1. Membuat dami data
        2. Rendering dami data pada home page
        3. Memeriksa hasilnya

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/views.py