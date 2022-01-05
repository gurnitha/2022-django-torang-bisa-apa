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


#### 10.2 Menggunakan logic rendering data ke templates

        Steps:

        1. Membuat variable pada projects_view
        2. Rendering data pada template
        3. Memerisa hasilnya

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/views.py
        modified:   templates/base.html


#### 10.3 Rendering data statik ke templates

        Steps:

        1. Membuat dami data
        2. Load data ke projects_view
        3. Rendering data pada template menggunakan for loop
        4. Periksa hasilnya

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/views.py



### 11. RENDERING DATA DINAMIS DARI DATABASE
--------------------------------------------

### 11.1 Menampilkan daftar proyeks

        Steps:

        1. Modifikasi project_view
        2. Rendering data
        3. Periksa hasilnya

        modified:   README.md
        modified:   projects/templates/projects/project_single.html
        modified:   projects/templates/projects/projects.html
        modified:   projects/urls.py
        modified:   projects/views.py
        modified:   templates/shared/navbar.html


### 11.2 Menampilkan proyek single

        Steps:

        1. Modifikasi project_single_view
        2. Modifikasi project_single template
        3. Periksa hasilnya


        modified:   README.md
        modified:   projects/templates/projects/project_single.html
        modified:   projects/views.py



### 12. OPERASI CRUD
--------------------


### 12.1 READ - Menampilkan dafter proyek dalam tabel

        Steps:

        1. Modifikasi projects.html
        2. Periksa hasilnya

        modified:   README.md
        modified:   projects/templates/projects/projects.html


### 12.2 CREATE (project_form) Part 1 - Membuat form Template, View, Urls

        Steps:

        1. Membuat file baru: templates/projects/project_form.html
        2. Membuat form templat
        3. Membuat method view
        4. Membuat path
        5. Membuat link
        6. Memeriksa hasilnya

        modified:   README.md
        new file:   projects/templates/projects/project_form.html
        modified:   projects/urls.py
        modified:   projects/views.py
        modified:   templates/shared/navbar.html


### 12.3 CREATE (project_form) Part 2 - Membuat Django Form

        Steps:

        1. Membuat file baru
        2. Mengimport django modules ModelForm
        3. Mengimport model Project
        4. Membuat class ProjectForm

        modified:   README.md
        new file:   projects/forms.py


### 12.4 CREATE (project_form) Part 3 - Rendering Django form pada project_form page

        Steps:

        1. Import ProjectForm
        2. Load ProjectForm 
        3. Render context form pada project_form template
        4. Memeriksa hasilnya

        modified:   README.md
        modified:   projects/templates/projects/project_form.html
        modified:   projects/views.py


### 12.5 CREATE (project_form) Part 4 - Rendering Django form with title, label etc

        Steps:

        1. Ubah project_form
        2. Memeriksa hasilnya

        modified:   README.md
        modified:   projects/templates/projects/project_form.html


### 12.6 CREATE (project_form) Part 5 - Looping Django form

        Steps:

        1. Loop form pada project_form
        2. Memeriksa hasilnya

        modified:   README.md
        modified:   projects/templates/projects/project_form.html


### 12.7 CREATE PROJECT Part 1 - Form testing

        Steps:

        1. Ubah project_form.html 
        2. Menentukan fields yang akan ditampilkan
        3. Load ProjectForm 
        4. Testing - isi dan submit form
        5. Periksa hasilnya pada terminal

        modified:   README.md
        modified:   projects/forms.py
        modified:   projects/templates/projects/project_form.html
        modified:   projects/views.py


### 12.8 CREATE PROJECT Part 2 - Create project

        Steps:

        1. Melengkapi logic pada method project_create_view
        2. Menguji form dengan mengisi form + submit
        3. Memeriksa hasilnya


        modified:   README.md
        modified:   projects/views.py


#### 12.9 House keeping - Modifikasi README.md file

        modified:   README.md


### 12.10 UPDATE PROJECT - Update proyek

        Steps:

        1. Membuat mothod project_update_view
        2. Membuat path
        3. Membuat link
        4. Menguji dengan meng-update proyek yg sudah ada
        5. Memeriksa hasilnya

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/urls.py
        modified:   projects/views.py


### 12.11 DELETE PROJECT - Menghapus proyek

        Steps:

        1. Membuat file templates/projects/project_delete.html 
        2. Membuat template project_delete.html
        3. Membuat method project_delete_view
        4. Membuat path
        5. Membuat link
        6. Menguji hasilnya

        new file:   projects/templates/projects/project_delete.html
        modified:   projects/templates/projects/projects.html
        modified:   projects/urls.py
        modified:   projects/views.py



### 13. STATIC DAN MEDIA FILES
------------------------------


#### 13.1 Setting up static dan media files pada settings.py dan urls.py

        Steps:

        1. Setup static dan media files
        2. Tambahkan path untuk static dan media files pada urls
        3. Jalankan server untuk menguji

        modified:   devsearch/settings.py
        modified:   devsearch/urls.py
        new file:   static/images/codesniper.png
        ...
        new file:   static/images/default.jpg
        new file:   static/images/django-react-course.jpg
        new file:   static/images/icon.svg



### 14. DEBUG, ALLOWED_HOSTS DAN WHITENOISE
### ---------------------------------------


#### 14.1 Setup DEBUG an ALLOWED_HOSTS

        modified:   README.md
        modified:   devsearch/settings.py


#### 14.2 Setup django whitenoice

        Steps:

        1. Install whitenoise
        2. Setup whitenoise in settings.py

        modified:   README.md
        modified:   devsearch/settings.py



### 15. TEMPLATE THEMES
### -------------------


#### 15.1 Testing loading static files

        Steps:

        1. Add logo
        2. Load static files
        3. Memeriksa hasilnya

        modified:   README.md
        modified:   templates/base.html


#### 15.2 Menambahkan template theme untuk projects page

        Steps:

        1. Modifikasi static assets 
        2. Mengisi template themes untuk projects.html
        3. Modifikasi projects_view
        4. Modifikasi base.html
        5. Refresh browser untuk melihat hasilnya

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/views.py
        modified:   templates/base.html
        ...
        new file:   static/images/DevSearch Projects.jpg
        new file:   static/images/Devsearch Home.jpg
        new file:   static/images/Devsearch Inbox.jpg
        new file:   static/images/Devsearch Profile.jpg
        new file:   static/images/favicon.ico
        modified:   static/images/logo.svg
        new file:   static/images/project-a.png
        new file:   static/images/project-b.png
        new file:   static/images/project-c.png
        modified:   static/uikit/app.js
        deleted:    static/uikit/index.html
        modified:   static/uikit/styles/modules/_form.css
        new file:   static/uikit/styles/modules/_formORI.css


#### 15.3 Mengisi template theme untuk project_single page

        Steps:

        1. Mengisi template themes untuk project_single.html
        2. Untuk memeriksa hasilnya: Klik salah satu proyek pada projects page

        modified:   projects/templates/projects/project_single.html


#### 15.4 PROJECT_FORM page Part 1: Mengisi basic template theme

        Steps:

        1. Mengisi template themes untuk project_form.html
        2. Untuk memeriksa hasilnya: Klik menu Add Project pada projects page

        modified:   README.md
        modified:   projects/templates/projects/project_form.html


        Note on Steps:

        1. Keep 1 form field and the submit button and remove the rest
        2. Use for loop to loop the ONE of the form field
        3. Display form label: {{field.label}} 
        4. Replace all line of the input tag with: {{field}} 
        5. Check the result


#### 15.5 PROJECT_FORM page Part 2: Ubah tags field dari multiselect menajadi radio button

        Steps:

        1. Buka projects/forms.py dan lakukan modifikasi
        2. Memeriksa hasilnya

        modified:   README.md
        modified:   projects/forms.py


#### 15.6 PROJECT_FORM page Part 3: Menambahkan class style pada input field


        Steps:

        1. Buka projects/forms.py dan lakukan modifikasi
        2. Periksa hasilnya

        modified:   README.md
        modified:   projects/forms.py


#### 15.7 PROJECT_FORM page Part 4: Menggunakan for loop menggantikan teknik pada poin 15.6

        Steps:

        1. Buka projects/forms.py dan lakukan modifikasi
        2. Periksa hasilnya

        modified:   README.md
        modified:   projects/forms.py



### 16. USERS APP
-----------------

#### 16.1 Membuat app baru dengan nama 'users'

        Steps:

        1. Membuat app 'users'
        2. Register users
        3. Jalankan server untuk menguji hasilnya

        modified:   README.md
        modified:   config/settings.py
        new file:   users/__init__.py
        new file:   users/admin.py
        new file:   users/apps.py
        new file:   users/migrations/__init__.py
        new file:   users/models.py
        new file:   users/tests.py
        new file:   users/views.py



### 17. STATIC USER PROFILE PAGE
--------------------------------

#### 17.1 Membuat profile page

        Steps:

        1. Membuat folder: users/templates
        2. Membuat sub folder    : users/templates/users
        3. Membuat profile page    : users/templates/users/profile.html

        modified:   README.md
        new file:   users/templates/users/profile.html        


#### 17.2 Membuat method profile_view dan urls

        Steps:

        1. Membuat method profile_view
        2. Membuat file: users/urls.py
        3. Membuat appname dan path untuk users
        4. Register users/urls.py pada config/urls.py
        5. Buka browser: http://127.0.0.1:8000/users/

        modified:   config/urls.py
        new file:   users/urls.py
        modified:   users/views.py


#### 17.3 Extending base layout pada profiles page

        1. Extends the base layout
        2. Gunakanan the block tags
        3. Test hasilnya
        
        modified:   README.md
        modified:   users/templates/users/profiles.html


#### 17.4 House keeping - Renaming git commits messages

        modified:   README.md




### 18. DINAMIS USER PROFILE PAGE
--------------------------------

#### 18.1 Membuat model Profile

        Steps:

        1. Import django module User
        2. Import django module uuid
        3. Buat model Profile

        modified:   README.md
        modified:   users/models.py


#### 18.2 Membuat tabel Profile pada database

        Steps:

        1. Membuat file migrasi
        2. Memeriksa hasil perintah migrasi
        3. Menjalankan file migrasi
        4. Memeriksa hasil perintah menjalankan migrasi
        5. Menjalankan perintah sqlmigrate
        6. Register model Profile pada admin.py
        7. Jalankan server
        8. Memeriksa hasilnya pada admin panel

        modified:   README.md
        modified:   users/admin.py
        new file:   users/migrations/0001_initial.py


#### 18.3 Membuat hubungan ManyToOne antar Project and Profile

        Steps:

        1. Mengimpor django module uuid
        2. Mengimpor model Profile
        3. Membuat hubungan ManyToOne antar Project dan Profile
        4. Menjalankan migrasi
        5. Memeriksa hasilnya pada admin panel

        modified:   README.md
        new file:   projects/migrations/0006_project_owner.py
        modified:   projects/models.py