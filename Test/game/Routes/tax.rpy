label tax:
scene bg sky
"Pada hari pertama kamu masuk, kamu ditugaskan untuk mengurus perusahaan XBJ yang bergerak dibidang manufaktur. PT XBJ sendiri pun merupakan induk perusahaan NBJ yang saat ini sedang menaungi kamu."
"Di PT XBJ pun membutuhkan seorang posisi Taxation untuk mengurus sistematika perpajakan dari penghasilan operasional perusahaan. "

scene bg office
show mc happy at left_pos
main "akhirnya bisa ngerasain kerja di perusahaan induk."
main "oh ya mana sekarang bulan maret lagi......., pasti gk lama lagi ada kerjaan terkait pelaporan pajak perusahaan."
hide mc normal
"*Tidak lama ada atasan kamu yang memiliki posisi sebagai manager keuangan di perusahaan datang menghampiri kamu* "

show managerKeu
managerKeu "Halo [main], kamu pasti baru ditugaskan disini ya? "
show mc happy at left_pos
main " hehehe iya bu betul"
managerKeu "Yang semangat yah, soalnya sebentar lagi sudah masuk ke masa pelaporan pajak, jadi harus yang rajin yahhh"
main "Oke siap buu"
hide mc 
hide managerKeu

"*Setelah ibu Manager tersebut pergi, kamu terus melakukan perkerjaan yang diberikan oleh atasan kamu, yaitu untuk menyiapkan pelaporan pendapatan perusahaan kedalam SPT* "

show mc happy at left_pos
main "Wih kalo selesai dihitung ternyata pendapatan sebelum tax yang ada di perusahaan ini besar juga ya, sampai 50 Miliar lohhhh. "
hide mc 
"*Tak lama kemudian manager datang kembali* "
show managerKeu
managerKeu "Kaget ya liat pendapatan perusahaan ditahun ini?"
show mc happy at left_pos
main " Iya bu hehehe "
managerKeu "iya syukurlah di tahun ini penjualan produk kita selalu hampir menghabiskan stok setiap bulannya, jadinya pendapatan kita meningkat secara drastis."
show mc confused at left_pos
main " Lho bagus dong kalo kayak gitu bu...."
managerKeu "Kata siapa bagus? Kalau pendapatan kita tinggi, otomatis pajak yang harus dibayarkan juga tinggi......"
managerKeu "nah berhubung sebentar lagi kan pelaporan SPT, kira-kira kamu bisa ngecatat pendapatan perusahaan kita lebih kecil dari sebenarnya gk nih? Kalo bisa saya ada bonus buat kamu berhubungan pendapatan kita sedang tinggi nih. "
show mc shock at left_pos
main "Duh.... gimana nih ya....."
hide mc normal
hide managerKeu


while True:
    menu:
        "Kurangi pencatatan":
            jump badTaxation
        "Catat Sesuai Pendapatan": 
            jump goodTaxation



label badTaxation:
    show mc normal at left_pos
    main "siap bu, di pelaporan sudah saya catat dengan pendapatan yang sudah dikurangi."
    show managerKeu
    managerKeu "sippp, Terima kasih ya"
    hide mc 
    hide managerKeu

    "Tanpa yang disadari, hal yang kamu ambil merupakan keputusan yang sangat berbahaya, karena dengan perubahan pencatatan yang kamu lakukan itu menyebabkan perusahaan langsung diaudit oleh pemerintah. "
    "Dari temuan pemerintah ternyata terdapat perbedaan pencatatan, dan langsung dikategorikan sebagai fraud"
    "Maka dari itu PT XBJ langsung didenda dan dipidanakan berdasarkan peraturan perpajakan yang berlaku, setelah kejadian tersebut kamu dikeluarkan dari perusahaan dan diblacklist oleh perusahaan lainnya akibat dari tindakan yang diambil. "

    return


label goodTaxation:
    show mc normal at left_pos
    main "mohon maaf bu, untuk pencatatannya harus disesuaikan dengan apa yang diterima"
    main "karena apabila pencatatan dikurangi, otomatis nanti DJP akan langsung menyadari dan kita bisa dipidanakan. "
    show managerKeu
    managerKeu " ooooo seperti itu....."
    hide managerKeu

    "Saat ini Barulah diketahui jika manager yang menaungi PT XBJ merupakan karyawan baru yang dipindahkan dari tim produksi* "

    show mc happy at left_pos
    main " Tidak masalah bu meskipun nanti nominalnya besar, kita bisa memanfaatkan kredit pajak yang ada di Indonesia. "
    hide mc normal

    "Dari keputusan yang kamu ambil, meskipun terlihat pendapatannya besar yang mengakibatkan pembayarannya besar tapi keputusan yang kamu ambil sudah betul dikarenakan perusahaan juga bisa mengkreditkan pajak yang dibayar."
    "Oleh karena itu, dari performa kamu yang  jeli dalam kasus perpajakan di PT XBJ, maka kamu dipromosikan sebagai Head Staff Taxation. "
    return
