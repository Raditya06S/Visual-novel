label auditor:

scene bg sky
play music "kerja.mp3"
"Pada hari pertama kerja, [main] menerima pekerjaaan dari klien yang berasal dari perusahaan BBKN yang merupakan sebuah perusahaan startup yang bergerak di industri Perbankan." 
"Jobdesk utama kamu adalah mengecek setiap transaksi arus kas, baik arus kas masuk dan keluar yang ada di perusahaan."
scene bg office
show mc normal at left_pos
main "oke Perusahaan BBKN ya, startup keren nih baru IPO aja valuasinya udah gede banget "
show mc confused at left_pos
main "oh iya kan ada saudara aku yang kerja di BBKN bagian finance juga. Semoga laporannya oke deh. "
show mc normal at left_pos
main "okee....  kita cek laporannya...."
hide mc normal

window hide
show keuUncl at center_pos
with dissolve 
pause 1.5
hide keuUncl
with dissolve
window show

show mc confused at left_pos
main "hmm, cash flow from operating activities udah sesuai, tapi kok cash flow from financing activites ada yang aneh ya??"
hide mc 
"Tidak lama ada telepon masuk dari Kakak melalui hp"
stop music
play sound "cpRing.mp3"
window hide
pause 5.0
stop sound fadeout 1.0
window show
play sound "cpUp.wav"
pause 1.0
play music "kerja.mp3"
show kakak happy
kakak "Halo [main], kamu sekarang  sedang mengaudit perusahaan aku ya?. Kalau boleh siapa yang mengaudit, kenal kah sama rekan kerja kamu?, gimana orangnya? "
show mc happy at left_pos
main "Halo kak, kok bisa tau kalo perusahaan aku yang mengaudit perusahaan kakak? "
kakak "iya dong aku tau, soalnya BBKN udah 2 kali jadi partner eksternal audit sama perusahaan NJB"
main " Wah iya ka?, aku baru tau. Terus kalo boleh tahu ada apa ya kak kok telpon?"
show kakak normal
kakak " ini aku mau infoin, kalau kamu sadar di bagian pencatatan akun Cash flow from financing activities di perusahaan BBKN itu ada yang aneh ga?"
show mc confused at left_pos
main "Iya, kok......  tahu kak?"
kakak " Iya soalnya di perusahaan ku itu sedang mengalami masa sulit, jadi pencatatan dan pembagian Dividen kepada shareholder sebetulnya ngga sesuai."
show mc shock at left_pos
main " Aduh gimana ya kak? Terus ini mau di apain nih?"
show kakak happy
kakak "jadi kalo kamu liat di pencatatan itu nilainya lebih gede kan? Nah itu gak perlu dianggap temuan, soalnya buat memancing calon investor baru buat dapetin modal tambahan lagi...."
show mc confused at left_pos
main "hmm gimana ya...."
hide mc 
hide kakak
window hide


while True:
    menu:
        "Biarkan":
            jump badAuditor
        "Catat sebagai temuan": 
            jump halfAuditor


label badAuditor:
stop music
play music "aftershock.mp3"loop
show mc normal at left_pos
main "Oke deh kak, aku biarin saja yaa... "  
show kakak happy
kakak "okee Thankyouuu yaa"
hide mc normal
hide kakak
stop music
if gender == "male":
        show bad mmc
else:
        show bad fmc
play music "badend.flac" loop
"Pada saat akhir periode akuntansi (akhir tahun), BBKN telah memublikasikan laporannya. Namun, dikarenakan publik tidak mudah dibodohi dengan laporan yang tidak benar"
"Para investor mencabut segala macam bentuk investasi yang ada di BBKN. Sehingga kini BBKN menyatakan diri jika perusahaannya bangkrut, dan kakak-mu juga dipecat."
stop music
window hide
play music "cgbad.flac"
pause 9.0
return


label halfAuditor:
    
    show mc normal at left_pos
    main "waduh sorry kak, untuk hal ini aku gk bisa bantu, jadi aku catat apa adanya kak.."
    show kakak normal
    kakak "waduh tolong dong"
    show mc confused
    main "wah aku gk berani bantu banyak kak, soalnya ini aja pekerjaan pertama aku sebagai auditor."
    kakak " beneran gk bisa? Nanti aku beliin hp baru deh..."
    hide mc normal
    hide kakak
    window hide
    stop music


menu:
    "Terima Tawaran":
        jump finbadAuditor
    "Tolak Tawaran": 
        jump fingoodAuditor

label finbadAuditor:
    play music "afterShock.mp3"
    show mc confused at left_pos
    main "Yaudah deh aku biarin buat gk jadi temuan"
    show kakak happy
    kakak "Asiikkk, nanti HPnya aku beliin pas pulang kerja yaa. Thankyouuuu"
    hide mc 
    hide kakak
    stop music 
    play music "badend.flac"

    if gender == "male":
        show bad mmc
    else:
        show bad fmc
    "Pada saat akhir periode akuntansi (akhir tahun). Laporan sudah dipublikasikan oleh perusahaan BBKN, namun dikarenakan publik tidak mudah dibodohi dengan laporan yang tidak benar," 
    "Hal tersebut menyebabkan para investor mencabut segala macam bentuk investasi yang ada di BBKN. Sehingga kini BBKN menyatakan diri jika perusahaannya bangkrut, dan kakak-mu juga dipecat."
    "Lalu pada saat kamu menelpon kakakmu, ada salah satu rekan kerja yang mendengar percakapan selama di telepon, sehingga atasan mu itu melaporkan ke pimpinan perusahaan dan kamu pun juga dipecat akibat adanya kasus suap dari perusahaan rekanan. "
    stop music
    window hide
    play music"cgbad.flac"
    pause 9.0
    
    return


label fingoodAuditor:
    play music "interview.wav"
    show mc shock at left_pos
    main "tetep kak aku gk bisa, soalnya ini menyangkut pekerjaan aku juga, kalo aku biarin yang kenapa kenapa aku juga"
    hide mc
    show kakak normal
    kakak " oh... yaudah deh, makasih ya"
    hide kakak

    window hide
    show keuCl at center_pos
    with dissolve 
    pause 1.5  
    hide keuCl
    with dissolve
    window show
    stop music
    
    play music "goodend.wav" loop
    if gender == "male":
        show good mmc
    else:
        show good fmc

    "Pada akhirnya, temuan yang kamu dapatkan dicatat sebagai temuan. Dan dari temuan tersebut diberikan ke pimpinan manajemen perusahaan BBKN." 
    "Dan tindakan yang diambil oleh perusahaan BBKN yaitu membuat laporan baru sesuai dengan temuan yang ditemukan. Sehingga dari hal tersebut investor tetap percaya dan perusahaan BBKN tetap berjalan seperti umumnya"
    stop music
    window hide
    play music "cggood.mp3"
    pause 5.0

    return


