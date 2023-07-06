# Tugas Gold Challenge Data Science Binar Academy
## Challenge : Membuat API untuk Cleansing Data dan Laporan Analisis Data
### Pengertian API
**API** merupakan singkatan dari Application Programming Interface, output dari proses kerja data science. API berfungsi melayani request dari Client/Customer dan mengembalikan sesuai request.
Bisa kita abaratkan seperti gambar berikut ini :
![image](https://github.com/christadel27/2300944_09_ADE_hate-speech_Challenge-Gold/assets/133072315/5f207ce2-0789-4d4d-b7ef-57324001165d)
ada 4 komponen yang akan kita temui dalam API, yaitu :
1. URL Design : Ibarat rumah, URL Design ini nomor rumahnya kalau di Restful API namanya URI (Uniform Resource Identifiers).
URL Design ini juga sering disebut dengan Endpoint atau route, yaitu ujung dari suatu network. Dari URL kalian bisa menemukan endpoint-nya sob, yaitu:
“/”
“/(text link website)”
“/(text link website-clean)
contohnya seperti gambar berikut :
![Screenshot 2023-07-06 113020](https://github.com/christadel27/2300944_09_ADE_hate-speech_Challenge-Gold/assets/133072315/ad41e206-73e1-40ad-b70c-35e2c563ef41)
dimana https://github.com/christadel27/2300944 adalah URL Design
2. HTTP Verbs : Saat mengakses URL tersebut, maka akan melalui tahapan proses yang disebut dengan HTTP verbs, hasilnya sendiri berupa request yang berhasil dan request yang salah (tidak berhasil).
![image](https://github.com/christadel27/2300944_09_ADE_hate-speech_Challenge-Gold/assets/133072315/be4c3338-e93b-4744-bb2c-eaaf8613d899)
Seperti pada gambar berikut :
![Screenshot 2023-07-06 114041](https://github.com/christadel27/2300944_09_ADE_hate-speech_Challenge-Gold/assets/133072315/d1bb4672-6968-4304-af3d-55d36d7e7e40)
4. HTTP Response Code : Seperti namanya yaitu HTTP Response Code maka komponen ini harus selalu menyertakan kode sesuai standar atas setiap request dari client. 
Adapun standar code yang digunakan sebagai berikut:
2xx: Response code yang menandakan request berhasil
4xx: Response code yang menandakan request mengalami kesalahan di sisi client
5xx: Response code yang mengalami kesalahan di sisi server.
![Screenshot 2023-07-06 114223](https://github.com/christadel27/2300944_09_ADE_hate-speech_Challenge-Gold/assets/133072315/ec4c2e7d-0624-4286-a2df-034c41cc14a3)
5. Format Response : Setelah diberi code dari komponen sebelah, maka server akan merespon lagi sob dengan format response, yaitu format JSON. 
Response di sini artinya adalah menghasilkan output, sesuai request. 
![image](https://github.com/christadel27/2300944_09_ADE_hate-speech_Challenge-Gold/assets/133072315/43de366d-dcfd-454b-8254-69fcfde44882)

### Pengertian Data
Data adalah sekumpulan keterangan ataupun fakta yang dibuat dengan kata-kata, kalimat, simbol, angka, dan lainnya. Data disini didapatkan melalui sebuah proses pencarian dan juga pengamatan yang tepat berdasarkan sumber-sumber tertentu. Adapun pengertian lain dari data yaitu sebagai suatu kumpulan keterangan atau deskripsi dasar yang berasal dari obyek ataupun kejadian.
Salah satu kemampuan sebagai seorang **data scientist** yaitu kemampuan dalam menganalisis data untuk menjawab permasalahan. Tujuan dari analisis data adalah mendapatkan kesimpilan, solusi serta insight dengan lebih mudah.
Ada empat langkah spesifik yang harus dilakukan dalam menganalisis data yaitu :
![image](https://github.com/christadel27/2300944_09_ADE_hate-speech_Challenge-Gold/assets/133072315/d08634eb-1a72-48e9-922e-be8dc50494f5)
1. Problem Definition : menjelaskan masalah apa sih yang harus dijawab, untuk memudahkan menjawabnya disempurnakan lewat 4 syarat yang harus dilakukan yaitu **Latar Belakang, Tujuan, Rumusan Masalah, dan Sumber Data**.
2. Data Preparation : adalah proses mencari dan mengumpulkan data yang diperlukan, baik berupa data primer maupun sekunder. Data primer adalah data yang dibuat oleh kita sendiri, mulai dari mengambil data mentah sampai mengolah jadi data yang siap dianalisis.
Sedangkan data sekunder itu adalah data yang diambil dari sumber lain. Kalau sudah terkumpul, data tadi harus dibersihkan dan dikondisikan sesuai dengan kebutuhan analisis data, melalui data cleansing.
3. Analyze : menganalisis data, Ada empat metode analisis yang bisa pakai :
   Descriptive Analytics tujuan dari analisis ini untuk mencari tahu kondisi data dan menemukan tren serta pola data.
   Diagnostic Analytics tujuan dari analisis ini untuk mencari tahu permasalahan dari data, disini akan menggali datanya lebih detail.
   Predictive Analytics bertujuan untuk mencari tahu apa yang akan terjadi berdasarkan data yang sudah ada atau data yang lampau.
   Prescriptive Analytics bertujuan untuk melihat masa depan atau mencari prediksi yang akan terjadi dan merekomendasikan solusi.
4. Communicate Results : menyampaikan hasil dari analisis tersebut dalam bentuk laporan
   
### Proses Dalam Mengerjakan Tugas
1. Data harus Dibersihkan terlebih dahulu bisa menggunakan Python, Pandas, dan RegEX
2. Menganalisis Data, untuk tugas yang diberikan data berbentuk teks dengan menggunakan _Descriptive Analytics_ atau sering disebut dengan **EDA (Exploratory Data Analysis)**
3. Hasil analisis yang telah dibuat kita buat dalam API menggunakan Flask dan Swagger UI

Untuk lebih lanjut hasil laporan dapat dilihat dalam laporan analisis data dalam bentuk ppt.
Referensi : materi binar academy gold
