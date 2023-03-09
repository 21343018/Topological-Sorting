# Topological-Sorting
Disusun untuk memenuhi tugas mata kuliah Perancangan dan Analisis Algoritma (202223430034).

## Kompleksitas waktu Topologi Sort O(V+E), dimana V = Vertices, E = Edges.
Untuk mengetahui kompleksitas waktu dari algoritma, mari kita coba mencari kompleksitas waktu dari setiap langkah:
-	Untuk menentukan in-degree dari setiap node, kita harus melakukan iterasi melalui semua sisi grafik. Jadi kompleksitas waktu dari langkah ini adalah O(E).
-	Selanjutnya, cari node dengan in-degree sama dengan 0. Ini mengharuskan kita untuk melakukan iterasi melalui seluruh larik yang menyimpan in-degree dari setiap node. Ukuran array ini sama dengan V. Jadi, kompleksitas waktu langkah ini adalah O(V) .
-	Untuk setiap node dengan in-degree sama dengan nol, kita menghapusnya dari grafik dan mengurangi in-degree dari node yang terhubung dengannya. Di seluruh proses algoritma, berapa kali kita harus melakukan operasi pengurangan sama dengan jumlah sisi. Jadi itu akan memakan waktu O(E) .
-	Setiap kali kita mengurangi derajat dalam sebuah simpul, kita memeriksa apakah simpul tersebut telah mencapai status derajat dalam = 0. Ketika ini terjadi, kita memindahkannya ke tumpukan. Di seluruh proses algoritme, ini dapat terjadi pada waktu maksimal (V-1). Jadi run time dari operasi ini adalah O(V).
-	Pada akhirnya, kita membandingkan ukuran array yang diurutkan secara topologi yang dihasilkan dan ukuran grafik untuk memastikan bahwa itu bukan grafik siklik. Operasi ini dilakukan dalam O(1) waktu.
Jadi, menambahkan semua waktu proses individu, kompleksitas waktu pengurutan topologi adalah O(V+E).

Ini adalah kasus terbaik, kasus terburuk, dan kompleksitas waktu kasus rata-rata dari algoritme ini karena kami melakukan langkah yang sama terlepas dari bagaimana elemen disusun.
