label business: 
play music "kerja.mp3" loop
scene bg sky
"Pada hari pertama kamu masuk kerja, kamu langsung ditugaskan sebagai konsultan di perusahaan Jaya Makmur yang bergerak di bidang manufaktur sejak tahun 2003. PT Jaya Makmur sendiri saat ini memiliki mesin otomatis dalam proses pembuatan furnitur rumah tangga. "

scene bg office 
show mc normal at left_pos
main "selamat pagi pak, perkenalkan saya [main] dari PT NBJ, hari ini saya ditugaskan sebagai consultan"
show bos happy
bos "Halo, selamat pagiii, wah selamat datang di PT Jaya makmur. Mulai hari ini kamu ditugaskan untuk membantu bagian produksi dan procurement yaa...."
main "oke siap pak..."
show bos normal
bos "sipp...."
hide bos 
hide mc normal

scene bg sky
"*Besok Harinya*"
"Keesokan harinya, kamu bertugas sebagai konsultan di perusahaan Jaya Makmur. Kamu langsung bertugas di bagian produksi, namun fokusmu adalah memberikan masukan terhadap proses yang dilakukan, bukan terlibat langsung dalam produksinya."

scene bg admin

show mc confused at left_pos
main "Dalam sebulan PT Jaya Makmur mampu memproduksi berapa meja, pak?"
show staff normal
staff "Dalam sebulan target produksi kita itu sekitar 10.000 unit, tapi kita menaruh harga diangka 1.000.000 rupiah agar tidak terlalu mahal"
show mc happy at left_pos
main "wihhhh banyak juga ya pak...."
show staff happy
staff "iya kebetulan kita memaksimalkan kemampuan mesin produksi kita, meskipun mesin yang kita miliki tergolong tua..."
hide mc 
hide staff
"Tak lama kemudian, dari lini produksi terdengar sebuah ledakan dari jalur produksi, ternyata mesin yang biasa digunakan untuk melelehkan bijih plastik meledak dikarenakan terlalu lama digunakan."
show staff shock
staff "duh... kok bisa begini ya....."
show mc normal at left_pos
main "ada kemungkinan unitnya sudah terlalu lama digunakan pak dan tidak ada waktu untuk cooling down(istirahat)..."
show staff thinking
staff "duh.... buat sekarang gimana ya..... diperbaiki atau beli unit baru ya?"
hide mc normal
hide staff
window hide
stop music
while True:
    menu:
        "Memilih untuk diperbaiki":
            jump badBusiness
        "Memilih untuk mengganti unit": 
            jump goodBusiness


label badBusiness:
    play music "aftershock.mp3" loop
    show mc normal at left_pos
    main "Sepertinya lebih baik diperbaiki pak, karena biaya yang dikeluarkan lebih sedikit dan lebih cepat pak"
    show staff normal
    staff "oooo betul juga, nanti saya sampaikan ke pihak keuangan yah....."
    hide mc normal
    hide staff
    stop music
    if gender == "male":
        show bad mmc
    else:
        show bad fmc
    play music "badend.flac"   
    "Dari keputusan yang kamu ambil kurang tepat, karena setelah diperbaiki pun mesin yang dimiliki masih tetap rusak dan membuat produksi tidak berjalan secara optimal.  "
    "sehingga dari hal tersebut membuat perusahaan mengalami profit loss setiap bulannya. "
    stop music 
    window hide
    play music "cgbad.flac"
    pause 9.0

return


label goodBusiness:
    play music"interview.wav" loop
    show mc normal at left_pos
    main "sepertinya lebih baik diganti deh pak, dikarenakan unit yang sekarang sedang beroperasi punya usia yang sudah cukup tua"
    show staff shock
    staff "tapi... kan harganya mahal..."
    main " Tidak masalah, karena menurut kalkulasi saya"
    hide mc normal
    hide staff

    window hide
    show keterangan at center_pos
    with dissolve 
    pause 1.5  
    "Harusny dengan penjualan unit saat ini dan pencicilan pembayaran pun mampu menutup produksi saat ini"
    hide keterangan
    with dissolve
    
    show mc happy at left_pos
    main "dan berikut pak seperti ini untuk proyeksi kedepannya dengan unit baru"
    hide mc normal

    window hide
    show proyeksi at center_pos
    with dissolve 
    pause 1.5  
    hide proyeksi
    with dissolve

    show staff normal
    staff " baiklah akan saya sampaikan dulu ke bagian procurement ya.... (pembelian)"
    hide staff
    stop music 
    play music "goodend.wav"
    if gender == "male":
        show good mmc
    else:
        show good fmc

    "Tak lama kemudian, pihak procurement menyetujui pembelian mesin produksi yang baru. Keputusan yang kamu berikan kepada staf produksi pun terbukti tepat"
    "Karena dari adanya unit produksi yang baru, jumlah produksi pun meningkat begitupun dari kualitas yang dihasilkan juga. Dan semenjak adanya unit baru menunjukan profit yang terus meningkat. "
    stop music
    window hide
    play music "cggood.mp3"
    pause 5.0

    return




