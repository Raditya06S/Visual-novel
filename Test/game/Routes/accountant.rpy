label accountant:

   #popup image mengisi lamaran
scene bg 3
        
main "Oke lamaran udah dikirim, sekarang tinggal tunggu kabar dari HRD aja."


scene bg_sky with dissolve
"satu minggu kemudian"    

scene bg 3
main "Lho Email dari siapa ini? *Baca email* Oh, syukurlah aku masuk tahap interview "
#popup email pernyataan akan di interview

image lamaran kerja = im.FactorScale("lamaran kerja.png", 0.5, 0.5)
transform posisi_resume:
    xalign 0.5
    yalign 0.2
window hide
show lamaran kerja at posisi_resume 
pause #2
hide lamaran_kerja onlayer screens with dissolve
window show 

"Hari Interview pun tiba"
        
scene bg office

show eileen senang       
HRD "berdasarkan hasil screening data yang Anda berikan, interview dan penilaian internal kami,"

HRD "selamat [main] anda diterima di perusahaan kami, sebagai [job] "

HRD "Berikut jobdesk *popup jobdesk* yang nantinya akan dikerjakan selama Anda menjadi [job] ."
        
HRD "Apakah ada yang ingin ditanyakan?"
        
HRD "Kalau tidak ada maka Anda bisa bekerja mulai hari senin di minggu depan, Terima kasih atas kerja samanya"

scene bg_sky 
scene bg office
"Pada hari pertama kerja, [main] menerima pekerjaaan dari klien yang berasal dari perusahaan ABC yang bergerak di industri manufaktur. "
"jobdesk utama anda adalah mencatat transaksi pembelian yang dilakukan perusahaan klien dari perusahaan rekanan klien vendor."

main "Duh pencatatannya banyak banget ya."

main "Pembelian bahan baku sebanyak 500 pack dengan nilai Rp100.000 per packnya." 
"*scene input transaksi* "

main "Lho, kok ada pembelian Uphone yang harganya Rp18.000.000 per 1pcsnya dengan jumlah pembelian 10 unit. Untuk apa ya kira kira? "

     #*tak selang lama ada telepon masuk* 

randP " Selamat pagi, saya *sensor nama* salah satu pekerja di bagian purchasing dari perusahaan ABC"

main "Baik pak, ada yang bisa saya bantu?"

randP "Bisa kah Anda mencatat pembelian barang X yang ada di transaksi perusahaan menjadi 8 unit saja? "

randP "Apabila Anda mencatat menjadi 8 unit maka 2 unit yang tidak tercatat akan menjadi milik Anda."

menu:
    "Catat 8 unit":
        jump bad1
    "Catat 10 unit": 
        jump half

label bad1:
    main "baik pak, untuk pencatatannya sudah saya tulis sebesar pembelian 8 unit."

    randP "oke untuk 2 unitnya akan dikirimkan di esok hari, terima kasih. " 
         #*Telpon ditutup* 
    scene bg_sky
    "Pada esok hari ternyata benar, ada paket yang masuk ke kantor dengan atas nama [main]"

    scene bg office 
    main "Oh paket atas nama saya."
        #*buka paket isi Uphone
    main "Wihhh mantap paket Uphone kemarin "    
    bos "Lho Uphone versi terbaru? Kamu baru beli? "
    main "hehehe, iya baru beli kemarin. "

    "[main], tidak mengetahui kalau posisinya dalam bahaya. Karena pada akhir periode produksi, perusahaan melakukan opname yang dilakukan oleh auditor."

    "Setelah  auditor menganalisa pembelian yang telah dilakukan berdasarkan pencatatan akuntan, diketahui ternyata ada salah satu karyawan yang telah menggelapkan dana perusahaan untuk membeli Uphone sebanyak 10 unit, namun tercatat hanya 8 unit.  "

    "Pembelian tersebut tercatat dalam transaksi pembelian perusahaan dan menggunakan budget perusahaan."

    "Untuk selanjutnya karyawan yang menggelapkan dana perusahaan ABC dipecat secara tidak hormat, dan kamu sebagai akuntan yang terlibat dalam fraud dengan cara menerima barang hasil penggelapan dana juga ikut dipecat dan dipidanakan "


    

label half:
    main "Mohon maaf pak, apabila disini tercatat pembeliannya sejumlah 10 unit saya akan tetap catat pembelian sesuai transaksi. Terima kasih "

 # *Menutup telepon* 

    "Saat sudah selesai mencatat keseluruhan transaksi, pencatatannya diberikan ke general accountant yang ada kantor maupun kantor klien "
    "Pada waktu akhir periode produksi, perusahaan melakukan opname yang dilakukan oleh auditor. Setelah  auditor menganalisa pembelian yang telah dilakukan berdasarkan pencatatan akuntan, diketahui ternyata ada salah satu karyawan yang telah menggelapkan dana perusahaan untuk membeli Uphone sebanyak 10 unit.  "
    "yang ternyata pembelian tersebut tercatat dalam transaksi pembelian perusahaan dan menggunakan budget perusahaan."

scene bg_sky
"satu bulan kemudian"

scene bg office
"Setelah kejadian yang dialami oleh perusahaan ABC, [main] memiliki performa yang baik dan tidak ada permasalahan selama bekerja, pimpinan perusahaan memutuskan untuk menaikan jabatan [main] menjadi general accountant. "

#Ppopup email dari perusahaann*

main "Hore! akhirnya naik ke general accountant..! *berseru kegirangan* "

#*Selang beberapa waktu mendapat email lain* 

main "Eh., email apa ini?"
#*Membuka email tawaran sebagai kepala kantor PT. ABC*
main "Hmm.., tawaran yang menarik *sembari mencari informasi perusahaan tersebut*" 

main"Ambil atau engga ya tawaran menarik ini?"


menu:
    "Terima Penawaran":
        jump finbad
    "Tolak Penawaran": 
        jump fingood

label finbad:
    main "Boleh lah aku coba, toh.., masih muda butuh pengalaman banyak *percaya diri meningkat*"

    scene bg_sky
    "Beberapa minggu kemudian"

    scene office
    main "waduh banyak juga ya pekerjaan di PT. NBJ sampai kerjaanku di PT. ABC ga kepegang"

    rekan "*tidak sengaja mendengar*: Apa kamu bekerja di dua tempat berbeda di waktu yang bersamaan??? "

    main "Eh iya hehe… "

    rekan "sebenarnya gk boleh lho jadi double agent. "

    main "hehe kan masih muda, butuh pengalaman…, kan lumayan dapet gaji double juga.. *tertawa*"

    rekan "Hmm *hanya terdiam*"

    scene bg_sky
    "beberapa hari kemudian"

    scene bg office
    main "Eh..!!, kenapa ini aku kena layoff, padahal aku ga buat kesalahan sama sekali lohh…"

    "Dari teman PT ABC yang mendengar hal tersebut, kamu dilaporkan ke owner perusahaan dan ke pimpinan PT NBJ. Yang mengakibatkan kamu saat ini dipecat dari 2 perusahaan yang tadinya ditempati. "
    
    "Sehingga saat ini kamu tidak memiliki pekerjaan lagi dikarenakan semua perusahaan menolak lamaran kamu karena tidak memiliki integritas dan loyalitas. "


label fingood:

    scene bg office
    main "Tolak ah, ngapain ambil double job kalau bisa berkarir lebih baik disini..."

    "Dari keputusan yang kamu ambil, kinerja perusahaan yang saat ini kamu tempati (PT. NBJ) memiliki kualitas yang sangat baik dari posisi general accountant yang kamu tempati,"
    "hal itu terbukti dari jarangnya fraud yang terjadi, hingga kualitas laporan yang dibuat oleh team accounting menjadi sangat baik"

    "Dan 2 bulan dari naiknya kamu menjadi general accountant. Pimpinan perusahaan setuju untuk menaikan posisi kamu menjadi direktur utama dari PT. NBJ"




return 



