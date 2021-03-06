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


#### 18.4 Membuat beberapa user baru pada admin panel

        Steps:

        1. Pada admin panel, klik tanda +Add pada users
        2. Isi form Add User
        3. Klik Save
        4. Change User dan save
        5. Periksa hasilnya

        modified:   README.md


#### 18.5 Menambahkan kolom username pada model Profile

        Steps:

        1. Menambahkan kolom username
        2. Jalankan migrasi
        3. Jalan server
        4. Periksa hasilnya pada admin panel

        modified:   README.md
        new file:   static/images/profiles/bisma.PNG
        new file:   users/migrations/0002_profile_username.py
        modified:   users/models.py      


#### 18.6 Membuat sebuah proyek dari admi panel

        Steps:

        1. Membuat user
        2. Membuat profile
        3. Membuat proyek
        4. Memeriksa hasilnya

        new file:   static/images/baratayuda.jpg
        new file:   static/images/profiles/bisma_RfGIQGb.PNG


#### 18.7 Asain proyek ke masing-masing nama pengguna

        Steps:

        1. Buka proyek pada admin panel dan asain masing
           - proyek pada username

        modified:   README.md
        new file:   static/images/baratayudha.PNG
        new file:   static/images/django3.jpeg
        new file:   static/images/mongodb.jpg
        new file:   static/images/profiles/arjuna.JPG
        new file:   static/images/profiles/ing.PNG
        new file:   static/images/profiles/kurukshetra_War.jpg


#### 18.8 Display username pada projects page

        Steps:

        1. Display proyek owner
        2. Periksa hasilnya

        modified:   README.md
        modified:   projects/templates/projects/projects.html



### 19. THEMING USERS PROFILES PAGE
-----------------------------------

#### 19.1 Menambahkan template theme pada user profiles page

        Steps:

        1. Buka dan tambahkan template theme pada user profiles page
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/profile.html


#### 19.2 Modifikasi users, profiles, projects

        Steps:

        1. Pad admin panel, lakukan modifikasi users
        2. Hasil modifikasi users
        3. Pada admin panel, lakukan modifikasi profile
        4. Pada admin panel, lakukan modifikasi proyek
        5. Hasil modifikasi proyek


        modified:   README.md
        modified:   projects/templates/projects/projects.html
        new file:   static/images/desainlokal.JPG
        new file:   static/images/desainlokal_2clmuVo.jpg
        new file:   static/images/desainlokal_PC8fub5.JPG
        new file:   static/images/profiles/gurunmeao.JPG
        new file:   static/images/profiles/saiber.w.JPG
        new file:   static/images/profiles/tahbahken.JPG
        new file:   static/images/tba.jpg


#### 19.3 Membuat model Skill

        Steps:

        1. Buka users/models.py dan buat model Skill
        2. Jalankan migrasi
        3. Register model Skill pada users/admin.py
        4. Jalankan server dan periksa hasilnya pada admin panel

        modified:   README.md
        modified:   users/admin.py
        new file:   users/migrations/0003_skill.py
        modified:   users/models.py


#### 19.4 Menambahkan kolom location pada model Profile

        Steps:

        1. Buka users/models.py dan tambahkan kolom location
        2. Jalankan migrasi, server dan periksa hasilnya

        modified:   README.md
        new file:   users/migrations/0004_profile_location.py
        modified:   users/models.py


#### 19.5 Menginput skill dan location melalui admin panel

        Steps:

        1. Buka admin panel dan input skill
        2. Buka admin panel dan input location

        modified:   README.md


#### 19.6 Menampilkan data profile dari db pada profile page

        Steps:

        1. Import dan load model Profile
        2. Loop data profiles pada profile page
        3. Periksa hasilnya

        modified:   README.md
        new file:   static/images/profiles/endiardkk.JPG
        modified:   users/templates/users/profile.html
        modified:   users/views.py


#### 19.7 Menampilkan data skill dari db pada profile page

        Steps:

        1. Re-input skill
        2. Import dan load model Profile
        3. Loop data profiles pada profile page
        4. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/profile.html
        modified:   users/views.py



### 20. HALAMAN PROFIL USER
---------------------------


#### 20.1 Membuat halaman statis profil user - Template, View dan Urls

        Steps:

        1. Modifikasi projects/urls.py
        2. Membuat file templates/users/profile_user.html
        3. Mengisi template theme untuk profile_user
        4. Membuat method profile_user_view
        5. Membuat path profile_user
        6. Membuat link untuk profile_user
        7. Memeriksa hasilnya


        modified:   README.md
        modified:   projects/urls.py
        modified:   users/templates/users/profile.html
        new file:   users/templates/users/profile_user.html
        modified:   users/urls.py
        modified:   users/views.py


#### 20.2 Mengganti logo

        Steps:

        1. Ganti logo
        2. Periksa hasilnya

        modified:   README.md
        new file:   static/images/tba-logo.JPG
        modified:   templates/base.html


#### 20.3 Mengubah nama file

        Steps:

        1. Ubah nama file dari users/profile.html menjadi users/profiles.html
        2. Ubah juga nama file pada profile_view

        modified:   README.md
        renamed:    users/templates/users/profile.html -> users/templates/users/profiles.html
        modified:   users/views.py


#### 20.4 Membuat user profile page dinamis Part 1 - Aside (nama dan lokasi)

        Steps:

        1. Load data Profile dari db
        2. Display data pada user profile page
        3. Perikasa hasilnya

        modified:   README.md
        modified:   users/templates/users/profile_user.html
        modified:   users/views.py


#### 20.5 Membuat user profile page dinamis Part 2 - Aside (sosial media)

        Steps:

        1. Display data sosmed menggunakan kondisional
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/profile_user.html


#### 20.6 Membuat user profile page dinamis Part 3 - About

        Steps:

        1. Display data bio
        2. Periksa hasilnya


#### 20.7 Membuat user profile page dinamis Part 4 - About dan Skill dengan deskripsi
        
        Steps:

        1. Display data bio
        2. Periksa hasilnya
        ------

        Steps:

        1. Display data skill dengan deskripsi
        2. Periksa hasilnya

        modified:   users/templates/users/profile_user.html
        modified:   users/views.py


#### 20.8 Membuat user profile page dinamis Part 5 - Skill tanpa deskripsi

        Steps:

        1. Display data skill tanpa deskripsi
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/profile_user.html
        modified:   users/views.py


#### 20.9 Membuat user profile page dinamis Part 6 - Showing all projects AS CHILD of profile

        Steps:

        1. Display data skill tanpa deskripsi
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/user-profile.html


#### 20.10 Membuat user profile page dinamis Part 7 - Display tags yg berkaitan dgn proyek yg dimiliki oleh user

        Steps:

        1. Load data tags pada method profile_user_view
        2. Display tags pada profile_user page
        3. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/user-profile.html
        modified:   users/views.py


#### 20.11 Membuat user profile page dinamis Part 8 - linking nama owner dengan user_profile page

        Steps:

        1. Buat link
        2. Buat link
        3. Periksa hasilnya

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   templates/base.html


#### 20.12 Membuat user profile page dinamis Part 9 - linking nama owner dengan profile_user page untuk re-load the page

        Steps:

        1. Buat link
        2. Periksa hasilnya
        modified:   README.md
        modified:   users/templates/users/profile_user.html


#### 20.13 Membuat user profile page dinamis Part 10 - Membatasi jumlah skill yg didisplay pada profiles page

        Steps:

        1. Batasi jumlah skill
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/profiles.html


#### 20.14 Membuat user profile page dinamis Part 11 - Buat link ke project_single

        Steps:

        1. Buat link
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/profile_user.html


#### 20.15 House keeping: Modifikasi messages poin 20.24 s.d 20.14 

        modified:   README.md



### 21. FIXING PROJECTS FILE
----------------------------


#### 21.1 Memperbaiki tampilan projects dengan membetulkan letak codes

        Steps:

        1. Betulkan file
        2. Lihat hasilnya



### 22. DJANGO SIGNALS
----------------------


#### 22.1  Create and delete a new profile and print out the signals reaction

        Steps:

        1. Import post_save and post_delete dari signals
        2. Buat method
        3. Test dan lihat hasilnya

        modified:   README.md
        modified:   users/models.py


#### 22.2  Using receiver to create and delete a new profile and print out the signals reaction

        Steps:

        1. Import receiver, post_save and post_delete dari signals
        2. Buat method
        3. Test dan lihat hasilnya

        modified:   README.md
        modified:   users/models.py


#### 22.3  Django signals - User profile akan terbuat secara otomatis bila user baru dibuat

        Steps:

        1. Import receiver, post_save and post_delete dari signals
        2. Buat method
        3. Test dan lihat hasilnya

        modified:   README.md
        modified:   users/models.py

        NOTE:
        1. User dibuat, profile terbuat
        2. User dihapus, profile terhapus
        3. Profile dihapus, user tidak terhapus


#### 22.4  Django signals - Bila profile dihapus, user juga akan terhapus secara otomatis

        Steps:

        1. Import receiver, post_save and post_delete dari signals
        2. Buat method
        3. Test dan lihat hasilnya

        modified:   README.md
        modified:   users/models.py


        NOTE:
        1. User dibuat, profile terbuat
        2. User dihapus, profile terhapus
        3. Profile dihapus, user juga terhapus


#### 22.5  Django signals - Menempatkan signals pada file tersendiri

        Steps:

        1. Buat file signals: users/signals.py
        2. Pindahkan signals dari users/models.py
        3. Testing

        NOTE:
        -----
        1. User berhasil dibuat
        2. Profile TIDAK berhasil

        modified:   README.md
        modified:   users/models.py
        new file:   users/signals.py


#### 22.6  Django signals - Menggunakan method ready() untuk mentriger signals

        Steps:

        1. Buka users/apps.py
        2. Tambahkan method ready()
        3. import signals dari users
        4. Add Print  ...
        5. Testing:
           - open a user
           - update it and save it
           - see the result in the terminal

        modified:   README.md
        modified:   users/apps.py
        modified:   users/signals.py



### 23. AUTHENTICATION: REGISTER, LOGIN DAN LOGOUT
--------------------------------------------------

#### 23.1 Login Part 1 - template, view dan urls

        Steps:

        1. Buat folder dan file baru: auth/register_login.html file
        2. Buat template
        3. Buat login view
        4. Buat path
        5. Buat link pada menu
        
        modified:   README.md
        modified:   templates/base.html
        new file:   users/templates/users/auth/register_login.html
        modified:   users/urls.py
        modified:   users/views.py


#### 23.2 Login Part 2 - Membuat basic form

        Steps:

        1. Add basic html form pada register_login
        2. Periksa hasilnya
        
        modified:   README.md
        modified:   users/templates/users/register_login.html


#### 23.3 Login Part 3 - Membuat basic logic page userLogin view

        Steps:

        1. Buat logic nya
        2. Test it out 
        3. Periksa hasilnya

        modified:   README.md
        modified:   users/views.py


#### 23.4 Login Part 4 - Membuat authentication logic

        Steps:

        1. Add inline style pada form dan periksa hasilnya
        2. Membuat authentication logic pada userLogin
        3. Test dengan user yg tdk ada di dalam db
        4. Periksa hasilnya
        5. Test dengan user yg ADA di dalam db
        6. Periksa hasilnya
        
        modified:   README.md
        modified:   users/templates/users/auth/register_login.html
        modified:   users/views.py


#### 23.5 Login Part 5 - Menampilkan menu logout bagi user yg telah log in

        Steps:

        1. Membuat kondisional
        2. Test dan lihat hasilnya

        modified:   README.md
        modified:   templates/base.html

        NOTE:

        1. Menampilkan menu logout berhasil
        2. User belum bisa log out
        3. NEXT> Membuat user bisa logout 


#### 23.6 Logout - Membuat logout functionality

        Steps:

        1. Import logout method
        2. Buat logoutUser view method
        3. Buath path untuk logout
        4. Tambahkan link logout pada menu
        5. Coba dan periksa hasilnya

        modified:   templates/base.html
        modified:   users/urls.py
        modified:   users/views.py


#### 23.7 Restriction Part 1 - Sembunyikan laman login bagi user yg tlh login

        Steps:

        1. Gunakan is_authenticated method
        2. Test it out to see the result

        NOTE:

        1. User yg telah login tidak bisa mengakses lagi laman login.
        2. Bila mencoba mengaksesnya, user akan di-redirect ke laman user

        DONE:)

        modified:   README.md
        modified:   projects/views.py
        modified:   users/views.py


#### 23.8 Restriction Part 2 - Blocking user unt meng-akses laman project_create, project_update dan project_delete 

        Steps:

        1. Import login_required method
        2. Add login_required pada project_create_view
        3. Add login_required pada project_update_view
        4. Add login_required pada project_delete_view
        5. Test it out to see the result

        NOTE:

        1. User yg tdk login tidak bisa mengakses laman project_create
        2. Bila user yg tdk login mencoba mengakses laman itu, maka
           user akan diarahkan ke laman login.

        NEXT > Menyembunyikan menu Add Project

        modified:   README.md
        modified:   projects/views.py


#### 23.9 Restriction Part 3 - Menyembunyikan menu Add Project dari un-logged in user

        Steps:

        1. Pindahkan Add Project menu ke bagian kondisional
        2. Periksa hasilnya

        NOTE
        1. Menu Add Project berhasil disembunyikan
           saat user melakukan logout

        NEXT> Flash messages

        modified:   README.md
        modified:   templates/base.html


#### 23.10 MESSAGES - Adding flash error message to login dan logout

        Steps:

        1. Import messages modules
        2. Gunakan messages module with error method
        3. Add message tags pada base page
        4. Coba dan lihat hasilnya

        NOTE:
        1. Flash messages berhasil

        NEXT> Registrasi

        modified:   README.md
        modified:   templates/base.html
        modified:   users/views.py


#### 23.11 REGISTER Part 1 - Create View dan Urls

        Steps:

        1. Buat method registerUser dan gunakan template register_login.html
        2. Buat path untuk register
        3. Tes hasilnya

        modified:   README.md
        modified:   users/urls.py
        modified:   users/views.py


#### 23.12 REGISTER Part 2 - Adding conditional pada register_login form

        Steps:

        1. Buka template register_login.html dan add kondisional
        2. Tes hasilnya

        modified:   README.md
        modified:   users/templates/users/auth/register_login.html


#### 23.13 REGISTER Part 3 - Menggunakan UserCreationForm

        Steps:

        1. Import UserCreationForm module
        2. Gunakan UserCreationForm pada registerUser view
        3. Gunakan instance dari UserCreationForm pada register form
        4. Buka browser dan lihat hasilnya
        
        modified:   README.md
        modified:   users/templates/users/auth/register_login.html
        modified:   users/views.py


#### 23.14 REGISTER Part 4 - Add logic to register a user

        Steps:

        1. Buat register logic pada method registerUser
        2. Register user baru untuk menguji

        NOTE:
        1. A new was user successfully created.

        modified:   users/views.py


#### 23.15 REGISTER Part 5 - Authomatically login user after Signing up

        Steps:

        1. Pada registerUser tambahkan lagi logic agar
           user yang berhasil melakukan register di
           redirect ke laman profile
        2. Tunjukkan failed message jika registration failed  
        3. Test it out

        NOTE:

        Kita memanfaatkan login session untuk me-login
        user baru

        modified:   users/views.py


#### 23.16 REGISTER Part 6 - Membuat CustomUserCreationForm

        Steps:

        -- forms.py
        1. Buat file baru: users/forms.py
        2. Import modules 
        3. Buat class CustomUserCreationForm
        4. Tentukan form fields
        
        -- views
        5. Remove UserCreationForm
        6. Modifikasi registerUser view method
        7. Test it out and see the result

        modified:   README.md
        new file:   users/forms.py
        modified:   users/views.py


#### 23.17 REGISTER Part 7 - Change reg form field from 'First name' to 'Name'

        Steps:

        1. Add labels pada forms.py
        2. Periksa hasilnya
        3. Test it out

        modified:   README.md
        modified:   users/forms.py


#### 23.18 REGISTER - LOGIN Part 1 - Add template theme

        Steps:

        1. Buka register_login page dan add template theme
        2. Buka browser, periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/register_login.html


#### 23.19 REGISTER - LOGIN Part 2 - Add kondisional memerlihatkan login atau register form

        Steps:

        1. Buka register_login page dan add kondisional
        2. Buka browser, periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/register_login.html


#### 23.20 REGISTER - LOGIN Part 3 - Add links pada login and register

        Steps:

        1. Buka register_login page dan add link
        2. Buka browser, periksa hasilnya

        NOTE: Links berfungsi

        modified:   README.md
        modified:   users/templates/users/auth/register_login.html


#### 23.21 REGISTER - LOGIN Part 4 - Include header dan modifikasi home url

        Steps:

        1. Buat file baru: templates/shared/header.html
        2. Pindahkan header dari base.html ke header.html
        3. Include header pada base.html
        4. Buka users/urls.py lakukan modifikasi home url dan profile url:
           -- home url
           dari   : http://127.0.0.1:8000/users/
           menjadi: http://127.0.0.1:8000
           -- profile url
           dari   : http://127.0.0.1:8000/user/profile/e8146636-b6ae-451e-bc46-4b9b51adfffe/
           menjadi: http://127.0.0.1:8000/profile/e8146636-b6ae-451e-bc46-4b9b51adfffe/
        5. Periksa hasilnya

        NOTE: 

        1. Include working
        2. Modifikasi working

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/shared/header.html
        deleted:    templates/shared/navbar.html
        modified:   users/urls.py


#### 23.22 REGISTER - LOGIN Part 5 - Add functionality pada login form

        Steps:

        1. Buka file auth/register_login.html dan modifikasi codes
        5. Periksa hasilnya

        NOTE: 

        1. Login working

        modified:   README.md
        modified:   users/templates/users/auth/register_login.html


#### 23.23 REGISTER - LOGIN Part 6 - Modifikasi register_login.html

        Steps:

        1. Buka dan modifikasi register_login.html
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/auth/register_login.html


#### 23.24 REGISTER - LOGIN Part 7 - Looping the form field Part 1

        Steps:

        1. Buka dan modifikasi register_login.html
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/register_login.html


#### 23.25 REGISTER - LOGIN Part 8 - Looping the form field Part 2 (rendering label dan input field)

        Steps:

        1. Buka dan modifikasi register_login.html
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/register_login.html


#### 23.26 REGISTER - LOGIN Part 9 - Styling forms.py

        Steps:

        1. Buka dan modifikasi users/forms/py
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/forms.py


#### 23.27 REGISTER - LOGIN Part 10 - Memperlihatkan pesan/alert error pada register_login.html

        Steps:

        1. Buka dan modifikasi register_login.html
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/auth/register_login.html


#### 23.28 REGISTER - LOGIN Part 11 - Add style pada flash messages

        Steps:

        1. Buka dan modifikasi base.html
        2. Buka dan modifikasi logoutUser view
        3. Periksa hasilnya

        NOTE:

        Style alert berhasil, tapi tidak bisa dihilangkan

        NEXT> Menghilangkan alert

        modified:   README.md
        modified:   templates/base.html
        modified:   users/views.py


#### 23.29 REGISTER - LOGIN Part 12 - Removing the flash message

        Steps:

        1. Buka dan modifikasi base.html
        2. Buka dan modifikasi static/uikit/app.js
        3. Periksa hasilnya

        NOTE:

        Alert berhasil dihilangkan :)

        modified:   static/uikit/app.js
        modified:   templates/base.html


#### 23.30 House keeping: Modifikasi README.md file

        modified:   README.md



### 24. USER ACTIONS
--------------------

#### 24.1 Membuat laman account - template, view, urls + link pada navbar

        Steps:

        1. Buat file baru: users/account.html
        2. Isi basic template
        3. Buat view method: account_user_view
        4. Buat path account
        5. Buat link pada navbar
        6. Test it out :)

        modified:   README.md
        modified:   templates/shared/header.html
        new file:   users/templates/users/account.html
        modified:   users/urls.py
        modified:   users/views.py


#### 24.2 Menyembunyikan My Account menu dari un-logged in user

        Steps:

        1. Buat file: templates/shared/header.html dan
           pindahkan menu My Account
        2. Test it out login :)
        3. Test it out logout :)

        modified:   README.md
        modified:   templates/shared/header.html


#### 24.3 Add template theme pada laman account

        Steps:

        1. Buka file: users/templates/users/account.html
           dan add theme
        2. Test it :)

        modified:   README.md
        modified:   users/templates/users/account.html


#### 24.4 Loading user information

        Steps:

        1. Load data pada account_user_view
        2. Display data pada laman account
        3. Display owner name pada laman project_single
        4. Ubah link pada laman projects
        5. Test create a new project

        modified:   README.md
        modified:   projects/templates/projects/project_single.html
        modified:   projects/templates/projects/projects.html
        modified:   users/templates/users/account.html
        modified:   users/views.py

        Steps membuat proyek baru:
        --------------------------

        1. Login
        2. Buat proyek baru

        NOTE:

        1. Proyek baru bisa dibuat
        2. Tapi nama owner tidak muncul
        3. Nama owner harus diisi secara 
           manual melalu admin panel oleh superuser


#### 24.5 Membuat laman edit accout - Template, View dan Urls

        Steps:

        1. Modifikasi laman projects dengan menghapus bagian file
        2. Buat file baru: users/templates/users/profile_form.html
        3. Isi basic template pada file baru tersebut
        4. Buat view function
        5. Buat path
        6. Test it out :)

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        new file:   users/templates/users/profile_form.html
        modified:   users/urls.py
        modified:   users/views.py


#### 24.6 Menambahkan basic form pada laman profile_form

        Steps:

        1. Mentautkan laman account dan profile_form
        2. Menambahkan basic form pada profile_form
        3. Test it out :)

        modified:   README.md
        modified:   users/templates/users/account.html
        modified:   users/templates/users/profile_form.html


#### 24.7 House keeping - Merubah nama message pada git repositori

        modified:   README.md


#### 24.8 Menambahkan form fields pada profile_form

        Steps:

        1. Import model Profile dan buat class ProfileForm pada users/forms.py
        2. Import dan load ProfileForm pada views.py
        3. Display instance ProfileForm pada profile_form + style
        4. Test it out :)

        modified:   README.md
        modified:   users/forms.py
        modified:   users/templates/users/profile_form.html
        modified:   users/views.py


#### 24.9 Membuat updateUser signals untuk mengupdate profile dan src otomatis mengupdate user, tetapi TIDAK sebaliknya

        Steps:

        1. Buka file users/signals.py dan buat method updateUser
        2. Menghapus profile: lihat laman users dan tentukan 
           profile yg akan dihapus, terutama profile yg tdk lengkap
        3. Menghapus profile: Go to admin panel dan hapus profile
           user yg sdh ditentukan pada poin 2.
        4. Pada admin panel: testing update satu atau dua profile
        5. Pada admin panel, buka user yg profilenya baru diupdate

        NOTE:

        1. Meng-update profile pada admin, maka data user scr
           otomatis akan ter-update.
        2. Tapi meng-update user melalui Users (admin), hal
           itu tdk meng-update profile user.

        Apa artinya hal itu?

        Itu berarti bahwa jika user meng-update profilenya
        melalu laman web, maka data user pada db jg
        akan ter-update scr otomatis.

        modified:   README.md
        modified:   users/signals.py


#### 24.10 Membatasi fields yg ditampilkan pada profile_form

        Steps:

        1. Menambah field baru 'social_stackoverflow' pd model Profile + migrasi
        2. Pada users/forms.py tentukan fields yang akan ditampilkan
        3. Periksa hasilnya

        NOTE:

        Pada tahap ini form belum bisa difungsikan karena
        belum ada logicnya pada account_user_edit_view.

        modified:   README.md
        modified:   users/forms.py
        new file:   users/migrations/0005_profile_social_stackoverflow.py
        modified:   users/models.py


#### 24.11 Membuat profile_form berfungsi

        Steps:

        1. Update profile_form
        2. Buat logic pada account_user_edit_view
        3. Periksa hasilnya
        4. Test it out :)

        NOTE:

        1. profile_form berfungsi.
        1.1 Berhasil melakukan update profile
        1.2 Berhasil melakukan update username pada db

        modified:   README.md
        modified:   users/templates/users/profile_form.html
        modified:   users/views.py


#### 24.12 Styling profile_form

        Steps:

        1. Modifikasi forms.py
        2. Modifikasi profile_form.html
        3. Modifikasi auth/register_login.html
        4. Modifkasi view

        modified:   README.md
        modified:   users/forms.py
        modified:   users/templates/users/auth/register_login.html
        modified:   users/templates/users/profile_form.html
        modified:   users/views.py


#### 24.13 House keeping: Merubah tata-letak codes profile_form

        NOTE:

        Proyek baru berhasil dibuat dari laman web.
        Namun, nama owner/user TIDAK MUNCUL pada laman web.



### 25. CRUD USER-BASED PROJECT
-------------------------------


#### 25.1 Menambahkan link Edite dan Delete proyek

        Steps:

        1. Tambahkan link
        2. Test it out :)

        modified:   README.md
        modified:   users/templates/users/account.html


#### 25.2 CRUD - CREATE : Menambahkan logic pada project_create_view untuk memungkinkan spesifik user membuat proyek baru

        Steps:

        1. Update project_create_view method
        2. Update projects/forms.py
        3. Test it out
        4. Periksa hasilnya :)

        modified:   projects/forms.py
        modified:   projects/views.py


#### 25.3 CRUD - UPDATE :  Menambahkan logic pada project_update_view untuk memungkinkan spesifik user mengupdate proyeknya

        Steps:

        1. Update project_update_view method
        2. Test it out dan periksa hasilnya

        modified:   README.md
        modified:   projects/views.py
        new file:   static/images/PYTHON.png


#### 25.4 CRUD - DELETE :   Menambahkan logic pada project_delete_view untuk memungkinkan spesifik user menghapus proyeknya

        Steps:

        1. Update project_delete_view method
        2. Test it out dan periksa hasilnya :)
        
        modified:   README.md
        modified:   projects/views.py


#### 25.5 CRUD - TESTING 

        Steps:

        1. Register user baru
        2. Update account
        3. Buat proyek
        4. Lakukan CRUD pada proyek baru tsb.

        NOTE:

        CRUD berhasil :)

        modified:   README.md
        new file:   static/images/profiles/darling.PNG
        new file:   static/images/samsung-tv-ua65t.PNG



### 26. CRUD USER-BASED SKILL
-----------------------------


#### 26.1 CRUD - CREATE Part 1: Membuat skill_form Template, View dan Urls

        Steps:

        1. Membuat file baru: users/templates/users/skill_form.html
        2. Membuat basic template untuk skill_form
        3. Membuat view method: skill_create_view
        4. Membuat path
        5. Mentautkan skill_form dan laman account
        6. Test it out :)

        modified:   README.md
        modified:   users/templates/users/account.html
        new file:   users/templates/users/skill_form.html
        modified:   users/urls.py
        modified:   users/views.py


#### 26.2 CRUD - CREATE Part 2: Membuat SkillForm model dan display pada laman skill_form

        Steps:

        1. Membuat SkillForm model
        2. Import SkillForm model pada users/view
        3. Load SkilForm pada skill_create_view
        4. Render SkillForm pada laman skill_form
        5. Periksa hasilnya :)

        modified:   users/forms.py
        modified:   users/templates/users/skill_form.html
        modified:   users/views.py


#### 26.3 CRUD - CREATE Part 3: Styling skill_form

        Steps:

        1. Style SkillForm
        2. Periksa hasilnya

        modified:   README.md
        modified:   users/templates/users/skill_form.html


#### 26.4 CRUD - CREATE Part 3: Add logic pada method skill_create_view agar user bisa membuat skill dari skill_form

        Steps:

        1. Buat logic untuk membuat skill
        2. Test it out dan periksa hasilnya :)

        modified:   README.md
        modified:   users/views.py


#### 26.5 CRUD - UPDATE Part 1: Membuat method skill_update_view untuk mengupdate skill

        Steps:

        1. Buat logic pada skill_update_view
        2. Buat path untuk update skill
        3. Tautk laman skill_form dan account
        4. Test it out
        5. Periksa hasilnya :)

        modified:   users/templates/users/account.html
        modified:   users/urls.py
        modified:   users/views.py


#### 26.6 CRUD - UPDATE Part 2: Sembunyikan/perlihatkan form title 'Create Skill' dan 'Update Skill'

        Steps:

        1. Buat variabel pada skill_update_view 
        2. Buat kondisional pada skill form
        3. Test it out :)

        modified:   README.md
        modified:   users/templates/users/skill_form.html
        modified:   users/views.py


#### 26.7 CRUD-DELETE: Delete skill

        Steps:

        1. Buat file: users/templates/users/skill_delete.html
        2. Isi template skill_delete.html
        3. Buat view method skill_delete_view
        4. Buat path
        5. Tautkan skill_delete dgn account
        6. Test it out
        7. Periksa hasilnya :)

        modified:   users/templates/users/account.html
        new file:   users/templates/users/skill_delete.html
        modified:   users/urls.py
        modified:   users/views.py


#### 26.8 CRUD-FLASH MESSAGES: Menampilkan pesan sukses operasi Create, Update dan Delete skill

        Steps:

        1. Isi pesan sukses pada view method Create, Update dan Delete skill
        2. Isi template laman users/skill_delete.html
        3. Test it out :)

        modified:   README.md
        modified:   users/templates/users/skill_delete.html
        modified:   users/views.py



### 27. SEARCH UNTUK PROFILE: NAMA, SHORT_INTRO DAN SKILL
---------------------------------------------------------


#### 27.1. SEARCH - Add url, Skenario dan persiapan

        Steps:

        1. Add url pada action dari search form

        NOTE Skenario dan persiapan:

        Kita akan melakukan Search atau pencarian informasi
        pada aplikasi kita dengan dua cara:

        1. Pada laman profiles; dan
        2. Pada laman projects.

        Ad 1. Laman Profiles.

        Pada laman Profilis atau home page, kita akan 
        lakukan pencarian terhadap developers atau siapapun
        yang tercatat dalam aplikasi kita melalui atribut
        mereka seperti:

        - nama, deskripsi dan skill mereka.

        Ad 2. Laman Projects

        Pada laman projects kita akan lakukan pencarian
        melalui atribut mereka, seperti:

        - judul proyek, deskripsi, tags yang berkaitan
          dengan proyek dan mungkin juga nama
          pengembangnya.

        modified:   README.md
        modified:   users/templates/users/profiles.html

        Langkah 1. Testing pencarian

        1. Buka users/profiles.html
        2. Lihat bagian form yang dimulai dengan <form class="form" action="#" 
        3. Ganti tanda pagar dengan {% url 'users:profiles' %}
           url itu dimaksudkan agar hasil pencarian bisa ditampilkan pada laman profiles.
        4. Buka browser anda dengan url ini http://localhost:8000/, lalu refresh
        5. Pada laman profil di bagian search, ketik sesuatu, misal anda ketik 'Torang Bisa Apa'
           lalu klik tanda SEARCH, maka hasilnya akan seperti ini:
           http://localhost:8000/?text=Torang+Bisa+Apa# 
        6. Periksa hasilnya pada url dari browser anda.
        7. Jika anda melakukan dengan benar, maka akan terlihat seperti pada gambar 27/04.
           http://localhost:8000/?text=Torang+Bisa+Apa#, terutama bagian dari text=Torang+Bisa+Apa#


#### 27.2. SEARCH - Testing the search result to terminal

        Langkah 2. Tampilkan hasil pencarian pada terminal

        1. Buka users/profiles.html, pada bagian form, 
           ubah nilai atribute name="text" menjadi name="search_query"
           , lihat gambar 27/05
        2. Buka file users/views.py, cari bagian def profile_view(request):
           lalu tulis code seperti pada gambar 27/06
        3. Lakukan:
           - Jalankan server dan buka aplikasi pada http://localhost:8000/
           - Pada search, ketik sesuatu, misal 'Torang Bisa Apa'
           - Lihat hasilnya pada terminal seperti terlihat pada gambar 27/07

        modified:   README.md
        modified:   users/templates/users/profiles.html
        modified:   users/views.py


#### 27.3. SEARCH - Pencarian melalui nama

        Langkah 3. Tampilkan hasil pencarian pada home page

        Note:

        Pada langkah 2, kita telah berhasil menampilkan
        informasi yang dicari pada terminal.
        Pada langkah ini, kita akan menampilkan hasil
        pencarian pada halaman depan atau home page.

        Untuk itu, kita akan melakukan:

        1. Buka file users/views.py, cari bagian def profile_view(request):
           - block dengan comment Step 3
           - ganti profiles = Profile.objects.all()
             dengan code yang ada pada Step 4
           - lihat gambar 27/09

        2. Pengujian:
           - Jalankan server anda
           - Buka browser
           - Ketik sesuatu, misal: ingafter63
           - Lihat gambar 27/10

           Note:

           Jika pada search anda ketik 'ing' atau 'i', maka akan
           ditampilkan hasil yang berbeda, coba lakukan 
           sendiri.

           Selanjutnya, coba dengan huruf atau kata yang lain
           seperti yang anda sukai.

        modified:   README.md
        modified:   users/views.py


#### 26.4. SEARCH - Membuat nilai pencarian tetap berada pada kotak pencarian


        NOTE:

        Pada langkah ke-2, setiap kali menulis sesuatu pada kotak pencarian,
        kemudian menekan tombol Search, hurup atau kata yang ditulis pada
        kotak pencarian terhapus.

        Sekarang kita akan membuat nilai pencarian akan tetap berada
        pada kotak pencarian.

        Langkah 3. Membuat nilai pencarian tetap berada pada kotak search

        1. Buka file users/views.py, cari bagian def profile_view(request):
           - tambahkan code ini: 'search_query':search_query ke dalam
             context dictionary, seperti terlihat pada gambar 27/12.
        2. Buka users/profiles.html, pada bagian form, tambahkan
           atribut value dan tambahkan varibale ini: 'search_query'
           yang terdapat di dalam context.
           Lihat gambar 27/13
        3. Lakukan pengujian dan periksa hasilnya: kata pada kotak pencarian
           tetap berada pada kotak pencarian setelah tombol Search diklik.

        modified:   README.md
        modified:   users/templates/users/profiles.html
        modified:   users/views.py


#### 27.5. SEARCH - Menggunakan Q look up untuk search

        NOTE:

        Pada langkah ke-3, terdapat sedikit masalah dalam melakukan pencarian dengan menggunakan name_icontains.

        Fungsi pencarian tidak dapat menemukan yang kita cari.
        Misal, bila huruf yang sama tidak terdapat pada nama dan
        short_intro.

        Jadi kita tidak dapat melakukan pencarian berganda, yakni: berdasarkan name dan short_intro

        Contoh: 

        Ref: Profile model

        name: ingafter63
        short_intro: Backend developer EX DB

        Pada name dan short_intro tidak memiliki karakter
        yang sama, misal (db). Bila pencarian dilakukan
        dengan mengketik db pada kotak pencarian,
        maka hasilnya akan nihil.

        Solusi dari masalah itu adalah menggunakan django module bernama Q look up search.

        Langkah 4. Pencarian menggunakan Q look up

        1. Buka file users/views.py, dan lakukan:
           - impor module Q
           - cari bagian def profile_view(request):, kemudian lakukan yang seperti terlihat pada gambar 27/15.

        2. Lakukan pengujian, hasilnya terlihat seperti pada gambar 27/16.

        modified:   README.md
        modified:   users/views.py


#### 27.6. SEARCH - Menggunakan Q, distinct dan icontains untuk melakukan  multiple search, termasuk pencarian skill dalam profile

        NOTE:

        Melakukan pencarian pada langkah ke-4, kita tidak dapat melakukan pencarian skill yang terdapat pada profile.

        Pada langkah 5, kita akan melakukan multiple search sehingga memungkinakan kita melakukan pencarian baik berdasarkan nama, short_intro dan skill.

        Langkah 5. Membuat multiple search

        1. Buka file users/views.py, profile_view(request) dan lakukan:
           - Pastikan model Skill sudah diimport
           - Blok semua langkah ke-5
           - Buat multiple search.
           Lebih jelasnya, lihat gambar 27/18.
        2. Lakukan pengujian, hasilnya terlihat seperti pada gambar 27/19.

        modified:   README.md
        modified:   users/views.py


#### 27.7. SEARCH - Codes separattions: Membuat file utility search

        NOTE:

        Pada langkah 5, fungsi pencarian untuk nama, short_intro dan skill pada laman home page telah berhasil.

        Selanjutnya kita akan membuat file utility dan memindahkan code pencarian ke dalam file itu, kemudian kita impor file itu untuk digunakan pada profile_view.

        Hal itu kita lakukan agar codes pada profile_view tidak terlalu gemuk.

        Langkah 6. Membuat multiple search

        1. Buat file baru: users/utils.py
        2. Pada utils.py buat fungsi searchProfile dan pindahkan code pencarian dari profile_view ke utils.py sebagai bagian dari fungsi searchProfile.
        3. Import dan load fungsi searchProfile pada profile_view
        4. Jalankan server dan lakukan pengujian. Saya telah melakukan pengujian dan hasilnya sama seperti pada langkah 5.

        modified:   README.md
        new file:   users/utils.py
        modified:   users/views.py


#### 27.8. House keeping: modifikasi README.md file

        modified:   README.md



### 28. SEARCH UNTUK PROYEK: TITLE, DESCRIPTION, OWNER DAN TAGS
---------------------------------------------------------------

#### 28.1 Membuat fungsi searchProjects

        NOTE:

        Kita telah berhasil membuat fungsi pencarian profiles.
        Sekarang kita akan membuat fungsi pencarian proyek.

        Langkah yang akan kita lakukan sama seperti pada langkah membuat fungsi pencarian profile. Namun kali ini lebih singkat karena semua langkah-langkah dasarnya telah kita bahas bersama.

        Yang akan kita lakukan sekarang adalah:

        1. Membuat file baru: projects/utils.py
        2. Membuat fungsi searchProjects dan logicnya.
        3. Mengimpor dan menggunakan fungsi searchProjects pada projects_view.
        4. Menambahkan atribut pada form pencarian.
        5. Menjalankan server dan melakukan pengujian. Lakukanlah pengujian sendiri sebagai bagian dari pembelajaran. Saya telah melakukan pengujian dan fungsi pencarian proyek berkerja dengan baik.

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        new file:   projects/utils.py
        modified:   projects/views.py



### 29. PAGINATION
------------------


#### 29.1 PAGINATION PART 1 - Menampilkan hanya 3 proyek pada halaman pertama


        NOTE: Tentang paginasi

        Anda pasti pernah membuka website, misalnya website berita KOMPAS. Website itu, biasanya berisi banyak informasi yg tersimpan pada database dari waktu ke waktu. 

        Informasi itu ditampilkan pada halaman website berdasarkan waktu inforamsi itu disimpan.

        Informasi terbaru, sesusungguh informasi itu disimpan paling terakhir, akan ditampilkan paling pertama secara otomatis. 

        Cara kerjanya saya sebut LIFO: Last In, First Out. Dengan cara ini, maka website tersebut akan terlihat selalu menampilkan informasi terkini. Sementara informasi yang lama masih tetap ada dan ditayangkan, namun seringkali informasi itu tidak terlihat pada halaman utama karena simtem membatasi inforamasi yang ditampilkan pada sebuah halaman agar kecepatan akses ke informasi tetap terjaga. 

        Misalnya pada halaman ke-1 hanya ditampilkan 10 berita, pada halaman ke-2 ditampilkan 10 berita lagi dan begitu seterusnya.

        Untuk beralih dari halaman ke-1 ke halaman ke-2 dan halaman-halaman berikutnya digunakan navigasi paginasi. Paginasi itu biasanya terletak pada bagian bawah dari halaman website.

        Pada laman aplikasi yang kita sedang bangun juga berisi navigasi paginasi. Namun paginasi itu belum berfungsi.

        Untuk itu, pada latihan kali ini kita akan belajar bagaimana cara memfungsikan paginasi itu selangkah demi selangkah.

        Kliklah menu projects, dan lihatlah bagian bawah laman itu. Di sini Anda akan menemukan napigasi seperti terlihat pada gambar 20/01.


        Langkah-langkah untuk memfungsikan paginasi


        1. Saya akan login sebagai admin. Setelah login saya akan mengklik menu Add Project untuk membuat 12 proyek baru.

        2. Refresh browser setelah proyek ke-12 di-submit. Anda akan melihat 'Proyek baru 12' terlihat paling di depan, padahal proyek itu yang terakhir saya buat.

        Pertanyaannya adalah, bagaimana cara mengturnya sehingga bisa seperti itu?

        Jawabannya sangat mudah. Periksalah Project model (class Project), di dalamnya terdapat field dengan nama 'created'. Dengan sedikit trik, lihat gambar 29/04, dengan membuat class Meta dan perintah ordering
        (ordering = ['-created']), maka proyek terakhir yang dibuat akan tampil paling depan. Trik itu memberi tanda - (baca minus) pada kata 'created'. Arti tanda minus itu adalah, tampilkanlah data proyek yang tersimpan di dalam database dengan urutan tampil LIFO: Last In, First Out atau yang terakhir yang ditampilkan sebagai yang pertama.

        3. Memulai paginasi - Membatasi hanya 3 proyek pada satu halaman

        Saat ini, di dalam database terdapat 18 proyek. Bila Anda perhatikan gambar 29/05, terlihat semua proyek yang tersimpan di dalam database ditampilkan dalam satu halaman. Bagaimana kalau ada 1.000 proyek? Dengan cara seperti ini, maka akses ke aplikasi kita akan menjadi sangat lambat karena user harus menunggu sampai semua data ditampilkan pada halaman pertama.

        Untuk itulah paginasi diperlukan untuk mengatur pembatasan jumlah proyek yang akan ditampilkan pada setiap halaman. Kali ini kita akan mencoba membatasi hanya 3 proyek ditampilkan pada setiap halaman. Caranya lihat pada gambar 29/06. 

        modified:   README.md
        modified:   projects/models.py
        modified:   projects/views.py


#### 29.2 PAGINATION PART 2 - Menampilkan 3 buah proyek berikutnya

        Steps:

        1. Ganti page = 1 menjadi page = 2
        2. Refresh browser
        3. Tiga buah proyek berikutnya, yakni Proyek baru 9, 8 dan 7 ditampilkan.

        Mudah bukan?

        Tapi cara ini tidak efektif karena masih dilakukan secara manual, yakni
        mengganti page=1 menjadi page=2.

        Berikut kita akan coba cara yang lebih efektif. 

        modified:   README.md
        modified:   projects/views.py

        DONE: :)


