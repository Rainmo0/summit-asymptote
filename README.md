### Tugas 2

## Bagaimana saya menjalankan sesuai arahan checklist tugas.
Apa yang saya lakukan tidak jauh dari apa yang tutorial 1 diajarkan.  
Hanya saja ada tambahan seperti model yang sesuai dengan kriteria tugas 2 dan mendefinisikan nama, tujuan pada aplikasi web tersebut.

## Alur Request-Response Django: Hubungan urls.py, views.py, models.py, dan Template HTML.
![bagan eak](https://krify.co/wp-content/uploads/2019/06/Django-Work-flow.jpg)
__reference: https://krify.co/wp-content/uploads/2019/06/Django-Work-flow.jpg__  

1. Mendapatkan request dari user melalui Django.
2. Kemudian proses melalui URL dan dilanjutkan ke View.
3. View memproses request, bila ada data dari database, View memanggil models.py. Models melakukan query ke database yang hasilnya dikembalikan ke View.
4. Setelah proses selesai, hasilnya dirender melalui HTML.
5. Django mengembalikan HTML menuju user sebagai response.

## Peran settings.py.
Settings.py adalah file yang mengandung semua konfigurasi yang diatur
oleh kita sendiri dan ini memengaruhi behavior dan environment pada django yang kita gunakan. 
Ada beberapa konfigurasi seperti host yang diperbolehkan, mode debug, dan lain-lain.

## Bagaimana migrasi database di Django?
1. Setelah membuat/mengubah `models.py`
2. Jalankan kode `python manage.py makemigrations`
3. Lalu aplikasikan ke basis data `python manage.py migrate`

## Kenapa Django dipilih sebagai materi untuk pemula?
Django memiliki banyak fitur yang sudah tersedia, memudahkan pemula untuk belajar cara menggunakan fiturnya saja. 
Selain itu, Django juga memiliki dokumentasi yang sangat rapih dan komprehensif sehingga
bisa dituju bila ada fitur yang berguna atau mencari cara tahu menggunakannya. 
Django bersifat simpel, fleksibel, konsisten, skalabilitas membuat pemula 
lebih cepat memahami alur kerja pengembangan web tanpa harus membangun segalanya dari nol. Penggunaan
arsitektur MVT juga ikut berperan untuk memudahkan pemula belajar.

## Feedback untuk asisten dosen tutorial 1.
Untuk feedback saya merasa tidak ada, karena saya rasa asisten dosen sudah cukup untuk
menawarkan bantuan. Hebat.

### Tugas 3

## Keperluan dalam data delivery dalam mengimplementasian sebuah platform
Data delivery adalah proses pengiriman data. Misal, dari server ke aplikasi atau dalam projek ini dari database ke pengguna. Tujuannya supaya data yang sudah ada bisa disampai dengan cepat dan aman serta konsisten. 

Jadi data harus disimpan disuatu tempat yang bisa disebut sebagai 'gudang' kemudian data akan di kirim melalui data delivery ke pengguna.

## XML atau JSON?
XML ataupun JSON merupakan format data yang umum digunakan pada keperluan data delivery. XML dirancang untuk mudah dimengerti dengan pengguna hanya membacanya. JSON juga mirip seperti XML yang mudah dibaca. Pemilihan XML atau JSON tergantung dari kelebihan dan kekurangan masing-masing. 

JSON mendukung tipe data sepertin strings, numbers, dan objects selain itu JSON juga dukung boolean arrays. XML tidak bisa tanpa menambahkan tag tambahan. Namun, XML lebih fleksibel dan mendukung tipe data yang kompleks seperti data binari dan timestamps.

## Fungsi dari method is_valid() dalam pembuatan form

Fungsi utama dari `is_valid()` adalah mengecek apakah data yang dikirim ke form sudah sesuai dengan aturan validasi yang ditentukan.

Misal ada form menerima data yang kemudian memanggil method `is_valid()`. Didalamnya, data akan di tes dengan beberapa validasi seperti field yang diharuskan ada, dsb. Kemudian bila valid, maka data akan dibersihkan dan siap dipakai. Jika di projek ini, form akan disimpan setelah siap dipakai. Namun bila tidak valid, maka akan muncul error yang akan dikembalikan ke pengguna.

## Pentingnya csrf_token saat membuat form

CSRF token sangatlah penting karena berfungsi sebagai pelindung dari serangan Cross-Site Request Forgery.

Ibarat sebuah tanda tangan rahasia yang memastikan request memang berasal dari form asli di website sendiri, bukan dari jebakan pihak luar.

Jadi CSRF token bekerja yang diawali dengan menyelipkan kode unik yang acak di setiap form. Kemudian kode ini ikut terkirim saat user sumbit form. Server akan mengecek apakah token cocok dengan yang disimpan sama user. Jika tidak, request ditolak.

## Feedback untuk asisten dosen tutorial 2.
Untuk feedback kepada asisten dosen tutorial 2 sudah cukup dan melaksanakan tugasnya. Keren.

## Penggunaan Postman 
XML
![XML](images/xml.PNG)

JSON
![JSON](images/json.PNG)

XML by id
![XML by id](images/xml1.PNG)

JSON by id
![JSON by id](images/json2.PNG)

## Terima kasih sudah mengunjungi!
Repositori ini dibuat oleh Farras Syafiq Ulumuddin dari kelas PBP A.  
Link menuju website : [https://farras-syafiq-summitasymptote.pbp.cs.ui.ac.id].
