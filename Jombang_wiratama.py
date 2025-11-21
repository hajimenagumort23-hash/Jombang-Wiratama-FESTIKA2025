# Pustaka Standar Python yang Diperbolehkan
import random
import sys
import time

# --- Pangkalan Data Petualangan MUTER JOMBANG (Total 35 Soal) ---
# Struktur: [Pertanyaan, [Opsi A, B, C, D], Jawaban Benar (Huruf a-d), Kategori (Tokoh, Ikon, Kuliner, Sejarah)]
# Catatan: Semua string penjelasan menggunakan Raw String (r'')
MUTTER_QUEST_DATA = [
    # KATEGORI: TOKOH & SEJARAH (10 Soal)
    {
        "pertanyaan": "Siapakah pendiri Pondok Pesantren Tebuireng dan Rais Akbar Nahdlatul Ulama (NU)?",
        "opsi": ["a. K.H. Abdul Wahid Hasyim", "b. K.H. Hasyim Asy'ari", "c. K.H. Wahab Hasbullah", "d. K.H. Bisri Syansuri"],
        "jawaban_benar": "b",
        "kategori": "Tokoh",
        "penjelasan": "K.H. Hasyim Asy'ari adalah ulama besar, Pahlawan Nasional, pendiri Ponpes Tebuireng, dan merupakan pendiri sekaligus Rais Akbar pertama organisasi Nahdlatul Ulama."
    },
    {
        "pertanyaan": "Siapakah tokoh yang terkenal sebagai pahlawan perjuangan Jombang yang memimpin Laskar Hizbullah di masa kemerdekaan?",
        "opsi": ["a. K.H. Wahab Hasbullah", "b. K.H. M. Bisri Syansuri", "c. K.H. Adlan Ali", "d. K.H. Achmad Siddiq"],
        "jawaban_benar": "a",
        "kategori": "Sejarah",
        "penjelasan": "K.H. Wahab Hasbullah (Pendiri Ponpes Tambakberas) adalah seorang ulama kharismatik dan Pahlawan Nasional yang juga dikenal sebagai tokoh pergerakan dan pemimpin Laskar Sabilillah/Hizbullah di wilayah Jombang."
    },
    {
        "pertanyaan": "Makam Pahlawan Nasional di Tebuireng yang merupakan Presiden RI ke-4 adalah...",
        "opsi": ["a. K.H. Hasyim Asy'ari", "b. K.H. Abdul Wahid Hasyim", "c. K.H. Abdurrahman Wahid", "d. K.H. Mustofa Bisri"],
        "jawaban_benar": "c",
        "kategori": "Tokoh",
        "penjelasan": "K.H. Abdurrahman Wahid, atau Gus Dur, adalah Presiden RI ke-4. Makam beliau di Tebuireng menjadi salah satu destinasi ziarah terbesar di Jawa Timur."
    },
    {
        "pertanyaan": "Monumen yang menjadi titik nol Kota Jombang dan sering disebut 'titik tengah Jombang' adalah...",
        "opsi": ["a. Tugu Adipura", "b. Monumen Ringin Contong", "c. Jembatan Ploso", "d. Tugu Selamat Datang"],
        "jawaban_benar": "b",
        "kategori": "Ikon",
        "penjelasan": "Monumen Ringin Contong adalah ikon sejarah sekaligus titik pusat kota (titik nol kilometer) Jombang. 'Ringin' berarti pohon beringin dan 'Contong' adalah saluran air, mencerminkan sejarah pertaniannya."
    },
    {
        "pertanyaan": "Peristiwa penting di Jombang pada tahun 1947 di mana tentara Belanda menyerang pusat kota disebut...",
        "opsi": ["a. Serangan Fajar Jombang", "b. Agresi Militer Belanda I", "c. Pertempuran Sepuluh Nopember", "d. Peristiwa Kedung Cangkring"],
        "jawaban_benar": "b",
        "kategori": "Sejarah",
        "penjelasan": "Jombang mengalami Agresi Militer Belanda I pada tahun 1947, di mana terjadi pertempuran sengit antara pejuang kemerdekaan (termasuk laskar santri) melawan tentara Belanda yang menduduki kota."
    },
    {
        "pertanyaan": "Siapakah Bupati Jombang yang menjabat pertama kali setelah era Reformasi (sekitar tahun 1999)?",
        "opsi": ["a. Suyanto", "b. Nyono Suharli Wihandoko", "c. Witjono", "d. Afifudin Audah"],
        "jawaban_benar": "d",
        "kategori": "Sejarah",
        "penjelasan": "Bupati Jombang pertama di era Reformasi adalah Afifudin Audah. Beliau menjabat pada periode 1999-2003."
    },
    {
        "pertanyaan": "Organisasi Islam terbesar yang memiliki kaitan erat dengan Ponpes di Jombang adalah...",
        "opsi": ["a. Muhammadiyah", "b. Nahdlatul Ulama (NU)", "c. Persis", "d. LDII"],
        "jawaban_benar": "b",
        "kategori": "Tokoh",
        "penjelasan": "Jombang adalah salah satu kota kelahiran dan pusat pengembangan Nahdlatul Ulama (NU), didirikan oleh K.H. Hasyim Asy'ari (Tebuireng) dan K.H. Wahab Hasbullah (Tambakberas)."
    },
    {
        "pertanyaan": "Nama stasiun kereta api utama yang melayani Kabupaten Jombang adalah...",
        "opsi": ["a. Stasiun Peterongan", "b. Stasiun Mojokerto", "c. Stasiun Jombang", "d. Stasiun Sembung"],
        "jawaban_benar": "c",
        "kategori": "Ikon",
        "penjelasan": "Stasiun Jombang (JG) adalah stasiun kelas I yang terletak di Jombang. Stasiun ini merupakan stasiun tersibuk dan terbesar di Kabupaten Jombang."
    },
    {
        "pertanyaan": "Siapa tokoh wanita asal Jombang yang merupakan pendiri organisasi Muslimat NU dan dikenal sebagai tokoh pergerakan perempuan?",
        "opsi": ["a. Nyai Hj. Khodijah", "b. Nyai Hj. Maemunah", "c. Nyai Hj. Machfudhoh Aly Ubaid", "d. Nyai Hj. Solichah A. Wahid"],
        "jawaban_benar": "d",
        "kategori": "Tokoh",
        "penjelasan": "Nyai Hj. Solichah A. Wahid, putri dari K.H. Abdul Wahid Hasyim, dikenal sebagai tokoh perempuan yang sangat aktif dalam pengembangan Muslimat NU."
    },
    {
        "pertanyaan": "Nama Pahlawan Nasional yang juga dikenal sebagai pendiri Ponpes Darul Ulum Jombang adalah...",
        "opsi": ["a. K.H. Tamim Romly", "b. K.H. Kholil", "c. K.H. M. Rifa'i", "d. K.H. M. As'ad Umar"],
        "jawaban_benar": "a",
        "kategori": "Tokoh",
        "penjelasan": "K.H. Tamim Romly adalah salah satu tokoh penting yang mendirikan dan memimpin Pondok Pesantren Darul Ulum, salah satu ponpes terbesar di Jombang."
    },

    # KATEGORI: GEOGRAFI & TEMPAT (10 Soal)
    {
        "pertanyaan": "Gunung yang terkenal di wilayah Jombang bagian tenggara dan sering dijadikan lokasi pendakian adalah...",
        "opsi": ["a. Gunung Semeru", "b. Gunung Arjuno", "c. Gunung Pundak", "d. Gunung Bromo"],
        "jawaban_benar": "c",
        "kategori": "Geografi",
        "penjelasan": "Gunung Pundak (1.585 mdpl) adalah salah satu gunung populer untuk pendakian di Jombang, terletak di perbatasan Jombang-Mojokerto."
    },
    {
        "pertanyaan": "Sungai besar yang mengalir membelah Kabupaten Jombang dan menjadi sumber air utama adalah...",
        "opsi": ["a. Sungai Bengawan Solo", "b. Sungai Brantas", "c. Sungai Kalimas", "d. Sungai Konto"],
        "jawaban_benar": "b",
        "kategori": "Geografi",
        "penjelasan": "Sungai Brantas adalah sungai terpanjang kedua di Jawa. Sungai ini melintasi dan membelah wilayah Kabupaten Jombang, sangat vital untuk irigasi dan kehidupan kota."
    },
    {
        "pertanyaan": "Wilayah Jombang yang dikenal sebagai pusat kerajinan tembikar (gerabah) adalah kecamatan...",
        "opsi": ["a. Ngoro", "b. Mojoagung", "c. Diwek", "d. Tembelang"],
        "jawaban_benar": "c",
        "kategori": "Kerajinan",
        "penjelasan": "Kecamatan Diwek, khususnya desa Nglundo dan sekitarnya, dikenal sebagai sentra kerajinan tembikar atau gerabah tradisional di Jombang."
    },
    {
        "pertanyaan": "Candi peninggalan era Majapahit yang terletak di Jombang dan sering dikunjungi adalah...",
        "opsi": ["a. Candi Borobudur", "b. Candi Bajang Ratu", "c. Candi Rimbi", "d. Candi Jago"],
        "jawaban_benar": "c",
        "kategori": "Sejarah",
        "penjelasan": "Candi Rimbi (atau Candi Arimbi) adalah candi peninggalan Kerajaan Majapahit yang terletak di Pulosari, Ngoro, Jombang, dipercaya sebagai makam salah satu istri Raja Hayam Wuruk."
    },
    {
        "pertanyaan": "Jombang terletak di antara dua kota besar Jawa Timur, yaitu Surabaya di timur dan ... di barat.",
        "opsi": ["a. Malang", "b. Kediri", "c. Madiun", "d. Gresik"],
        "jawaban_benar": "b",
        "kategori": "Geografi",
        "penjelasan": "Jombang secara strategis terletak di jalur utama yang menghubungkan Surabaya (timur) dan Kediri (barat)."
    },
    {
        "pertanyaan": "Terminal bus utama di Jombang yang menjadi penghubung antar kota adalah Terminal...",
        "opsi": ["a. Terminal Kertajaya", "b. Terminal Kepuhsari", "c. Terminal Tandes", "d. Terminal Ploso"],
        "jawaban_benar": "b",
        "kategori": "Ikon",
        "penjelasan": "Terminal Kepuhsari adalah terminal tipe A di Jombang yang melayani rute Antar Kota Antar Provinsi (AKAP) dan Antar Kota Dalam Provinsi (AKDP)."
    },
    {
        "pertanyaan": "Jombang dilewati oleh jalur transportasi penting yang menghubungkan Jawa Barat hingga Jawa Timur, yaitu...",
        "opsi": ["a. Jalur Pantura", "b. Jalur Lintas Selatan", "c. Jalan Tol Trans Jawa", "d. Jalur Daendels"],
        "jawaban_benar": "c",
        "kategori": "Geografi",
        "penjelasan": "Jalan Tol Trans Jawa ruas Mojokerto–Kertosono (termasuk Jombang) adalah infrastruktur vital yang mempercepat konektivitas logistik Jombang."
    },
    {
        "pertanyaan": "Nama pasar tradisional terbesar di Jombang yang menjadi pusat perdagangan adalah...",
        "opsi": ["a. Pasar Legi", "b. Pasar Kliwon", "c. Pasar Wage", "d. Pasar Pon"],
        "jawaban_benar": "a",
        "kategori": "Ikon",
        "penjelasan": "Pasar Legi adalah pasar tradisional utama di Jombang yang selalu ramai dan menjadi pusat kegiatan ekonomi rakyat."
    },
    {
        "pertanyaan": "Ikon alam Jombang yang merupakan air terjun indah dan terletak di Wonosalam adalah...",
        "opsi": ["a. Air Terjun Sedudo", "b. Air Terjun Tirtosari", "c. Air Terjun Tretes", "d. Air Terjun Grojogan Sewu"],
        "jawaban_benar": "b",
        "kategori": "Geografi",
        "penjelasan": "Air Terjun Tirtosari adalah salah satu destinasi wisata alam terpopuler di Wonosalam, Jombang, dikenal dengan keindahan alamnya yang masih alami."
    },
    {
        "pertanyaan": "Kecamatan di Jombang yang terkenal sebagai daerah pegunungan dan penghasil durian serta cengkeh adalah...",
        "opsi": ["a. Mojowarno", "b. Kertosono", "c. Wonosalam", "d. Sumobito"],
        "jawaban_benar": "c",
        "kategori": "Geografi",
        "penjelasan": "Wonosalam adalah wilayah pegunungan yang sejuk di Jombang, sangat terkenal sebagai penghasil durian kualitas unggul dan cengkeh."
    },

    # KATEGORI: KULINER & BUDAYA (10 Soal)
    {
        "pertanyaan": "Jajanan khas Jombang yang terbuat dari tepung ketan, gula merah, dan dibungkus daun pisang, sering menjadi oleh-oleh adalah...",
        "opsi": ["a. Jenang", "b. Kue Lumpur", "c. Lepet", "d. Getuk Lindri"],
        "jawaban_benar": "a",
        "kategori": "Kuliner",
        "penjelasan": "Jenang (Jenang Jombang) adalah makanan khas yang manis dan lengket, sering dibawa pulang sebagai oleh-oleh dari Jombang."
    },
    {
        "pertanyaan": "Makanan khas Jombang yang berupa nasi dengan sayur tewel (nangka muda) berbumbu pedas adalah...",
        "opsi": ["a. Nasi Pecel", "b. Nasi Campur", "c. Sego Tewel", "d. Nasi Liwet"],
        "jawaban_benar": "c",
        "kategori": "Kuliner",
        "penjelasan": "Sego Tewel, atau Nasi Tewel, adalah kuliner ikonik Jombang yang menggabungkan nasi dengan nangka muda yang dimasak pedas."
    },
    {
        "pertanyaan": "Jenis tarian tradisional yang berasal dari Jawa Timur dan sering dipentaskan di Jombang sebagai tarian pembuka atau penyambut adalah...",
        "opsi": ["a. Tari Saman", "b. Tari Topeng", "c. Tari Remo", "d. Tari Jaipong"],
        "jawaban_benar": "c",
        "kategori": "Budaya",
        "penjelasan": "Tari Remo adalah tarian khas Jawa Timur (sering ditarikan di Jombang) yang biasanya dibawakan oleh penari laki-laki dengan gerakan heroik dan kostum yang mencolok, sering menjadi tarian pembuka."
    },
    {
        "pertanyaan": "Produk olahan pangan Jombang yang terbuat dari singkong dan populer sebagai keripik adalah...",
        "opsi": ["a. Kerupuk Kulit", "b. Opak Gambir", "c. Keripik Samiler", "d. Keripik Tempe"],
        "jawaban_benar": "c",
        "kategori": "Kuliner",
        "penjelasan": "Keripik Samiler adalah keripik yang terbuat dari singkong parut, populer sebagai camilan renyah khas Jombang."
    },
    {
        "pertanyaan": "Apa moto/semboyan resmi Kabupaten Jombang?",
        "opsi": ["a. Jombang Beriman", "b. Jombang Sejahtera", "c. Jombang The Unity", "d. Jombang Bersatu"],
        "jawaban_benar": "a",
        "kategori": "Umum",
        "penjelasan": "Moto resmi Kabupaten Jombang adalah 'Jombang Beriman' (Bersih, Indah, Aman, dan Nyaman)."
    },
    {
        "pertanyaan": "Pusat oleh-oleh khas Jombang, terutama jenang dan dodol, paling banyak ditemui di sekitar daerah...",
        "opsi": ["a. Mojoagung", "b. Tembelang", "c. Jombang Kota", "d. Peterongan"],
        "jawaban_benar": "c",
        "kategori": "Kuliner",
        "penjelasan": "Meskipun Jenang diproduksi di berbagai tempat, toko-toko oleh-oleh terpusat di kawasan Jombang Kota dan jalur utama."
    },
    {
        "pertanyaan": "Sajian Gado-gado khas Jombang yang membedakannya dengan daerah lain adalah penambahan...",
        "opsi": ["a. Petis Udang", "b. Bumbu Kacang Tanpa Cabai", "c. Sambal Tumpang", "d. Kerupuk Puli"],
        "jawaban_benar": "c",
        "kategori": "Kuliner",
        "penjelasan": "Beberapa penjual Gado-gado di Jombang menyajikan dengan tambahan Sambal Tumpang (bumbu tempe busuk) yang memberikan rasa unik dan berbeda dari Gado-gado Jakarta atau Surabaya."
    },
    {
        "pertanyaan": "Jombang memiliki tradisi upacara adat unik yang dilakukan oleh petani sebagai rasa syukur hasil panen, yang disebut...",
        "opsi": ["a. Larung Sesaji", "b. Petik Laut", "c. Sedekah Bumi", "d. Bersih Desa"],
        "jawaban_benar": "c",
        "kategori": "Budaya",
        "penjelasan": "Sedekah Bumi (atau Selametan Bumi) adalah tradisi adat yang dilakukan oleh masyarakat agraris (petani) di Jombang dan Jawa pada umumnya sebagai ungkapan rasa syukur atas panen yang melimpah."
    },
    {
        "pertanyaan": "Bandara terdekat dari Jombang yang biasanya digunakan untuk akses udara adalah...",
        "opsi": ["a. Bandara Juanda (Surabaya)", "b. Bandara Abdul Rachman Saleh (Malang)", "c. Bandara Internasional Adisutjipto (Yogyakarta)", "d. Bandara Internasional Ahmad Yani (Semarang)"],
        "jawaban_benar": "a",
        "kategori": "Umum",
        "penjelasan": "Bandara Internasional Juanda di Sidoarjo/Surabaya adalah bandara utama yang paling dekat dan sering digunakan oleh warga Jombang."
    },
    {
        "pertanyaan": "Tokoh sastrawan dan penulis terkenal asal Jombang yang karyanya banyak mengangkat tema sosial adalah...",
        "opsi": ["a. Pramoedya Ananta Toer", "b. Emha Ainun Nadjib (Cak Nun)", "c. Gus Mus", "d. D Zawawi Imron"],
        "jawaban_benar": "b",
        "kategori": "Tokoh",
        "penjelasan": "Emha Ainun Nadjib (Cak Nun), budayawan dan intelektual Muslim, adalah salah satu tokoh Jombang yang karyanya sangat berpengaruh di Indonesia."
    },

    # KATEGORI: UMUM JOMBANG (5 Soal)
    {
        "pertanyaan": "Ikan yang menjadi lambang fauna Kabupaten Jombang adalah...",
        "opsi": ["a. Ikan Nila", "b. Ikan Lele", "c. Ikan Wader", "d. Ikan Bandeng"],
        "jawaban_benar": "c",
        "kategori": "Umum",
        "penjelasan": "Ikan Wader (Wader Pari) merupakan fauna khas Jombang, sering ditemukan di sungai-sungai dan sawah. Ikan ini melambangkan kesederhanaan dan kelimpahan air."
    },
    {
        "pertanyaan": "Taman kota terbesar yang menjadi paru-paru dan tempat rekreasi di pusat kota Jombang adalah...",
        "opsi": ["a. Taman Tirta Wisata", "b. Kebun Raya Jombang", "c. Kebun Binatang Jombang", "d. Alun-Alun Jombang"],
        "jawaban_benar": "d",
        "kategori": "Ikon",
        "penjelasan": "Alun-Alun Jombang adalah taman kota utama dan pusat kegiatan masyarakat, terletak di depan kantor Bupati."
    },
    {
        "pertanyaan": "Jombang dikenal dengan julukan 'Kota Santri'. Julukan ini diberikan karena Jombang merupakan tempat berdirinya organisasi Islam terbesar di Indonesia, yaitu NU, dan memiliki lebih dari...",
        "opsi": ["a. 50 Pondok Pesantren", "b. 100 Pondok Pesantren", "c. 300 Pondok Pesantren", "d. 500 Pondok Pesantren"],
        "jawaban_benar": "c",
        "kategori": "Umum",
        "penjelasan": "Jombang dikenal sebagai Kota Santri karena memiliki ratusan pondok pesantren (lebih dari 300), termasuk Tebuireng, Darul Ulum, dan Tambakberas, yang menjadi pusat pendidikan agama Islam yang berpengaruh di Indonesia."
    },
    {
        "pertanyaan": "Dalam mitologi Jawa yang diyakini di Jombang, tokoh yang sering dikaitkan dengan penunggu Gunung Pundak dan Bromo adalah...",
        "opsi": ["a. Nyi Roro Kidul", "b. Joko Tingkir", "c. Eyang Semar", "d. Raden Wijaya"],
        "jawaban_benar": "c",
        "kategori": "Budaya",
        "penjelasan": "Eyang Semar adalah tokoh pewayangan yang sangat dihormati di Jawa, sering dikaitkan dengan kekuatan spiritual dan penunggu gunung-gunung di Jawa Timur."
    },
    {
        "pertanyaan": "Selain padi, komoditas pertanian Jombang yang terkenal dan diekspor adalah...",
        "opsi": ["a. Bunga Krisan", "b. Tembakau", "c. Kopi Arabika", "d. Teh Hijau"],
        "jawaban_benar": "b",
        "kategori": "Umum",
        "penjelasan": "Jombang adalah salah satu sentra penghasil tembakau (Virginia) di Jawa Timur, yang menjadi komoditas ekspor penting."
    },
]

# --- Pengaturan Game Global ---
TOTAL_PERTANYAAN = len(MUTTER_QUEST_DATA) # Total 35 soal
SKOR_MAKSIMAL_DASAR = 100 # Skor dasar per pos
HISTORY_DETAIL = []
SALAH_MAKSIMAL = 1 # Hanya boleh salah 1 kali per pos

# --- Feedback Messages Lokal (Gaul Jatim/Jombangan) ---
FEEDBACK_BENAR = [
    "JOSS GANDHOSS! Arek Jombang tenan, rek! Lanjut Soal Berikutnya!",
    "BEEH! Benar! Ilmu Geografimu gak kaleng-kaleng. Cepat ke tantangan rahasia!",
    "HEBAT! Kuncinya ketemu! Otakmu encer koyok banyu Sumur Bandung!",
]
FEEDBACK_SALAH = [
    "WADUH, SALAH SAWAH! Ojo lali diwoco maneh penjelasane. Coba maning!",
    "KELIRU KADIT! Masih ada kesempatan, tapi jangan sampai salah lagi!",
    "AWAS! Peluangmu tipis iki. Mikir sing tenanan, Jombang menantangmu!",
]
FEEDBACK_GAGAL = [
    "GAME OVER REK! Kurang fokus nang sejarah kota dewe. Mesti balen maning!",
    "WASSALAM! Jombanganmu kurang mumpuni! Ambil buku, mari kita belajar lagi!",
]

def tampilkan_secret_ending(skor_detail):
    """
    Menampilkan narasi epik Asal-Usul Jombang (Kebo Kicak vs Surontanu)
    yang menjadi Secret Ending setelah pemain meraih skor sempurna.
    """
    print("\n" + "#" * 70)
    print("#                      !!! SECRET UNLOCKED !!!                   #")
    print("#  SKOR SEMPURNA! KAMU ADALAH JURU KUNCI RAHASIA KOTA JOMBANG!  #")
    print("#" * 70)
    print("\nNARASI ASAL-USUL JOMBANG: KEBO KICAK VS SURONTANU")
    print("------------------------------------------------------------------")
    print("Setelah berabad-abad, kamu, **KEBO KICAK**, akhirnya menyelesaikan semua tantangan ini.")
    print("Kini tiba saatnya kamu memahami peranmu dalam sejarah wilayah ini.")
    time.sleep(2)
    
    print("\n[ADEGAN 1: WABAH DAN KEKACAUAN]")
    print(r"Di masa surut Majapahit, wilayah ini dilanda kekacauan oleh **Surontanu**, seorang perampok sakti yang menanamkan teror. Ia membawa pusaka Banteng Tracak Kencono yang menyebarkan wabah mematikan. Kamu, Kebo Kicak (meskipun dikutuk berkepala kerbau karena durhaka, kini telah bertaubat dan menjadi Ksatria), diutus oleh gurumu untuk menghentikan kejahatan ini.")
    time.sleep(4)

    print("\n[ADEGAN 2: PERTARUNGAN SENGIT]")
    print(r"Kamu, Kebo Kicak, mengejar Surontanu dari Mojosongo hingga ke sebuah kolam suci di kawasan yang kini menjadi Jombang Kota. Pertarungan dahsyat tak terhindarkan. Kesaktian Surontanu memancarkan aura **Merah (Abang)** yang melambangkan kekuatan dan nafsu dunia. Sedangkan dari tubuhmu, Kebo Kicak, terpancar aura **Hijau (Ijo)**, yang melambangkan keilmuan, keimanan, dan kerakyatan.")
    time.sleep(4)
    
    print("\n[ADEGAN 3: IJO VS ABANG]")
    print("Dua kekuatan besar, Ijo dan Abang, berbenturan di titik yang sama. Pertarungan itu mencapai klimaksnya, di mana kekuatanmu, Kebo Kicak, berhasil memukul mundur Surontanu. Meskipun tidak ada yang melihat jasad kalian berdua setelah pertempuran, jejak pertarungan abadi di kolam tersebut menciptakan cahaya unik.")
    print("Dari penggabungan kata **Ijo** dan **Abang** itulah, nama **JOMBANG** lahir.")
    time.sleep(3)

    print("\n[AKHIR: KESATUAN JATI DIRI]")
    print(r"Masyarakat yang menyaksikan fenomena cahaya Merah (Abang/Bang) dan Hijau (Ijo/Jo) itu kemudian menyebut wilayah ini sebagai **JOMBANG**. Sebuah nama yang melambangkan persatuan (Manunggaling Jo lan Bang) antara kaum santri/rakyat (Ijo) dan kaum nasionalis/abangan/bangsawan (Abang).")
    print("\nKamu telah menyatukan kota ini, Kebo Kicak!")
    print("\n------------------------------------------------------------------")
    print("SELAMAT! PETUALANGANMU TELAH SELESAI. JOMBANG BERIMAN.")
    print("Tekan ENTER untuk mengakhiri program.")
    input()
    sys.exit(0) # Menghentikan program setelah Secret Ending
    
def tampilkan_header():
    """Menampilkan judul dan instruksi game."""
    print("=" * 70)
    print(" 🗺️ MUTER - JOMBANG QUEST: PETUALANGAN KOTA SANTRI 🗝️")
    print("=" * 70)
    # PERBAIKAN: Mengganti TOTAL_PERTANYAN menjadi TOTAL_PERTANYAAN
    print(f"Tugasmu: Lewati {TOTAL_PERTANYAAN} Pertanyaan Acak seputar Jombang.")
    print(f"Setiap pertanyaan hanya boleh salah {SALAH_MAKSIMAL} kali.")
    print("RAIH SKOR SEMPURNA untuk membuka SECRET ENDING!")
    print("\nNdang Dijawab, reek! Ketik a, b, c, opo d. Ojo kakean mikir!\n")
    time.sleep(1)

def tampilkan_pertanyaan(index, soal, wrong_count_current):
    """Menampilkan pertanyaan, opsi, dan mengambil input user."""
    
    print("\n" + "=" * 70)
    # PERBAIKAN: Mengganti TOTAL_PERTANYAN menjadi TOTAL_PERTANYAAN
    print(f"[{index + 1}/{TOTAL_PERTANYAAN}] KATEGORI: {soal['kategori'].upper()}")
    print(f"SALAH TERSISA: {SALAH_MAKSIMAL - wrong_count_current}")
    print("=" * 70)
    print(f"PERTANYAAN:")
    print(soal["pertanyaan"])
    print("-" * 70)
    
    # Tampilkan opsi
    for opsi in soal["opsi"]:
        print(f"    {opsi}")

    # Loop untuk memastikan input valid
    while True:
        jawaban_user = input("Jawab Ndang (a/b/c/d): ").lower().strip()
        if jawaban_user in ['a', 'b', 'c', 'd']:
            return jawaban_user
        else:
            print("[PERINGATAN] Inputmu gak jelas, Cuma oleh ngetik 'a', 'b', 'c', opo 'd'.")

def main_game_loop():
    """Fungsi utama yang menjalankan petualangan."""
    
    skor_petualangan = 0
    total_benar = 0
    
    # Acak dan ambil semua pertanyaan
    soal_untuk_kuis = random.sample(MUTTER_QUEST_DATA, TOTAL_PERTANYAAN) 
    
    print("\n*** PETUALANGAN DIMULAI! JOMBANG MENANTANGMU! ***")
    time.sleep(1)
    
    start_time_total = time.time()
    
    # Loop Utama Petualangan (Per Pertanyaan)
    for i, soal in enumerate(soal_untuk_kuis):
        
        wrong_count_lokasi = 0
        is_pos_clear = False
        
        # Loop ini memastikan pemain harus menjawab benar untuk lanjut
        while not is_pos_clear:
            
            # Ambil jawaban (mengirim wrong_count untuk display)
            jawaban_user = tampilkan_pertanyaan(i, soal, wrong_count_lokasi)
            
            # Cek jawaban
            jawaban_benar = soal["jawaban_benar"]
            is_correct = (jawaban_user == jawaban_benar)
            
            # Logika Poin dan Kontrol
            if is_correct:
                
                total_benar += 1
                skor_petualangan += SKOR_MAKSIMAL_DASAR # Tambah skor per soal
                feedback_message = random.choice(FEEDBACK_BENAR)
                print(f"\n*** {feedback_message} ***")
                print(f"POIN DIDAPAT: +{SKOR_MAKSIMAL_DASAR} | TOTAL SKOR: {skor_petualangan}")
                
                # JIKA BENAR: Tampilkan penjelasan
                print("\n------------------------- PENJELASAN ILMU -------------------------")
                print(soal['penjelasan'])
                print("-----------------------------------------------------------------")
                
                is_pos_clear = True # Lanjut ke soal berikutnya
                
            else:
                wrong_count_lokasi += 1
                
                if wrong_count_lokasi > SALAH_MAKSIMAL:
                    # GAME OVER
                    feedback_message = random.choice(FEEDBACK_GAGAL)
                    print(f"\n!!! {feedback_message} !!!")
                    print(f"Jawaban benar adalah {jawaban_benar.upper()}")
                    
                    # Tampilkan penjelasan terakhir sebelum game over (TETAP DI SINI)
                    print("\n------------------------- PENJELASAN TERAKHIR -------------------------")
                    print(soal['penjelasan'])
                    print("---------------------------------------------------------------------")
                    
                    # Tampilkan hasil akhir dengan flag kalah
                    tampilkan_hasil_akhir(skor_petualangan, total_benar, False, (time.time() - start_time_total))
                    return # Menghentikan permainan
                
                else:
                    # Salah, tapi masih ada kesempatan
                    feedback_message = random.choice(FEEDBACK_SALAH)
                    print(f"\n--- {feedback_message} ---")
                    print(f"Jawaban benar adalah {jawaban_benar.upper()}")
                    
                    # PERBAIKAN: Tampilkan penjelasan HANYA setelah salah, agar pemain bisa belajar sebelum mencoba lagi
                    print("\n------------------------- PENJELASAN ILMU -------------------------")
                    print(soal['penjelasan'])
                    print("-----------------------------------------------------------------")
                    
                    print(f"SISA KESEMPATAN SALAH: {SALAH_MAKSIMAL - wrong_count_lokasi}")
                    print("\nTekan ENTER untuk mencoba lagi...")
                    input()

    # Jika loop selesai (semua soal berhasil dilewati)
    tampilkan_hasil_akhir(skor_petualangan, total_benar, True, (time.time() - start_time_total))


def dapatkan_gelar_jombang(skor_persentase):
    """Memberikan gelar khusus Jombang berdasarkan persentase skor akhir."""
    if skor_persentase == 100:
        return "SANG PENAKLUK KOTA SANTRI (Juru Kunci Jombang)"
    elif skor_persentase >= 90:
        return "AREK JOMBANG SEJATI (Pakar Sejarah Lokal)"
    elif skor_persentase >= 75:
        return "SEDULUR JOMBANG (Mulai Kenal Kota)"
    else:
        return "PEMULA WAE (Mesti Sinau Maning)"

def tampilkan_hasil_akhir(skor, total_benar, is_menang, waktu_tempuh):
    """Menampilkan ringkasan skor dan gelar akhir."""
    
    global HISTORY_DETAIL
    
    # Hitung Persentase
    persentase = (total_benar / TOTAL_PERTANYAAN) * 100
    
    # Tentukan skor total akhir
    final_score_log = skor 
    
    # Tentukan apakah SECRET terbuka
    is_secret_unlocked = (total_benar == TOTAL_PERTANYAAN) and (final_score_log == (TOTAL_PERTANYAAN * SKOR_MAKSIMAL_DASAR))
    
    # Catat skor ini ke history
    HISTORY_DETAIL.append({
        'Skor': final_score_log,
        'Benar': total_benar,
        'Waktu': waktu_tempuh,
        'Secret': is_secret_unlocked
    })
    
    # Format waktu tempuh
    waktu_bersih = time.strftime('%H:%M:%S', time.gmtime(waktu_tempuh))

    
    print("\n" + "!" * 70)
    print(" 🏅 PETUALANGAN MUTER WES MARI! HASILMU IKI 🏆 ")
    print("!" * 70)
    
    print(f"TOTAL PERTANYAAN: {TOTAL_PERTANYAAN}")
    print(f"Jawaban BENAR: {total_benar}/{TOTAL_PERTANYAAN}")
    print(f"SKOR AKHIR: {final_score_log} Poin")
    print(f"Waktu Tempuh: {waktu_bersih}")
    
    if is_menang:
        print("\nSELAMAT! KABEH TANTANGAN WES BERHASIL DITAKLUKNO!")
    else:
        print("\nMESTI COBA MANING! Petualangan terhenti di tengah jalan.")
        
    print(f"PERSENTASE BENAR: {persentase:.0f}%")
    gelar_diperoleh = dapatkan_gelar_jombang(persentase)
        
    print(f"\n>>> GELAR OLEH-OLEHMU:")
    print(f"*** {gelar_diperoleh} ***")

    # --- KONTEN RAHASIA / ENDING ---
    if is_secret_unlocked:
        # Panggil fungsi narasi epik Kebo Kicak dan keluar
        tampilkan_secret_ending(skor_detail=None)
        # Jika tampilkan_secret_ending dipanggil, program akan keluar di sana,
        # jadi baris di bawah ini hanya dijalankan jika ada bug, tapi kita tetap perlu menyertakannya
        return 
    # --------------------------------

    # Output standar jika tidak menang sempurna
    if HISTORY_DETAIL:
        # Menghitung rekor terbaik (berdasarkan skor)
        rekor_tertinggi = max(HISTORY_DETAIL, key=lambda x: x['Skor'])
        if final_score_log >= rekor_tertinggi['Skor'] and final_score_log > 0:
             print("\nSTATUS REKOR: IKI SKOR PALING APIK SAK LAWASE SESI INI!")
        else:
             print(f"\nREKOR TERTINGGI SESI: {rekor_tertinggi['Skor']} Poin. Ayo Pecahno Rekormu!")
        
    print("=" * 70)
    print("PENGEN BALEN PETUALANGAN? Tekan ENTER. Nek wes kesel, CTRL+C wae.")
    input()


if __name__ == "__main__":
    try:
        # Loop utama agar pemain bisa kembali ke menu mode setelah game selesai
        while True:
            tampilkan_header()
            main_game_loop()
            
    except KeyboardInterrupt:
        # Menangani Ctrl+C agar keluar dengan bersih
        print("\n\nPetualangan Muter dihentikan. Sampai ketemu di Jombang, rek!")
        sys.exit(0)