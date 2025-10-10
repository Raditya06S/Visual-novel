label business: 
    #popup image mengisi lamaran
scene bg 3
        
main "Oke lamaran udah dikirim, sekarang tinggal tunggu kabar dari HRD aja."


scene bg_sky with dissolve
"satu minggu kemudian"    

scene bg 3
main "Lho Email dari siapa ini? *Baca email* Oh, syukurlah aku masuk tahap interview "
#popup email pernyataan akan di interview

"Hari Interview pun tiba"
        
scene bg office

show eileen senang       
hrd "berdasarkan hasil screening data yang Anda berikan, interview dan penilaian internal kami,"

hrd "selamat [main] anda diterima di perusahaan kami, sebagai [route] "

hrd "Berikut jobdesk *popup jobdesk* yang nantinya akan dikerjakan selama Anda menjadi [route] ."
        
hrd "Apakah ada yang ingin ditanyakan?"
        
hrd "Kalau tidak ada maka Anda bisa bekerja mulai hari senin di minggu depan, Terima kasih atas kerja samanya"

"Pada hari pertama kamu masuk kerja, kamu langsung ditugaskan sebagai konsultan di perusahaan Jaya makmur yang bergerak di bidang manufaktur sejak tahun 2003. PT jaya Makmur sendiri saat ini memiliki mesin otomatis dalam proses pembuatan furnitur rumah tangga. "

main "selamat pagi pak/bu, perkenalkan saya [main] dari PT NBJ, hari ini saya ditugaskan sebagai consultan"

bos "Halo, selamat pagiii, wah selamat datang di PT Jaya makmur. Mulai hari ini kamu ditugaskan untuk membantu bagian produksi dan procurement yaa...."
main "oke siap bu..."
bos "sipp...."

"*Besok Harinya*"
"Tak lama di esok hari kamu bertugas sebagai konsultan di perusahaan jaya makmur. Kamu langsung bertugas di bagian produksi, namun kamu tidak bersentuhan langsung dengan bagian produksinya namun lebih ke arah memberikan masukan atas proses yang dilakukan di bagian produksi.  "

main "dalam sebulan PT jaya makmur mampu memproduksi berapa meja pak/bu?"
staff "Dalam sebulan target produksi kita itu sekitar 10.000 unit, tapi kita menaruh harga diangka 1.000.000 rupiah agar tidak terlalu mahal"
main "wihhhh banyak juga ya pak/bu...."
staff "iya kebetulan kita memaksimalkan kemampuan mesin produksi kita, meskipun mesin yang kita miliki tergolong tua..."
"Tak lama kemudian, dari lini produksi terdengar sebuah ledakan dari jalur produksi, ternyata mesin yang biasa digunakan untuk melelehkan bijih plastik meledak dikarenakan terlalu lama digunakan."
staff "duh... kok bisa begini ya....."
main "ada kemungkinan unitnya sudah terlalu lama digunakan pak/bu, dan tidak ada waktu untuk cooling down(istirahat)..."
staff "duh.... buat sekarang gimana ya..... diperbaiki atau beli unit baru ya?"

while True:
    menu:
        "Memilih untuk diperbaiki":
            jump badBusiness
        "Memilih untuk mengganti unit": 
            jump goodBusiness


label badBusiness:
    main "Sepertinya lebih baik diperbaiki pak, karena biaya yang dikeluarkan lebih sedikit dan lebih cepat pak"
    staff "oooo betul juga, nanti saya sampaikan ke pihak keuangan yah....."

    "Dari keputusan yang kamu ambil kurang tepat, karena setelah diperbaiki pun mesin yang dimiliki masih tetap rusak dan membuat produksi tidak berjalan secara optimal.  "

    "sehingga dari hal tersebut membuat perusahaan mengalami profit loss setiap bulannya. "
return


label goodBusiness:
    main "sepertinya lebih baik diganti deh pak, dikarenakan unit yang sekarang sedang beroperasi punya usia yang sudah cukup tua"
    staff "tapi... kan harganya mahal..."
    main " Tidak masalah, karena menurut kalkulasi saya"

    "*Menampilkan sheet kalkulasi* "
    "Harusny dengan penjualan unit saat ini dan pencicilan pembayaran pun mampu menutup produksi saat ini"
    main "dan berikut pak seperti ini untuk proyeksi kedepannya dengan unit baru"
    "*menampilkan sheet proyeksi* "
    staff " baiklah akan saya sampaikan dulu ke bagian procurement ya.... (pembelian)"

    "Tak lama pihak procurement pun menyetujui pembelian mesin produksi yang baru. "
    "Dan dari keputusan yang kamu berikan ke staff produksi, hal tersebut merupakan hal yang tepat. Karena dari adanya unit produksi yang baru, jumlah produksi pun meningkat begitupun dari kualitas yang dihasilkan juga. Dan semenjak adanya unit baru menunjukan profit yang terus meningkat. "

