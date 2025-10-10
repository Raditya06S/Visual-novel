label auditor:

scene bg sky

"Pada hari pertama kerja, [main] menerima pekerjaaan dari klien yang berasal dari perusahaan BBKN yang merupakan sebuah perusahaan startup yang bergerak di industri Perbankan, jobdesk utama kamu adalah mengecek setiap transaksi arus kas, baik arus kas masuk dan keluar yang ada di perusahaan."

scene bg office

main "oke Perusahaan BBKN ya, startup keren nih baru IPO aja valuasinya udah gede banget "

main "oh iya kan ada saudara aku yang kerja di BBKN bagian finance juga. Semoga laporannya oke deh. "

main " okee....  kita cek laporannya...."

"*mengecek laporan keuangan* "

main "hmm, cash flow from operating activities udah sesuai, tapi kok cash flow from financing activites ada yang aneh ya??"

"Tidak lama ada telepon masuk dari Kakak melalui hp*"

kakak "Halo [main], kamu sekarang  sedang mengaudit perusahaan aku ya?. Kalau boleh siapa yang mengaudit, kenal kah sama rekan kerja kamu?, gimana orangnya? "
main "Halo kak, kok bisa tau kalo perusahaan aku yang mengaudit perusahaan kakak? "
kakak "iya dong aku tau, soalnya BBKN udah 2 kali jadi partner eksternal audit sama perusahaan NJB"
main " Wah iya ka?, aku baru tau. Terus kalo boleh tahu ada apa ya kak kok telpon?"
kakak " ini aku mau infoin, kalau kamu sadar di bagian pencatatan akun Cash flow from financing activities di perusahaan BBKN itu ada yang aneh ga?"
main "Iya, kok......  tahu kak?"
kakak " Iya soalnya di perusahaan ku itu sedang mengalami masa sulit, jadi pencatatan dan pembagian Dividen kepada shareholder sebetulnya ngga sesuai."
main " Aduh gimana ya kak? Terus ini mau di apain nih?"
kakak "jadi kalo kamu liat di pencatatan itu nilainya lebih gede kan? Nah itu gak perlu dianggap temuan, soalnya buat memancing calon investor baru buat dapetin modal tambahan lagi...."
main "hmm gimana ya...."

while True:
    menu:
        "Biarkan":
            jump badAuditor
        "Catat sebagai temuan": 
            jump halfAuditor


label badAuditor:
main "Oke deh kak, aku biarin saja yaa... "  
kakak "okee Thankyouuu yaa"
"Pada saat akhir periode akuntansi (akhir tahun). Laporan sudah dipublikasikan oleh perusahaan BBKN, namun dikarenakan publik tidak mudah dibodohi dengan laporan yang tidak benar"
"para investor mencabut segala macam bentuk investasi yang ada di BBKN. Sehingga kini BBKN menyatakan diri jika perusahaannya bangkrut, dan kakak-mu juga dipecat."
  
return


label halfAuditor:
    main "waduh sorry kak, untuk hal ini aku gk bisa bantu, jadi aku catat apa adanya kak.."
    kakak "waduh tolong dong"
    main "wah aku gk berani bantu banyak kak, soalnya ini aja pekerjaan pertama aku sebagai auditor."
    kakak " beneran gk bisa? Nanti aku beliin hp baru deh..."


menu:
    "Terima Tawaran":
        jump finbadAuditor
    "Tolak Tawaran": 
        jump fingoodAuditor

label finbadAuditor:
    main "Yaudah deh aku biarin buat gk jadi temuan"
    kakak "Asiikkk, nanti HPnya aku beliin pas pulang kerja yaa. Thankyouuuu"
    "Pada saat akhir periode akuntansi (akhir tahun). Laporan sudah dipublikasikan oleh perusahaan BBKN, namun dikarenakan publik tidak mudah dibodohi dengan laporan yang tidak benar," 
    "maka para investor mencabut segala macam bentuk investasi yang ada di BBKN. Sehingga kini BBKN menyatakan diri jika perusahaannya bangkrut, dan kakak-mu juga dipecat."
    "Lalu pada saat kamu menelpon kakakmu, ada salah satu rekan kerja yang mendengar percakapan selama di telepon, sehingga atasan mu itu melaporkan ke pimpinan perusahaan dan kamu pun juga dipecat akibat adanya kasus suap dari perusahaan rekanan. "
    return


label fingoodAuditor:
    main "tetep kak aku gk bisa, soalnya ini menyangkut pekerjaan aku juga, kalo aku biarin yang kenapa kenapa aku juga"
    kakak " oh... yaudah deh, makasih ya"
    "Pada akhirnya, temuan yang kamu dapatkan dicatat sebagai temuan. Dan dari temuan tersebut diberikan ke pimpinan manajemen perusahaan BBKN." 
    "Dan tindakan yang diambil oleh perusahaan BBKN yaitu membuat laporan baru sesuai dengan temuan yang ditemukan. Sehingga dari hal tersebut investor tetap percaya dan perusahaan BBKN tetap berjalan seperti umumnya"

    return



