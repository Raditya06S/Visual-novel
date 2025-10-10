label tax:

    #menampilkan gambar waktu isi lamaran
main "Oke lamaran udah dikirim, sekarang tinggal tunggu kabar dari HRD aja."
"*time skip 1 minggu*"

main "Lho Email dari siapa ini? *Baca email* Oh, syukurlah aku masuk tahap interview "

"*Tertulis di email akan ada interview* "

"Hari interview pun tiba"
"*Scene Interview*"

hrd "berdasarkan hasil screening data yang Anda berikan, interview dan penilaian internal kami, "
hrd "Selamat [main],anda diterima di perusahaan kami, sebagai [route]"
hrd "Berikut jobdesk *Menampilkan selembaran jobdesk* yang nantinya akan dikerjakan selama Anda menjadi [route]"
hrd " Apakah ada yang ingin ditanyakan?"
hrd "Kalau tidak ada maka Anda bisa bekerja mulai hari senin di minggu depan, Terima kasih atas kerja samanya."

"Pada hari pertama kamu masuk, kamu ditugaskan untuk mengurus perusahaan XBJ yang bergerak dibidang manufaktur. PT XBJ sendiri pun merupakan induk perusahaan NBJ yang saat ini sedang menaungi kamu."
"Di PT XBJ pun membutuhkan seorang posisi Taxation untuk mengurus sistematika perpajakan dari penghasilan operasional perusahaan. "

main "akhirnya bisa ngerasain kerja di perusahaan induk."
main "oh ya mana sekarang bulan maret lagi......., pasti gk lama lagi ada kerjaan terkait pelaporan pajak perusahaan."
"*Tidak lama ada atasan kamu yang memiliki posisi sebagai manager keuangan di perusahaan datang menghampiri kamu* "

managerKeu "Halo [main], kamu pasti baru ditugaskan disini ya? "
main " hehehe iya bu betul"
managerKeu "Yang semangat yah, soalnya sebentar lagi sudah masuk ke masa pelaporan pajak, jadi harus yang rajin yahhh"
main "Oke siap buu"

"*Setelah ibu Manager tersebut pergi, kamu terus melakukan perkerjaan yang diberikan oleh atasan kamu, yaitu untuk menyiapkan pelaporan pendapatan perusahaan kedalam SPT* "

main "Wih kalo selesai dihitung ternyata pendapatan sebelum tax yang ada di perusahaan ini besar juga ya, sampai 50 Miliar lohhhh. "
"*Tak lama kemudian manager datang kembali* "
managerKeu "Kaget ya liat pendapatan perusahaan ditahun ini?"
main " Iya bu hehehe "
managerKeu "iya syukurlah di tahun ini penjualan produk kita selalu hampir menghabiskan stok setiap bulannya, jadinya pendapatan kita meningkat secara drastis."
main " Lho bagus dong kalo kayak gitu bu...."
managerKeu "Kata siapa bagus? Kalau pendapatan kita tinggi, otomatis pajak yang harus dibayarkan juga tinggi......"
managerKeu "nah berhubung sebentar lagi kan pelaporan SPT, kira-kira kamu bisa ngecatat pendapatan perusahaan kita lebih kecil dari sebenarnya gk nih? Kalo bisa saya ada bonus buat kamu berhubungan pendapatan kita sedang tinggi nih. "
main "Duh.... gimana nih ya....."

while True:
    menu:
        "Kurangi pencatatan":
            jump badTaxation
        "Catat Sesuai Pendapatan": 
            jump goodTaxation



label badTaxation:
    main "siap bu, di pelaporan sudah saya catat dengan pendapatan yang sudah dikurangi."
    managerKeu "sippp, Terima kasih ya"

    "Tanpa yang disadari, hal yang kamu ambil merupakan keputusan yang sangat berbahaya, karena dengan perubahan pencatatan yang kamu lakukan itu menyebabkan perusahaan langsung diaudit oleh pemerintah. "

    "Dari temuan pemerintah ternyata terdapat perbedaan pencatatan, dan langsung dikategorikan sebagai fraud"

    "Maka dari itu PT XBJ langsung didenda dan dipidanakan berdasarkan peraturan perpajakan yang berlaku, setelah kejadian tersebut kamu dikeluarkan dari perusahaan dan diblacklist oleh perusahaan lainnya akibat dari tindakan yang diambil. "

    return


label goodTaxation:
    main "mohon maaf bu, untuk pencatatannya harus disesuaikan dengan apa yang diterima"
    main "karena apabila pencatatan dikurangi, otomatis nanti DJP akan langsung menyadari dan kita bisa dipidanakan. "
    managerKeu " ooooo seperti itu....."

    "Saat ini Barulah diketahui jika manager yang menaungi PT XBJ merupakan karyawan baru yang dipindahkan dari tim produksi* "

    main " Tidak masalah bu meskipun nanti nominalnya besar, kita bisa memanfaatkan kredit pajak yang ada di Indonesia. "

    "Dari keputusan yang kamu ambil, meskipun terlihat pendapatannya besar yang mengakibatkan pembayarannya besar tapi keputusan yang kamu ambil sudah betul dikarenakan perusahaan juga bisa mengkreditkan pajak yang dibayar."
    "Oleh karena itu, dari performa kamu yang  jeli dalam kasus perpajakan di PT XBJ, maka kamu dipromosikan sebagai Head Staff Taxation. "
