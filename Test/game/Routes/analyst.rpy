label analyst:


"*Hari Pertama bekerja sebagai data analyst* "

"Pada saat ini kamu ditempatkan sebagai sales analyst di perusahaan yang bergerak di bidang FnB yang bernama /“Tumbas”/." 
"Tumbas sendiri merupakan sebuah perusahaan baru yang memiliki business process berupa Coffee Shop dengan konsep speciality cafe dengan produk penjualan terbesarnya ada di sektor kopi dengan racikan espresso. "

show mc normal
main " hmm Tumbas ya, dulu pas masih kuliah pengen sih kesana tapi dulu gk ada waktu sama uang buat jajannya."
main "oke deh berarti besok tinggal berangkat kesana buat diskusi terkait data penjuualan dia"
hide mc normal
"Hari pertama"

show staffKopi
staffKopi "Halo [main], kamu pasti ditugaskan oleh perusahan NJB untuk membantu dalam analisa data penjualan kan? "
show mc normal
main "betul pak hehehe, kebetulan saya membantu di sektor sales forecasting"
staffKopi "Oh kebetulan, untuk saat ini sales kita penjualannya agak sedikti drop. "
hide mc normal
hide staffKopi

"*Menampilkan data penjualan dan list produk yang terjual bulan ini dan bulan sebelumnya*"

show mc normal
main "lho hampir semua penjualan di semua produk mengalami penurunan ya......"
show staffKopi
staffKopi " iya, apa ini akibat dari tren yang ada di social media ya? Yang lagi ramainya kan sekarang trend matcha tuh....."
main "hmm kalau itu harus diliat dari berbagai macam sisi dan data sih, kita gk bisa ambil data dari sosmed aja."
staffKopi "tapi kalo kamu liat, setiap coffee shop yang jual matcha itu laku keras, kalo kita ikutin pasti laku juga."
hide staffKopi
hide mc normal

while True:
    menu:
        "Ikuti kata staff coffee shop":
            jump badAnalyst
        "minta lebih banyak data": 
            jump goodAnalyst

label badAnalyst:
    show mc normal at left_pos
    main " baik pak sepertinya kalau mengikuti trend di internet juga tidaklah buruk. "
    show staffKopi
    staffKopi " oke baik, mulai besok ktia coba racik sesuai dengan resep yang ada di internet ya..."
    hide mc normal
    hide staffKopi

    "Dengan adanya mengikuti trend yang ada di internet tidak semuanya berjalan dengan mulus. "

    "Dari resep dan racikan yang dibuat ternyata menghasilkan hasil yang kurang baik, namun dari keputusan dari staff coffee shop adalah tetap menjual dengan racikan dari internet "

    "Hingga pada waktu perilisan menu baru, sejumlah pelanggan memesan dan mereview menu terbaru itu dan mengatakan jika menu tersebut tidak rekomen dikarenakan rasanya yang tidak enak. Sehingga dari kejadian tersebut Tumbass pun mengalami kebangkrutan yang dimana penjualannya makin merosot. "

    return


label goodAnalyst:
    show mc normal
    main "pak saya mau meminta data yang lebih banyak"
    main " soalnya kalau hanya produk dan matcha saja yang akan dijual saya rasa tidak cukup untuk menaikan penjualan"
    show staffKopi
    staffKopi "Baik, berikut semua data yang berkaitan dengan penjualan dalam 2 bulan terakhir. "
    hide mc normal
    hide staffKopi


    "Berdasarkan data yang diberikan oleh Staff Tumbass, kamu menemukan sebuah penemuan menarik yang dimana ternyata penjualan terbanyak sebelum trend matcha jatuh kepada varian latte "
    
    "Maka dari itu mengingat Tumbass belum ada menu varian Matcha, maka Tumbass pun meracik 2 Menu baru, Coffe-Matcha dan Matcha latte"

    "Dan dari keputusan membuat 2 menu baru tersebut, ternyata membuat dampak positif, yang dimana penjualan Tumbass meningkat drastis dikarenakan hampir keseluruhan pelanggan yang datang, memesan kedua menu terbaru tersebut dikarenkan memiliki rasa yang unik dan berbeda dengan matcha yang ada di coffee shop diluar. Sehingga dari keputusan yang kamu ambil adalah benar. "


    return


