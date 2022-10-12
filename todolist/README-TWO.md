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
 
 
