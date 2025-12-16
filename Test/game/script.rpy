default job = 0
default gender = 'null'
transform left_pos:
    xalign 0.0
    yalign 1.0
    xoffset -60
    yoffset 87  

transform center_pos:
    xalign 0.5
    yalign 0.5

image splash = "Binus.png"
label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

screen job_popup(img):
    modal True
    zorder 200

    add im.Scale(img, 800, 900):   
        xalign 0.5
        yalign 0.5
        
        

    


    


label start:

    stop music fadeout 2.0

    "Selamat datang di dunia visual novel"
    "Disini anda dapat merasakan pengalaman dan mempelajari dunia kerja."
    "Sebelum kita mulai, Siapa nama anda?"

    while True:
        $ main = renpy.input("Masukkan nama:", default=main).strip()
        if not main:
            $ main = "Protagonist"
        else:
            "Namamu [main]?"
            menu:
                "Yes":
                    "Next"
                    jump gender_choice
                "No":
                    pass

label gender_choice:
    "Apa jenis kelaminmu?"
    while True:
        menu:
            "Laki-laki":
                $ gender = 'male'
                jump common
            "Perempuan":
                $ gender = 'female'
                jump common

label common:
    
    play music "prolog.wav"
    scene bg room
    show mc happy at left_pos 

    main "Akhirnya!!!"
    main "Setelah 4 tahun kuliah, aku lulus"
    hide mc happy
    "Aku [main], aku adalah mahasiswa jurusan Akuntansi yang baru saja lulus dari kampus A. Aku lulus dengan nilai yang cukup baik "
    show mc normal at left_pos
    main "Karena sekarang udah gak perlu belajar sesering pas masih mahasiswa, sekarang aku punya banyak waktu luang"
    hide mc normal
    show mc confused at left_pos
    main "Waktu luang sebanyak ini enaknya ngapain ya?, apa aku harus olahraga?, atau..."
    main "..."
    main "Males juga keluar rumah, mending scroll Tungtung aja"
    hide mc confused
    "Setelah itu aku habiskan waktuku untuk mengscroll Tungtung untuk menghabiskan waktu luang"
    show mc normal at left_pos
    main "Hm? Apaan nih?"
    hide mc normal
    "Beberapa saat kemudian aku lihat sebuah artikel yang menarik perhatian ku"
    show mc shock at left_pos

    stop music
    play sound "shock.mp3"
    main "Banyak lulusan S1 nganggur?!"
    hide mc shock
    "Menurut artikel, tertulis bahwa \"Terjadi peningkatan jumlah pengangguran belakangan ini terutama para mahasiswa lulusan S1. Hal ini disebabkan karena sedikitnya jumlah lowongan kerja yang tidak mencukupi permintaan banyak pelamar pekerja\""
    show mc normal at left_pos
    main "Kalau aku santai terus kayak gini, aku bisa berakhir jadi pengangguran"
    hide mc normal
    "Dengan cekatan aku mencari lowongan pekerjaan di LinkGan yang sesuai dengan studi ku"
    "Beberapa jam aku habiskan untuk mencari lowongan pekerjaan sampai aku melihat sebuah post dari perusahaan PT.NJB"
    "Menurut post itu mereka membuka 5 posisi yang berhubungan dengan akuntansi"
    play music "prolog.wav"
    show mc normal at left_pos
    main "Wah, pas banget ada posisi di PT.NJB yang sesuai sama prodi ku. Mending aku coba dulu daftar disini"
    hide mc normal
    show mc confused at left_pos
    main "Tapi dari 5 posisi yang ada ini mending aku ngelamar di posisi apa ya?"
    show mc normal at left_pos
    main "Sebaiknya aku hati-hati karena kelima posisi ini bisa ngasih peluang yang beda buat karir ku"
    hide mc normal
    show mc confused at left_pos
    main "Sebaiknya aku ambil yang mana ya?"
    hide mc 
    window hide
    

    while True:
        menu:
            "Akuntan":
                $ job = "Akuntan"
                jump interview

            "Auditor":
                $ job = "Auditor"
                jump interview

            "Konsultan Pajak":
                $ job = "Konsultan Pajak"
                jump interview

            "Data Analis":
                $ job = "Data Analis"
                jump interview

            "Konsultan Bisnis":
                $ job = "Konsultan Bisnis"
                jump interview
            


label interview:
    show mc normal at left_pos 
    main "Oke aku udah putusin, aku yakin ini pasti posisi yang cocok buat aku!"

    window hide
    hide mc
    
    play sound "paperSd.mp3"
    if job == "Akuntan":
        show screen job_popup("images/lamAkun.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Auditor":
        show screen job_popup("images/lamAudi.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Konsultan Pajak":
        show screen job_popup("images/lamTax.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Data Analis":
        show screen job_popup("images/lamData.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Konsultan Bisnis":
        show screen job_popup("images/lamBusi.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve

    window show
    
    show mc normal at left_pos
    main "Sebagai anak jurusan akuntansi gak mungkin aku bisa gagal disini"
    main "Sebaliknya aku yakin aku bisa naik jabatan cepat disisni"
    main "Waktunya mempersiapkan diri buat interview, aku harus pastiin buat gak gagal dalam percobaan pertama"
    hide mc normal
    scene bg sky with dissolve
    "Setelah itu aku menghabiskan waktu luang ku untuk mempersiapkan diri jika tiba waktunya untuk aku interview"
    "Walaupun ini pengalaman yang asing untuk ku aku harus bisa melalui ini"
    "Akan kupastikan aku berhasil agar usaha ku selama ini tidak terbuang sia-sia"
    stop music
    
    scene black with dissolve
    show mc normal at left_pos
    main "Oke lamaran udah dikirim, sekarang tinggal tunggu kabar dari HRD aja."
    hide mc normal
    scene bg sky with dissolve
    "satu minggu kemudian"   
    scene bg room
    play music "interview.wav"
    show mc confused at left_pos
    main "Lho Email dari siapa ini?" 
    hide mc
    window hide
    
    if job == "Akuntan":
        show screen job_popup("images/mailAkun.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Auditor":
        show screen job_popup("images/mailAudi.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Konsultan Pajak":
        show screen job_popup("images/mailTax.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Data Analis":
        show screen job_popup("images/mailData.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Konsultan Bisnis":
        show screen job_popup("images/mailBusi.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve

    window show

    show mc happy at left_pos
    main "Oh, syukurlah aku masuk tahap interview "
    hide mc
    "Saat itu aku merasa sangat senang. Tapi ini belum apa-apa, masih ada interview yang perlu aku hadapi sebelum memasuki dunia kerja"
    "Aku sudah bekerja keras sampai saat ini jadi akan kupastikan aku diterima di perusahaan ini"
    scene bg office with dissolve

    show mc happy at left_pos
    main "Selamat siang"
    hide mc happy
    "Saat aku memasuki ruangan interview terdapat seorang pria dengan penampilan rapih yang menyambutku"
    show hrd normal
    hrd "Selamat siang. Nama saya adalah Paul, saya yang akan bertanggung jawab sebagai interviewer hari ini."
    show mc happy at left_pos
    main "Selamat siang, nama saya [main] saya adalah lulusan Akuntansi dari Universitas A."
    hide mc
    "Setelah itu aku melanjutkan perkenalan diri dari riwayat pendidikan, pengalaman, keahlian, sampai pencapaian yang pernah saya capai."
    "Setelah itu pak Paul beberapa kali melemparkan pertanyan kepadaku, tapi dengan latihan dan riset yang telah lakukan dengan sebelumnya."
    "Aku berhasil melalui pertanyaan yang dilemparkan padaku dengan mudah."
    show hrd thinking
    hrd "berdasarkan hasil screening data yang Anda berikan, interview dan penilaian internal kami,"
    show hrd happy
    hrd "Selamat [main] anda diterima di perusahaan kami, sebagai [job] "
    show hrd confused
    hrd "Berikut jobdesk yang nantinya akan dikerjakan selama Anda menjadi [job] ."
    hide mc
    hide hrd
    window hide
   
    play sound "paperSd.mp3"
    if job == "Akuntan":
        show screen job_popup("images/jobAkun.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Auditor":
        show screen job_popup("images/jobAudi.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Konsultan Pajak":
        show screen job_popup("images/jobTax.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Data Analis":
        show screen job_popup("images/jobData.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve
    elif job == "Konsultan Bisnis":
        show screen job_popup("images/jobBusi.png")
        with dissolve
        with Pause(1.5)
        hide screen job_popup
        with dissolve


    window show 
    show hrd thinking
    hrd "Apakah ada yang ingin ditanyakan?"  
    show hrd normal
    hrd "Kalau tidak ada maka Anda bisa bekerja mulai hari senin di minggu depan, Terima kasih atas kerja samanya"
    hide mc normal
    stop music

    if job == "Akuntan":
        jump accountant
    elif job == "Auditor":
        jump auditor
    elif job == "Konsultan Pajak":
        jump tax
    elif job == "Data Analis":
        jump analyst
    elif job == "Konsultan Bisnis":
        jump business

    return





