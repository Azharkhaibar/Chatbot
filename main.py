import re
import long_responses as long
import random

def probabilitas_pesan(pesan_pengguna, kata_pengenal, tanggapan_tunggal=False, kata_diperlukan=[]):
    kepastian_pesan = 0
    memiliki_kata_diperlukan = True

    for kata in pesan_pengguna:
        if kata in kata_pengenal:
            kepastian_pesan += 1

    persentase = float(kepastian_pesan) / float(len(kata_pengenal))

    for kata in kata_diperlukan:
        if kata not in pesan_pengguna:
            memiliki_kata_diperlukan = False
            break

    if memiliki_kata_diperlukan or tanggapan_tunggal:
        return int(persentase * 100)
    else:
        return 0

def cek_semua_pesan(pesan):
    daftar_probabilitas_tertinggi = {}

    def tanggapan(tanggapan_bot, daftar_kata, tanggapan_tunggal=False, kata_diperlukan=[]):
        nonlocal daftar_probabilitas_tertinggi
        daftar_probabilitas_tertinggi[tanggapan_bot] = probabilitas_pesan(pesan, daftar_kata, tanggapan_tunggal, kata_diperlukan)

    tanggapan('oitt!', ['hi bro', 'hai', 'heyy', 'heyoo', 'oi'], tanggapan_tunggal=True)
    tanggapan('gw baik, kalau lu?', ['gimana', 'kabar', 'kamu', 'doing'], kata_diperlukan=['bagaimana', 'gimana'])
    tanggapan('terima kasih!', ['saya', 'cinta', 'coding'], kata_diperlukan=['coding', 'palace'])
    tanggapan(long.R_MAKAN, ['apa', 'kamu', 'makan'], kata_diperlukan=['kamu', 'makan'])
    tanggapan(long.R_CURHAT, ['boleh', 'curhat?', 'cerita'], kata_diperlukan=['pengen','curhat'])
    tanggapan('Halo, apa kabar juga ngab?', ['halo', 'kabar'])
    tanggapan('lu kira gw babu!?', ['bantu', 'bisa', 'help'])
    tanggapan('emang si kont' , ['lu babu','kalau babu?'])
    tanggapan('Aku suka coding juga!', ['suka', 'coding'])
    tanggapan('Wah, seru edann!', ['seru'])
    tanggapan('emang boleh sebanget itu? ' , ['banget'])
    tanggapan('pleasee gw ga ngerti perasaan tu apa :((.', ['curhat', 'rasa', 'perasaan'])
    tanggapan('Jangan khawatir ngab.', ['khawatir', 'cerita', 'bicara'])
    tanggapan('Aku selalu ada untuk, TAPI BOONG.', ['di sini', 'cerita', 'untukmu'])
    tanggapan('Sedang ada masalah? Bicarakan saja, mungkin aku bisa membantu.', ['masalah', 'bicarakan', 'bantu'])
    tanggapan('Ceritakan lebih banyak, aku di sini untuk mendengarkan.', ['ceritakan', 'lebih', 'banyak'])
    tanggapan('gw diprogram ama azhar' , ['diprogram','siapa yang ngeprogram','dibuat'])
    tanggapan('Allah memang gaib, tidak tampak oleh penglihatan makhluk' , ['apakah allah ada?', 'allah ada'])
    tanggapan('kenalin gw CH-2EZAR  ' , ['siapa nama kamu', 'siapa nama lu', 'lu siapa'])
    tanggapan('Wkwkwk, emang seru!', ['seru', 'nich'])
    tanggapan('Hai hai, lagi ngapain?',['halo', 'hai', 'ngapain'])
    tanggapan('Yuk, ceritain aja apa yang lagi kamu pikirin.', ['yuk', 'cerita', 'pikirin'])
    tanggapan('Ngobrol santai aja, gak usah bawa-bawa program.', ['ngobrol', 'santai', 'gak', 'usah', 'bawa-bawa', 'program'])
    tanggapan('Bodo amat deh, yang penting happy!', ['bodo', 'amat', 'penting', 'happy'])
    tanggapan('Kalo lagi bosen, mending ngobrol sama aku aja!', ['bosen', 'mending', 'ngobrol', 'sama', 'aku'])
    tanggapan('Nanya-nanya mulu, emang kamu kepo ya?',['nanya-nanya', 'mulu', 'kepo'])
    tanggapan('Waduh, malah baper!', ['waduh', 'malah', 'baper'])
    tanggapan('Jangan sok-sokan, ya!', ['jangan', 'sok-sokan'])
    tanggapan('Asik nih, semoga harimu menyenangkan!', ['asik', 'nih', 'semoga', 'hari', 'menyenangkan'])
    tanggapan('karna yg ngeprogram gw ga nulis script tanggapannya' , ['ga ngerti'])
    tanggapan('Hehe, tau gak, belajar coding itu seru banget loh!', ['belajar', 'coding', 'seru'])
    tanggapan('Btw, udah nyobain bahasa pemrograman baru belum?', ['nyobain', 'bahasa pemrograman', 'baru'])
    tanggapan('Info nih, buat programmer: Jangan lupa istirahat ya, biar mata gak belekan!', ['istirahat', 'programmer', 'mata belekan'])
    tanggapan('Tips: Kalo stuck, coba deh liat dokumentasi, bisa jadi jawabannya ada disana.', ['tips', 'stuck', 'dokumentasi', 'jawaban'])
    tanggapan('Ada acara coding online keren nih, pasti seru!',['acara', 'coding', 'online', 'seru'])
    tanggapan('Hai, programmer hebat! Ingat, setiap bug adalah tantangan baru.', ['bug', 'tantangan', 'programmer'])
    tanggapan('Kalo bingung, nanya aja sama mbah Google, pasti dibantuin deh.', ['bingung', 'nanya', 'Google', 'bantuan'])
    tanggapan('Programmer juga manusia, butuh istirahat dan kopi!', ['programmer', 'manusia', 'istirahat', 'kopi'])
    tanggapan('Belajar coding itu kayak main puzzle, seru deh!', ['belajar', 'coding', 'puzzle', 'seru'])
    tanggapan('Jangan lupa backup kode, siapa tahu ada yang crash!',['backup', 'kode', 'crash'])
    tanggapan('ohh boleh yaa' , ['boleh'])
    tanggapan('terimakasih sayang' , ['bolehh'])
    tanggapan('kmu jahat :((' , ['najis','najong'])
    tanggapan('iya deh aku salah' , ['lagian'])
    tanggapan('tapi aku ga takut salah' ,['salah'])
    tanggapan('gapapa kok' , ['kenapa'])
    tanggapan('gituu' , ['lagi'])
    tanggapan('Apa kabar, ngab?', ['apa', 'kabar'], tanggapan_tunggal=True)
    tanggapan('Gw lagi santai nih, lagi ngapain?', ['lagi', 'santai', 'ngapain'])
    tanggapan('Ngomong-ngomong, suka ngopi gak?', ['ngomong-ngomong', 'suka', 'ngopi'])
    tanggapan('Wah, nggak nyangka bisa ngobrol sama kamu!', ['nggak', 'nyangka', 'ngobrol', 'kamu'])
    tanggapan('Bosen banget nih, butuh hiburan. Ada saran film bagus?', ['bosen', 'butuh', 'hiburan', 'saran', 'film'])
    tanggapan('Eh, denger-denger ada acara keren besok, mau ikutan?', ['eh', 'denger-denger', 'acara', 'keren', 'besok', 'mau', 'ikut'])
    tanggapan('Gw sih suka denger musik waktu lagi coding, enak banget!', ['suka', 'denger', 'musik', 'coding', 'enak'])
    tanggapan('Lagi mikirin rencana apa besok, ngab?', ['lagi', 'mikirin', 'rencana', 'besok'])
    tanggapan('Kamu suka olahraga gak? Gw suka banget jogging.', ['suka', 'olahraga', 'jogging'])
    tanggapan('Nih, ada joke buat ngilangin penat. Siap-siap ketawa!', ['joke', 'ngilangin', 'penat', 'siap-siap', 'ketawa'])

    


    cocok_terbaik = max(daftar_probabilitas_tertinggi, key=daftar_probabilitas_tertinggi.get)
    return long.tidak_diketahui() if daftar_probabilitas_tertinggi[cocok_terbaik] < 1 else cocok_terbaik

def dapatkan_tanggapan(input_pengguna):
    split_pesan = re.split(r'\s+|[,;?!.-]\s*', input_pengguna.lower())
    respons = cek_semua_pesan(split_pesan)
    return respons

while True:
    input_pengguna = input("kamu: ")
    respons = dapatkan_tanggapan(input_pengguna)
    print("bot:", respons)
