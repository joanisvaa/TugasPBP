Joan Isva Shanti Andrea
2106707712
PBP E
# Tugas 4 PBP
Link app: https://tugas2pbp-joan.herokuapp.com/todolist/
1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Kegunaan dari {% csrf_token %} pada elemen <form> adalah untuk mencegah serangan CSRF atau (Cross-Site Request Forgery). {% csrf_token %} akan menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi karena berarti permintaan tersebut tidak berasal dari user yang sudah terverfikasi. 

Apabila kita tidak menggunakan potongan kode tersebut maka user yang tidak terverifikasi dapat menggunakan kredensial user (orang yang mengunjungi situs jahatnya) untuk melakukan beberapa tindakan di situs web lainnya yang memercayai browser atau identitas user yang sudah terverifikasi. Penyerang menggunakan status terverifikasi user untuk keuntungan mereka dengan mengubah permintaan user tersebut.

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?
Ya, bisa. Tujuan dari generator form.as_table adalah untuk mempermudah proses pembuatan tampilan agar form dirender dalam bentuk sebuah tabel.

3. Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Pertama, kita perlu membuat forms.py di dalam folder aplikasi yang kita inginkan. Kemudian, kita perlu me

Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

# Tugas 3 PBP 
Link app: https://tugas2pbp-joan.herokuapp.com/mywatchlist/
1. Jelaskan perbedaan antara JSON, XML, dan HTML!

JSON

JSON atau JavaScript Object Notation adalah format pertukaran data yang digunakan untuk merepresentasikan data yang terstruktur dalam format yang dapat dibaca oleh manusia. JSON bersifat self-describing sehingga sangat mudah untuk dipahami. JSON menggunakan teks dan tipe data numerik untuk merepresentasikan objek. JSON dibuat berdasarkan pada sintaks objek JavaScript dan bahasa JavaScript. Syntax dari JSON jauh lebih ringan dibandingkan dengan XML, contoh dari perbedaan syntaxnya adalah tidak adanya start/end tags yang diperlukan di XML dan HTML. JSON berorientasi pada data yang menyebabkan sedikitnya redundansi yang ada saat menggunakan JSON untuk pertukaran data. JSON mendukung beberapa tipe data, yaitu string, integer, array, dan objek. JSON hanya mendukung UTF-8 encoding dan tidak mendukung objek yang bersifat _native._ JSON dianggap sebagai format yang lebih cocok untuk pertukaran data antara aplikasi web karena fleksibilitas yang dimiliki. 

XML

XML atau Extensive Markup Language adalah format data berbasis teks yang berasal dari SGML (ISO 8879) dan ditulis dengan cara yang sama dengan HTML. XML bersifat self-descriptive sehingga dapat langsung terbaca data yang dikirimkan. XML adalah versi sederhana dari SGML yang digunakan untuk menyimpan dan mewakili data terstruktur dalam format yang dapat dibaca oleh mesin dan dapat dibaca manusia. XML berorientasi pada dokumen dibandingkan dengan JSON yang berorientasi pada data. XML memiliki syntax yang lebih berat dan kompleks dibandingkan dengan JSON karena membutuhkan karakter yang lebih banyak untuk merepresentasikan data yang sama. XML mendukung numerik, teks, gambar, graf, dll tetapi tidak mendukung array layaknya JSON. 

HTML

HTML atau Hypertext Markup Language adalah format yanag membuat data lebih interaktif dengan berbagai fitur pemformatan. HTML berorientasi pada tampilan data sehingga HTML lebih fokus kepada tampilan dari data tersebut dibandingkan dengan XML dan JSON yang fokus pada pertukaran data.


3. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Saat kita mengembangkan suatu platform, maka ada saatnya dimana kita akan perlu untuk mengirimkan data dari satu stack ke stack lainnya. Bentuk dari data yang dikirimkan dapat bermacam-macam. Disinilah data delivery memainkan peran yang besar. Data delivery membantu kita untuk mengirimkan data-data tersebut. Terdapat beberapa contoh format data yang umum digunakan antara lain HTML, XML, dan JSON. 

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Saya memulai aplikasi baru bernama mywatchlist dengan command 'startapp' pada terminal. Kemudian, saya 'mywatchlist' pada settings.py pada folder project_django ke dalam variable 'INSTALLED_APPS' dan juga membuat kelas 'MyWatchList' pada models.py yang berisikan atribut yang akan dimiliki oleh setiap filmnya. Kemudian, saya juga melakukan migrasi untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal. Setelah itu, saya membuat file json bernama initial_mywatchlist_data.json dan menuliskan semua film sebagai data yang akan ditampilkan nantinya. Untuk mengimplementasikan sebuah fitur dalam 3 format. Saya membuat beberapa fungsi (show_html, show_json, show_json_by_id, show_xml, show_xml_by_id) yang akan menampilkan data mywatchlist pada file views.py dan tidak lupa saya menuliskan path pada urlpatterns di file urls.py untuk setiap formatnya untuk melakukan routing. Kemudian, saya melakukan deployment ke heroku. Untuk mengakses URL menggunakan postman, saya menuliskan link url yang terdapat pada soal menggunakan "GET" dan mengirimkan request. Kemudian, saya membuat unit test pada test.py untuk menguji ketiga URL tersebut. 

<img width="898" alt="Screen Shot 2022-09-21 at 21 40 59" src="https://user-images.githubusercontent.com/101711787/191656953-6e0ead63-f47a-40d7-a6af-005f522b4266.png">
<img width="898" alt="Screen Shot 2022-09-21 at 21 40 47" src="https://user-images.githubusercontent.com/101711787/191656978-3618ca55-66b5-47cd-9a9a-1096f7227476.png">
<img width="902" alt="Screen Shot 2022-09-21 at 21 40 36" src="https://user-images.githubusercontent.com/101711787/191657003-6f22a282-33cc-45bc-9a62-aaa8eeb9e4d1.png">


# Tugas 2 PBP 
Link app: https://tugas2pbp-joan.herokuapp.com/katalog/

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
<img width="718" alt="Screen Shot 2022-09-15 at 09 35 21" src="https://user-images.githubusercontent.com/101711787/190300191-0918f1cc-564e-4787-a78f-62589b9840fe.png">

Model berperan sebagai penyedia interface untuk menyimpan dan mengatur data pada database. Views berperan sebagai penerima input user yang dibuat oleh Template. Melalui Models, Views menerima data dari database dan mengirimkan data tersebut kepada user. Template berperan sebagai user interface bagi user. User akan meminta sebuah URL request untuk mengambil data melalui template pada Django. Kemudian, Django akan mencari URL request tersebut. URL akan memanggil Views dan Views akan berinteraksi dengan Model dan mengambil data dari database. Views akan mengcompile response yang dibuat oleh Model kembali ke Template. Siklus request-respons akan dimulai.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment berfungsi untuk mengisolasi package serta dependencies dari aplikasi. Virtual environment berfungsi untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek Django sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Setiap proyek Django sebaiknya memiliki virtualenv-nya sendiri. Virtual environment pada sebuah projek Django bukanlah suatu keharusan namun hal ini lebih baik dilakukan, terutama apabila terdapat beberapa proyek. 


3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Saya mengerjakan Tugas 2 PBP sesuai dengan cara yang sudah dipelajari pada Lab 1 yang lalu. 
Untuk langkah pertama, saya membuat sebuah fungsi dengan parameter request pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML. 

def show_katalog(request):
    return render(request, "katalog.html")
    
Kemudian saya membuat sebuah folder bernama templates di dalam folder aplikasi katalog dan membuat file bernama katalog.html. 
 
Untuk langkah kedua, saya membuat file HTML yang nantinya akan ditampilkan di browser dengan membuat file bernama urls.py yang melakukan routing terhadap fungsi views yang sudah dibuat pada langkah-langkah sebelumnya. Berikut 

from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]

Langkah ketiga adalah untuk menghubungkan models dengan views dan template atau mapping. Cara untuk menghubungkan models dengan views adalah untuk mengimport models yang sudah dibuat sebelumnya di dalam file views.py. Kemudian, saya melakukan mapping pada data yang telah ikut di-render pada fungsi views untuk memunculkan di halaman HTML. Untuk menampilkan daftar barang ke dalam tabel, saya melakukan iterasi variabel list_barang yang telah di-render ke dalam HTML.
Kemudian saya melakukan git add, commit, dan push. 

Langkah keempat adalah untuk melakukan deployment. Saya membuat aplikasi baru di akun heroku saya sesuai dengan nama aplikasi yang saya inginkan (tugas2pbp-joan). Kemudian, saya menambahkan file Tugas2PBP_HEROKU.txt di github yang berisikan API key dan app name dari aplikasi saya. Setelah itu, saya membuat 2 secret baru, yaitu API key dan app name secara terpisah. Terakhir, saya melakukan re-run all failed jobs di github dan melakukan deployment. 


# Template Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Pendahuluan

Repositori ini merupakan sebuah template yang dirancang untuk membantu mahasiswa yang sedang mengambil mata kuliah Pemrograman Berbasis Platform (CSGE602022) mengetahui struktur sebuah proyek aplikasi Django serta file dan konfigurasi yang penting dalam berjalannya aplikasi. Kamu dapat dengan bebas menyalin isi dari repositori ini atau memanfaatkan repositori ini sebagai pembelajaran sekaligus awalan dalam membuat sebuah proyek Django.

## Cara Menggunakan

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi:

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.
2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (_filesystem_) komputermu:

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```
3. Masuk ke dalam repositori yang sudah di-_clone_ dan jalankan perintah berikut
   untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```
4. Nyalakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
5. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara
   lokal:

   ```shell
   python manage.py runserver
   ```
7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

## Contoh Deployment 

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

Untuk melakukan deployment, kamu dapat melihat instruksi yang ada pada [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0).

Untuk contoh aplikasi Django yang sudah di deploy, dapat kamu akses di [https://django-pbp-template.herokuapp.com/](https://django-pbp-template.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.