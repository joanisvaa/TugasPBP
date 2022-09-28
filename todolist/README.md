Joan Isva Shanti Andrea
2106707712
PBP E

# Tugas 4 PBP
Link app: 
https://tugas2pbp-joan.herokuapp.com/todolist/
https://tugas2pbp-joan.herokuapp.com/todolist/login
https://tugas2pbp-joan.herokuapp.com/todolist/register
https://tugas2pbp-joan.herokuapp.com/todolist/logout
https://tugas2pbp-joan.herokuapp.com/todolist/create-task

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
