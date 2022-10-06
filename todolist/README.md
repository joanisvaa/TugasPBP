Joan Isva Shanti Andrea
2106707712
PBP E
# Tugas 5 PBP
1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

- Inline CSS: kode CSS yang dituliskan secara langsung didalam atribut elemen HTML yang sepsifik.
    Contoh:
    ```
    <h1 style="color:blue; font-family: arial;">Loginr</h1>
    ```
    
    Kelebihan dari inline CSS adalah dapat sangat bermanfaat saat kita hanya ingin melakukan styling pada salah satu elemen saja dan kita tidak perlu   membuat file CSS ataupun mengakses file CSS yang terpisah. Selain itu, inline CSS lebih mudah untuk dilakukan sehingga cocok saat ingin melakukan percobaan atau memperbaiki kesalahan-kesalahan kecil.

    Kekurangan dari inline CSS adalah mengonsumsi banyak waktu dikarenakan kita harus melakukan styling pada setiap elemen HTML. Selain itu, melakukan styling pada setiaqp elemen dapat mempengaruhi ukuran halaman dan meningkatkan waktu download. 

- Internal CSS: kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) / <head> file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.
    Contoh:
    ```
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {
        background-color: blue;
    }
    h1 {
        color: red;
        padding: 60px;
    } 
    </style>
    </head>
    <body>

    <h1>Contoh Internal CSS</h1>
    <p>Paragraf baru</p>

    </body>
    </html>    
    ```
    
    Kelebihan dari internal CSS adalah kita tidak memerlukan file yang banyak dan juga kita dapat menggunakan class dan id selector di dalam file tersebut.

    Kekurangan dari internal CSS adalah tidak efisien saat kita ingin menggunakan CSS yang sama dalam beberapa file.

- External CSS: kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. 
    Contoh file .css:
    ```
    .xleftcol {
       float: left;
       width: 33%;
       background:#809900;
    }
    .xmiddlecol {
       float: left;
       width: 34%;
       background:#eff2df;
    }
    ```
   
    Kode tersebut kemudian di letakan di bagian <head> file HTML. 
    Kelebihan dari external CSS adalah proses pembuatan halaman yang lebih cepat dan efisien dikarenakan kita hanya perlu membuat satu file .css yang dapat digunakan berkali-kali. Selain itu, apabila kita ingin melakukan perubahan pada seluruh halaman website maka kita hanya perlu mengubah satu fil .css tersebut saja.

    Kekurangan dari external CSS adalah apabila proses loading file .css tersebut lama maka website tidak akan ter-render dengan benar. 

2. Jelaskan tag HTML5 yang kamu ketahui
```
"<a>" : tag yang digunakan saat ingin membuat elemen hyperlink. 
"<b>" : tag yang digunakana saat ingin membuat elemen text dengan style bold.
"<br>" : tag untuk membuat satu baris break.
"<div>" : tag untuk mendefinisikan sebuah section.
"<button>" : tag untuk membuat button/tombol yang dapat diklik.
"<form>" : tag yang mendefinisikan sebuah HTML form untuk input user.
"<head>" : tag untuk mendefinisikan bagian atas sebuah file HTML yang berisikan informasi mengenai dokumen tersebut seperti judul/title.
"<header>" : tag yang merepresentasikan bagian header dari sebuah dokumen atau section. 
"<h1>" - "<h6>" : tag untuk mendefinisikan heading HTML.
"<html>" : tag untuk mendefinisikan root dari dokumen HTML.
"<i>" : tag untuk mendefinisikan elemen text dengan style italic.
"<input>" : tag untuk mendefinisikan input control.
"<label>" : tag untuk mendefinisikan label untuk tag "<input>"
"<p>" : tag untuk mendefinisikan sebuah paragraf.
"<style>" : tag untuk mendefinisikan informasi mengenai style dari sebuah elemen.
"<table>" : tag untuk mendefiniskan sebuah tabel.
```

3. Jelaskan tipe-tipe CSS selector yang kamu ketahui
  
- Selector Tag
    Selector tag atau type akan memilih elemen berdasarkan nama tag sebuah elemen. 
    Contoh:
    ```
    p {
    color: blue;
    }
    ```
    
    Maka, selector akan menargetkan semua tag <p> yang ada pada file HTML dan mengubah elemen tersebut menjadi berwarna biru.
- Selector Class
    Selector yang akan memilih elemen berdasarkan nama class yang diberikan. 
    Contoh:
    ```
    Contoh:
    .blue {
      color: white;
      background: blue;
      padding: 5px;
    }
    ```
    
    Maka, selector akan menargetkan semua elemen dengan atribut class "blue". 
    Contoh:
    ```
    <b class="blue">CSS</b>
    
    ```
    
    Contoh tersebut akan menghasilkan penulisan CSS dalam style bold dengan warna, background, dan padding yang telah didefinikan pada selector class .blue. Jumlah selector class yang digunakan dapat lebih dari satu.
    
- Selector ID
    Selector ID adalah sebuah selector yang memiliki sifat yang sama dengan selector class, tetapi selector ID bersifat unik sehingga hanya dapat digunakan pada satu elemen saja. Selector ID ditandakan dengan "#".
    Contoh:
    ```
    #header {
    background: blue;
    color: white;
    height: 50px;
    padding: 50px;
    }   
    ```
    
- Selector Atribut
    Selector atribut adalah selector yang memiliki elemen berdasarkan atribut. Selector atribut memiliki sifat yang hampir sama dengan selector tag.
    Contoh:
    ```
    input[type=text] {
    background: none;
    color: cyan;
    padding: 10px;
    border: 1px solid cyan;
    }
    ```
    
    Selector tersebut akan menargetkan semua elemen input yang memiliki atribut "type" text.
    
- Selector Universal
     Selector yang digunakan untuk menargetkan semua elemen pada scope tertentu.
    Contoh:
    ```
    * {
    border: 1px solid black;
    }
    ```
    
    Maka, semua elemen akan memiliki border yang solid dengan ukuran 1 px dan berwarna hitam.  
- Selector Pseudo
    Selector pseudo adalah selector untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya. Terdapat dua jenis selector pseudo, yaitu pseudo class dan pseudo element.
    - Pseudo Class
        Pseudo class adalah selector yang menargetkan elemen berdasarkan state/kondisi. State/kondisi ini dapat berupa hover, focus, onclick, active, checked, link, dll.
        ```
        a:hover {
        color: green;
        }
        ```
        
        Maka, semua elemen dengan tag <a> akan memiliki warna hijau saat sedang keadaan hover.
    - Pseudo Element
        Pseudo element CSS dapat digunakan untuk menata bagian tertentu dari suatu elemen. Misalnya, dapat digunakan untuk: Style huruf pertama, atau baris, dari suatu elemen. Contoh selector pseudo elemen dapat berupa ::before, ::after, ::marker, ::placeholder, dll.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
Pertama, saya menambahkan potongan kode berikut ke base.html agar dapat menggunakan tailwind untuk styling elemen HTML. 
```
    ...
    ...
    <script src="https://cdn.tailwindcss.com"></script>
    ...
    ...
```
    
Kemudian, saya menghias semua halaman HTML yang ada pada folder Templates. Untuk membuat cards pada to do list, saya menambahkan potongan kode berikut.
```
   <div class = "grid gap-4 sm:grid-cols-5">
       
    {% for task in list_task %}
                    <div class = "bg-gradient-to-l from-rose-300 to-yellow-300 w-32 h-28 inline-block align-middle rounded-lg flex justify-center drop-shadow-2xl">
                        <div class = "align-middle">
                        <div class = "font-bold mt-4 text-lg underline underline-offset-1 decoration-pink-600">{{task.task_title}}</div>
                        <div>{{task.task_description}}</div>
                        <div class = "mt-2 text-xs">{{task.task_date}}</div>
                    </div>
                    </div>
                {% endfor %}
   <div>
```

Potongan kode berikut akan membuat sebuah card yang akan berisikan judul, deskripsi, dan tanggal dari task tersebut dan akan membuat kolom sebanyak 5 dengan gap 4. Baris tidak dispesifikasikan karena kita ingin membuat cards tersebut terus melanjut ke bawah halaman apabila task dari user banyak. Kemudian, saya menerapkan kode responsive kepada semua elemen sesuai dengan dokumentasi tailwind CSS. Terakhir, saya melakukan git add, commit, dan push. 
# Tugas 4 PBP
Link app: 
https://tugas2pbp-joan.herokuapp.com/todolist/

https://tugas2pbp-joan.herokuapp.com/todolist/login

https://tugas2pbp-joan.herokuapp.com/todolist/register

https://tugas2pbp-joan.herokuapp.com/todolist/logout

https://tugas2pbp-joan.herokuapp.com/todolist/create-task

User dummy:
1. Username: user1, Pass: pengguna1
2. Username: user2, Pass: pengguna2

1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Kegunaan dari {% csrf_token %} pada elemen <form> adalah untuk mencegah serangan CSRF atau (Cross-Site Request Forgery). {% csrf_token %} akan menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi karena berarti permintaan tersebut tidak berasal dari user yang sudah terverfikasi. 

Apabila kita tidak menggunakan potongan kode tersebut maka user yang tidak terverifikasi dapat menggunakan kredensial user (orang yang mengunjungi situs jahatnya) untuk melakukan beberapa tindakan di situs web lainnya yang memercayai browser atau identitas user yang sudah terverifikasi. Penyerang menggunakan status terverifikasi user untuk keuntungan mereka dengan mengubah permintaan user tersebut.

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }}) Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual?
Ya, bisa. Tujuan dari generator form.as_table adalah untuk mempermudah proses pembuatan tampilan agar form dirender dalam bentuk sebuah tabel. Berikut cara untuk melakukan rendering secara manual.

```
<form action="..." method="<(POST/GET)">
    {% csrf_token %}
    <input type="..." name="..." placeholder="..." class="..." atribut lainnya>
    ...
    ...
    <input type="..." name="..." placeholder="... class="..." atribut lainnya >
</form>

```

4. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
1. Seorang pengguna akan memberikan request dengan Type Address (http://host/path)
2. Browser akan membuat HTTP Request ke Type Address yang diberikan oleh pengguna
3. Server akan menerima HTTP Request tersebut dan menentukan views.py mana yang akan menangani path tersebut
4. Views.py akan menghasilkan halaman HTML Form
5. Browser akan menampilkan layout HTML kepada pengguna
6. Layout HTML Form yang dikirimkan ke user akan diisikan oleh user dan browser akan menghasilkan HTTP Request, methods, argument ke URL tujuan berdasarkan halaman HTML Form
7. Server akan menerima HTTP Request tersebut dan menentukan views.py mana yang akan menangani path tersebut
8. Server akan menghasilkan halaman HTML 
9. Browser akan menuampilkan layout HTML tersebut kepada pengguna

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama, saya membuat aplikasi baru dengan perintah startapp.
```
python3 manage.py startapp todolist
    
```

Kemudian, saya memasukkan aplikasi todolist ke dalam INSTALLED_APPS di file settings.py dan memasukkan path todolist/ ke dalam urlspatterns pada file urls.py di folder project django.
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'example_app',
    'katalog',
    'mywatchlist',
    'todolist'
]
    
```
Kemudian, saya membuat models.py pada folder todolist yang berisikan models untuk Task dan form
```
from turtle import title
from django.db import models

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        models.User, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    task_date = models.DateField(auto_now_add = True)
    task_title = models.TextField()
    task_description = models.TextField()
```
Setelah selesai mendefinisikan models.py, saya melakukan migrasi dengan perintah makemigrations dan migrate. Kemudian, saya mendefinisikan semua fungsi yang diperlukan pada file views.py 
```
def show_todolist(request):
    data_task = Task.objects.filter(user = request.user)
    context = {
    'list_task': data_task,
    'user': request.POST.get('username')
    }

    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def create_task(request):
    if request.method == 'POST':
        form = forms.create_task(request.POST)
        
        if form.is_valid():
            return redirect('todolist:todolist')
    else:
        messages.info(request, 'Input data task salah!')

    form = forms.create_task

    context = {
        'form' : form
    }
    return render(request, "create_task.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
```
Setelah itu, saya membuat beberapa file yang akan dijadikan template pada folder templates.py

File pertama adalah create_task.html. File ini digunakan sebagai template untuk tampilan halaman saat pengguna ingin membuat task baru. File kedua adalah login.html. File ini digunakan sebagai template untuk tampilan halaman saat pengguna ingin melakukan login. File ketiga adalah register.html. File ini digunakan sebagai template untuk tampilan halaman saat pengguna ingin melakukan registrasi akun. File terakhir adalah todolist.html. File tersebut akan digunakan sebagai template untuk tampilan halaman saat pengguna ingin melihat task-task yang mereka miliki. 

Tahap terakhir adalah untuk membuat urls.py untuk menambahkan path url ke urlpatterns sesuai dengan yang diperlukan.
```
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('create-task/', create_task, name='create_task'),
    path('logout/', logout_user, name='logout'),
]
```
