label business: 
scene bg sky
"Pada hari pertama kamu masuk kerja, kamu langsung ditugaskan sebagai konsultan di perusahaan Jaya makmur yang bergerak di bidang manufaktur sejak tahun 2003. PT jaya Makmur sendiri saat ini memiliki mesin otomatis dalam proses pembuatan furnitur rumah tangga. "

scene bg office 
show mc normal at left_pos
main "selamat pagi pak/bu, perkenalkan saya [main] dari PT NBJ, hari ini saya ditugaskan sebagai consultan"
show bos
bos "Halo, selamat pagiii, wah selamat datang di PT Jaya makmur. Mulai hari ini kamu ditugaskan untuk membantu bagian produksi dan procurement yaa...."
main "oke siap bu..."
bos "sipp...."
hide bos 
hide mc normal

scene bg sky
"*Besok Harinya*"
"Tak lama di esok hari kamu bertugas sebagai konsultan di perusahaan jaya makmur. Kamu langsung bertugas di bagian produksi, namun kamu tidak bersentuhan langsung dengan bagian produksinya namun lebih ke arah memberikan masukan atas proses yang dilakukan di bagian produksi.  "

scene bg pabrik

show mc confused at left_pos
main "dalam sebulan PT jaya makmur mampu memproduksi berapa meja pak/bu?"
show staff
staff "Dalam sebulan target produksi kita itu sekitar 10.000 unit, tapi kita menaruh harga diangka 1.000.000 rupiah agar tidak terlalu mahal"
show mc happy at left_pos
main "wihhhh banyak juga ya pak/bu...."
staff "iya kebetulan kita memaksimalkan kemampuan mesin produksi kita, meskipun mesin yang kita miliki tergolong tua..."
hide mc 
hide staff
"Tak lama kemudian, dari lini produksi terdengar sebuah ledakan dari jalur produksi, ternyata mesin yang biasa digunakan untuk melelehkan bijih plastik meledak dikarenakan terlalu lama digunakan."
show staff 
staff "duh... kok bisa begini ya....."
show mc normal at left_pos
main "ada kemungkinan unitnya sudah terlalu lama digunakan pak/bu, dan tidak ada waktu untuk cooling down(istirahat)..."
staff "duh.... buat sekarang gimana ya..... diperbaiki atau beli unit baru ya?"
hide mc normal
hide staff


while True:
    menu:
        "Memilih untuk diperbaiki":
            jump badBusiness
        "Memilih untuk mengganti unit": 
            jump goodBusiness


label badBusiness:
    show mc normal at left_pos
    main "Sepertinya lebih baik diperbaiki pak, karena biaya yang dikeluarkan lebih sedikit dan lebih cepat pak"
    show staff
    staff "oooo betul juga, nanti saya sampaikan ke pihak keuangan yah....."
    hide mc normal
    hide staff

    "Dari keputusan yang kamu ambil kurang tepat, karena setelah diperbaiki pun mesin yang dimiliki masih tetap rusak dan membuat produksi tidak berjalan secara optimal.  "
    "sehingga dari hal tersebut membuat perusahaan mengalami profit loss setiap bulannya. "
return


label goodBusiness:
    show mc normal at left_pos
    main "sepertinya lebih baik diganti deh pak, dikarenakan unit yang sekarang sedang beroperasi punya usia yang sudah cukup tua"
    show staff
    staff "tapi... kan harganya mahal..."
    main " Tidak masalah, karena menurut kalkulasi saya"
    hide mc normal
    hide staff

    "*Menampilkan sheet kalkulasi* "
    "Harusny dengan penjualan unit saat ini dan pencicilan pembayaran pun mampu menutup produksi saat ini"
    show mc happy at left_pos
    main "dan berikut pak seperti ini untuk proyeksi kedepannya dengan unit baru"
    hide mc normal
    "*menampilkan sheet proyeksi* "
    show staff
    staff " baiklah akan saya sampaikan dulu ke bagian procurement ya.... (pembelian)"
    hide staff

    "Tak lama pihak procurement pun menyetujui pembelian mesin produksi yang baru. "
    "Dan dari keputusan yang kamu berikan ke staff produksi, hal tersebut merupakan hal yang tepat. Karena dari adanya unit produksi yang baru, jumlah produksi pun meningkat begitupun dari kualitas yang dihasilkan juga. Dan semenjak adanya unit baru menunjukan profit yang terus meningkat. "

    return
