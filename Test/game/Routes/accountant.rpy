
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

randP "Apabila Anda mencatat menjadi 8 unit nantinya akan saya transfer uang sebesar 10Juta Rupiah."

while True:
    menu:
        "Catat 8 unit":
            jump badAccountant
        "Catat 10 unit": 
            jump halfAccountant

label badAccountant:
main "baik pak, untuk pencatatannya sudah saya tulis sebesar pembelian 8 unit."

randP "oke untuk Transfer uang sebesar 10 Juta di esok hari, Terima kasih.  " 
         #*Telpon ditutup* 
scene bg_sky
"Hingga pada hari esok ternyata benar, ada Transfer yang masuk ke akun [main]"

scene bg office 
main "wih transferannya sudah masuk dong. ."
main "Enaknya dipake buat beli apa ya???  "    
bos "Lho kamu dapet Transferan? "
main "hehehe iya, soalnya kemarin baru aja selesaiin tugas khusus soalnya.  "
bos "Lho tugas khusus?"

"[main], tidak mengetahui kalau posisinya dalam bahaya. Karena pada akhir periode produksi, perusahaan melakukan opname yang dilakukan oleh auditor. Setelah  auditor menganalisa pembelian yang telah dilakukan berdasarkan pencatatan akuntan, diketahui ternyata ada salah satu karyawan yang telah menggelapkan dana perusahaan untuk membeli Uphone sebanyak 10 unit, namun tercatat hanya 8 unit. " 
"yang ternyata pembelian tersebut tercatat dalam transaksi pembelian perusahaan dan menggunakan budget perusahaan. " 
"Untuk selanjutnya karyawan yang menggelapkan dana perusahaan ABC dipecat secara tidak hormat, dan kamu sebagai akuntan yang terlibat dalam fraud dengan cara menerima suap untuk menutupi penggelapan dana juga ikut dipecat dan dipidanakan "
return


    

label halfAccountant:
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

while True:
    menu:
        "Terima Penawaran":
            jump finbadAccountant
        "Tolak Penawaran": 
            jump fingoodAccountant

label finbadAccountant:
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


label fingoodAccountant:

scene bg office
main "Tolak ah, ngapain ambil double job kalau bisa berkarir lebih baik disini..."

"Dari keputusan yang kamu ambil, kinerja perusahaan yang saat ini kamu tempati (PT. NBJ) memiliki kualitas yang sangat baik dari posisi general accountant yang kamu tempati,"
"hal itu terbukti dari jarangnya fraud yang terjadi, hingga kualitas laporan yang dibuat oleh team accounting menjadi sangat baik"

"Dan 2 bulan dari naiknya kamu menjadi general accountant. Pimpinan perusahaan setuju untuk menaikan posisi kamu menjadi direktur utama dari PT. NBJ"




return 






