Joan Isva Shanti Andrea
2106707712
PBP E
# Tugas 6 PBP

 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
 
Saat menggunakan synchronus programming, task akan dilakukan satu per satu dan kita harus mennunggu sebuah task untuk selesai sebelum pindah ke task berikutnya. Asynchronus programming artinya kita dapat melakukan ke task lainnya tanpa harus menunggu untuk task sebelumnya selesai. Dengan asynchronus programming, kita dapat melakukan banyak task sekaligus. Hal ini akan mempercepat proses pengerjaan task. 

Perbedaan antara asynchronus dan synchronus:
- Asynchronus programming bersifat multi-thread, yang berarti operasi atau program dapat berjalan secara paralel. Synchronus bersifat single-thread sehingga hanya ada satu task yang dapat berjalan di satu waktu. 
- Asynchronus tidak melakukan blokir, yang berarti kita dapat mengirimkan banyak request ke server. Synchronis melakukan lokir dimana kita hanya dapat mengirimkan satu request ke server pada satu waktu dan harus menunggu agar request tersebut selesai. 
- Asynchronus akan meningkatkan throughput dari sistem karena beberapa operasi dapat berjalan secara bersamaan. Synchronus bersifat lebih lambat dikarenakan kita harus menunggu untuk sebuah task untuk selesai terlebih dahulu sebelum lanjut melakukan task lainnya. 


 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
JavaScript menggunakan model event-driven programming. Hal ini berarti alur program ditentukan oleh event seperti input pengguna (klik mouse, penekanan tombol). Pemrograman event-driven digunakan untuk menyinkronkan terjadinya beberapa peristiwa dan membuat program sesederhana mungkin. 
Salah satu penerapan pada tugas ini:
```
$('#button_modal').click(function(){
            console.log("masuk modal button");
        $.post("/todolist/add/", {task_title: $('#new_task_title').val(), task_desc: $('#new_task_desc').val()} ,function(data) {
            $('#tasks').append(
                    `<div class = "bg-gradient-to-l from-rose-300 to-yellow-300 w-32 h-28 inline-block align-middle rounded-lg flex justify-center drop-shadow-2xl">
                        <div class = "align-middle">
                        <div class = "font-bold mt-4 text-lg underline underline-offset-1 decoration-pink-600">${data.title}</div>
                        <div>${data.description}</div>
                        <div class = "mt-2 text-xs">${data.date}</div>
                    </div>
                    </div>`
                    );
        });
        });
```

Potongan kode berikut bergantung pada event click yang dilakukan oleh user pada button pembuatan task. Apaila button_modal diklik, maka akan melakukan method post. 

 4. Jelaskan penerapan asynchronous programming pada AJAX.
 
AJAX adalah singkatan dari "Asynchronous JavaScript and XML", adalah teknik yang memungkinkan halaman web diperbarui secara asynchronus, yang berarti bahwa browser tidak perlu memuat ulang seluruh halaman ketika terdapat perubahan pada halaman. AJAX hanya meneruskan informasi yang diperbarui ke dan dari server. AJAX akan memproses request secara asynchronus untuk menghindari proses pengambilan data dari lama yang lama. 

 6. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama, saya membuat method pada views.py bernama show_data_json yang akan memengembalikan semua data task dalam bentuk file json. 
```
def show_data_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Kemudian, saya menambahkan path todolist/json ke dalam urls.py di folder todolist
```
urlpatterns = [
    ...
    path('add/', create_task_modal, name='create_task_modal'),
]
```
Kemudian, saya membuat fungsi method get di dalam todolist.html untuk melakukan pengambilan data task. Untuk menampilkan cards, saya menggunakan id "#tasks" pada potongan kode yang menandakan blok cards. Kemudian, cards dari hasil pengambilan data task akan diappend ke dalam <div> dengan id "#task".
```
        $.get("/todolist/json", function(data) {
            for (i = 0; i<data.length; i++){
                $('#tasks').append(
                    `<div class = "bg-gradient-to-l from-rose-300 to-yellow-300 w-32 h-32 inline-block align-middle rounded-lg flex justify-center drop-shadow-2xl">
                        <div class = "align-middle">
                        <div class = "font-bold mt-4 text-lg underline underline-offset-1 decoration-pink-600">${data[i].fields.task_title}</div>
                        <div>${data[i].fields.task_description}</div>
                        <div class = "mt-2 text-xs">${data[i].fields.task_date}</div>
                    </div>
                    </div>`
                    );
            }}
```
Langkah berikutnya adalah untuk membuat tombol add task dengan sebuah modal. Untuk melakukan hal ini, saya akan menggunakan bootstrap sehingga saya perlu meletakkan link dan script yang akan digunakan pada file todolist.html.
```
...
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
...
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
...
```
Kemudian, saya membuat modal dan tombol yang akan digunakan untuk membuat task baru pada file todolist.html.
```
 <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Buat Task Baru</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <div class = "flex justify-center">  
                <label class="block">
                    <span class="after:content-['*'] after:ml-0.5 after:text-red-500 block text-sm font-medium text-slate-700 text-left w-40 ml-4 mr-4">Task Title</span>
                    <div><input id = new_task_title type=text required class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
                        focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
                        invalid:border-pink-500 invalid:text-pink-600
                        focus:invalid:border-pink-500 focus:invalid:ring-pink-500 mb-4 w-64 ml-4 mr-4" class = "form-control"
                        name="task_title"></div>

                        <label class="block">
                            <span class="after:content-['*'] after:ml-0.5 after:text-red-500 block text-sm font-medium text-slate-700 text-left w-40 ml-4 mr-4">Task Description</span>
                            <div><input id = new_task_desc type=text required class="mt-1 block w-full px-3 py-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400
                                focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
                                invalid:border-pink-500 invalid:text-pink-600
                                focus:invalid:border-pink-500 focus:invalid:ring-pink-500 mb-4 w-64 ml-4 mr-4" class = "form-control"
                                name="task_description"></div>
                </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button id = "button_modal" type="button" class="btn btn-warning">Save changes</button>
        </div>
      </div>
    </div>
  </div>
```
Kemudian, saya membuat method baru di file views.py yang berguna untuk melakukan penambahan task melalui modal yang sudah dibuat dan kemudian mengembalikan data tersebut dalam bentuk JSON. Tidak lupa saya nemabahkan path todolist/add/ ke dalam urls.py.
```
@csrf_exempt
def create_task_modal(request):

    if request.method == 'POST':
        title = request.POST.get('task_title')
        description = request.POST.get('task_desc')
        task =  Task.objects.create(task_title=title, task_description=description,task_date=datetime.date.today(), user=request.user)

        new_task = {
                'title':task.task_title,
                'description':task.task_description,
                'date':task.task_date,
        }

        return JsonResponse(new_task)
   
```
Langkah berikutnya adalah untuk membuat method post di file todolist.html untuk menghubungkan antara form yang baru saja ditambahkan dengan modal. Data yang dikembalikan oleh views akan ditampilkan dengan melakukan method append ke dalam blok cards yang memiliki id "#tasks".
```
     $('#button_modal').click(function(){
        $.post("/todolist/add/", {task_title: $('#new_task_title').val(), task_desc: $('#new_task_desc').val()} ,function(data) {
            $('#tasks').append(
                    `<div class = "bg-gradient-to-l from-rose-300 to-yellow-300 w-32 h-28 inline-block align-middle rounded-lg flex justify-center drop-shadow-2xl">
                        <div class = "align-middle">
                        <div class = "font-bold mt-4 text-lg underline underline-offset-1 decoration-pink-600">${data.title}</div>
                        <div>${data.description}</div>
                        <div class = "mt-2 text-xs">${data.date}</div>
                    </div>
                    </div>`
                    );
        });
        });
```
