# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
default main = "Protagonist"
define mc = Character("[main]")
define HRD = Character("eileen", color="#1cb87c")
define randP = Character("Orang misterius", color="#e81010")
define bos = Character("Bos Brando", color="#d8ef0ad2")
define rekan = Character("Steve", color="#2c0aefd2")
define Kakak = Character("Kakak", color="#f802d3f5")
define staffKopi = Character("Staff Coffe Shop", color="#80130b73")
define managerKeu = Character("Manager Keuangan", color="#09bb09f5")
default job = 0

label start:

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
                    jump common
                "No":
                    pass

label common:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg 3

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    main "Akhirnya!!!"
    main "Setelah 4 tahun kuliah, aku lulus"
    "Aku [main], aku adalah mahasiswa jurusan Akuntansi yang baru saja lulus dari kampus A. Aku lulus dengan nilai yang cukup baik "
    main "Karena sekarang udah gak perlu belajar sesering pas masih mahasiswa, sekarang aku punya banyak waktu luang"
    main "Waktu luang sebanyak ini enaknya ngapain ya?, apa aku harus olahraga?, atau..."
    main "..."
    main "Males juga keluar rumah, mending scroll Tungtung aja"
    "Setelah itu aku habiskan waktuku untuk mengscroll Tungtung untuk menghabiskan waktu luang"
    main "Hm? Apaan nih?"
    "Beberapa saat kemudian aku lihat sebuah artikel yang menarik perhatian ku"
    main "Banyak lulusan S1 nganggur?!"
    "Menurut artikel, tertulis bahwa \"Terjadi peningkatan jumlah pengangguran belakangan ini terutama para mahasiswa lulusan S1. Hal ini disebabkan karena sedikitnya jumlah lowongan kerja yang tidak mencukupi permintaan banyak pelamar pekerja\""
    main "Kalau aku santai terus kayak gini, aku bisa berakhir jadi pengangguran"
    "Dengan cekatan aku mencari lowongan pekerjaan di internet yang sesuai dengan studi ku"
    "Beberapa jam aku habiskan untuk mencari lowongan pekerjaan sampai aku melihat sebuah post dari perusahaan PT.NJB"
    "Menurut post itu mereka membuka 5 posisi yang berhubungan dengan akuntansi"
    main "Wah, pas banget ada posisi di PT.NJB yang sesuai sama prodi ku. Mending aku coba dulu daftar disini"
    main "Tapi dari 5 posisi yang ada ini mending aku ngelamar di posisi apa ya?"
    main "Sebaiknya aku hati-hati karena kelima posisi ini bisa ngasih peluang yang beda buat karir ku"
    main "Sebaiknya aku ambil yang mana ya?"

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
    main "Oke aku udah putusin, aku yakin ini pasti posisi yang cocok buat aku!"
    main "Sebagai anak jurusan akuntansi gak mungkin aku bisa gagal disini"
    main "Sebaliknya aku yakin aku bisa naik jabatan cepat disisni"
    main "Waktunya mempersiapkan diri buat interview, aku harus pastiin buat gak gagal dalam percobaan pertama"

    scene bg_sky with dissolve
    "Setelah itu aku menghabiskan waktu luang ku untuk mempersiapkan diri jika tiba waktunya untuk aku interview"
    "Walaupun ini pengalaman yang asing untuk ku aku harus bisa melalui ini"
    "Akan kupastikan aku berhasil agar usaha ku selama ini tidak terbuang sia-sia"

    scene black with dissolve
    scene bg office with dissolve
    "Sudah sebulan sejak hari itu, saat ini aku berada di kantor perusahaan PT.NJB untuk interview."
    "Seminggu yang lalu aku menerima pesan bahwa saya telah terpilih untuk mengikuti interview untuk posisi akuntan"
    "Saat itu aku merasa sangat senang. Tapi ini belum apa-apa, masih ada interview yang perlu aku hadapi sebelum memasuki dunia kerja"
    "Aku sudah bekerja keras sampai saat ini jadi akan kupastikan aku diterima di perusahaan ini"
    main "Selamat siang"
    "Saat aku memasuki ruangan interview terdapat seorang pria dengan penampilan rapih yang menyambutku"
    HRD "Selamat siang. Nama saya adalah Paul, saya yang akan bertanggung jawab sebagai interviewer hari ini."
    main "Selamat siang, nama saya [main] saya adalah lulusan Akuntansi dari Universitas A."
    "Setelah itu aku melanjutkan perkenalan diri dari riwayat pendidikan, pengalaman, keahlian, sampai pencapaian yang pernah saya capai."
    "Setelah itu pak Paul beberapa kali melemparkan pertanyan kepadaku, tapi dengan latihan dan riset yang telah lakukan dengan sebelumnya."
    "Aku berhasil melalui pertanyaan yang dilemparkan padaku dengan mudah."
    HRD "Selamat anda diterima sebagai [job] di perusahaan kami"

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




