import csv
import random

# Komponen dasar untuk membangun kalimat - diperluas dengan bank lain
banks = ['Bank Mandiri',
         'Bank BCA',
         'Bank BNI',
        #  'Bank BTN',
         'Bank BRI',
        #  'Bank Danamon',
        #  'Bank CIMB Niaga',
        #  'Bank Permata',
        #  'Jenius BTPN',
        #  'Bank DBS'
         ]
apps = {
    'Bank Mandiri': 'Livin by Mandiri',
    'Bank BCA': 'myBCA',
    'Bank BNI': 'BNI Mobile Banking',
    # 'Bank BTN': 'BTN Mobile',
    'Bank BRI': 'BRImo',
    # 'Bank Danamon': 'D-Bank PRO',
    # 'Bank CIMB Niaga': 'OCTO Mobile',
    # 'Bank Permata': 'PermataNet Mobile',
    # 'Jenius BTPN': 'Jenius',
    # 'Bank DBS': 'digibank'
}

# --- Aspek yang Diperkaya dengan Lebih Banyak Variasi ---

aspek_positif = {
    'mobile_banking': [
        'aplikasi {app}-nya sangat intuitif dan mudah digunakan, bahkan buat pemula',
        'fitur di {app} lengkap banget, semua bisa dari hp, gak perlu ke cabang',
        'tampilan {app} modern dan user-friendly, enak dilihat',
        '{app} sangat stabil dan jarang error, bisa diandalkan',
        'login di {app} sekarang cepat pakai biometrik, praktis!',
        'QRIS di {app} responsif dan gak pernah gagal, sat set bayarnya',
        'transfer pakai {app} anti ribet, prosesnya cepat dan simpel',
        'top up e-wallet dari {app} instan masuknya',
        'fitur cardless di {app} ngebantu banget pas dompet ketinggalan',
        'notifikasi real-time di {app} selalu akurat dan tepat waktu',
        'dark mode di {app} bikin mata gak capek pas malem',
        'fitur split bill di {app} memudahkan patungan sama teman',
        'bisa atur budget dan tracking pengeluaran di {app}, sangat membantu',
        'update {app} selalu membawa fitur baru yang berguna',
        'widget di home screen untuk {app} praktis banget',
        'keamanan {app} berlapis-lapis, bikin tenang',
        'facial recognition di {app} lebih cepet dari fingerprint'
    ],
    'cs': [
        'CS {bank} sangat responsif dan membantu, masalah langsung kelar',
        'pengalaman saya dengan customer service {bank} selalu baik dan solutif',
        'masalah saya cepat teratasi berkat bantuan CS {bank} via telepon',
        'petugas di kantor cabang {bank} ramah-ramah dan informatif',
        'walaupun antre, pelayanan di teller {bank} efisien dan cepat',
        'satpam di {bank} sigap membantu nasabah yang kebingungan',
        'CS {bank} via WhatsApp responsif 24/7, sangat membantu',
        'live chat di website {bank} selalu ada yang standby',
        'priority banking {bank} layanannya premium banget',
        'CS {bank} sabar banget jelasinnya, gak bikin bingung',
        'complaint handling di {bank} profesional dan follow up terus'
    ],
    'atm': [
        'ATM {bank} mudah ditemukan di mana-mana, bahkan di kota kecil',
        'jaringan ATM {bank} sangat luas, jadi gampang tarik tunai',
        'ATM {bank} jarang kosong uangnya, selalu terisi',
        'selain tarik tunai, fitur setor tunai di ATM {bank} sangat membantu',
        'ATM {bank} bisa deposit cek, praktis untuk yang bisnis',
        'antrian di ATM {bank} biasanya cepat karena mesinnya responsif',
        'layar ATM {bank} jernih dan touchscreen-nya sensitif',
        'bisa bayar tagihan listrik dan PDAM di ATM {bank}',
        'ATM {bank} ada fitur tarik tunai tanpa kartu, canggih!'
    ],
    'biaya': [
        'biaya admin {bank} cukup terjangkau, sesuai dengan layanannya',
        'suka banget karena {bank} banyak promo transfer gratis via BI-FAST',
        'kalau transfer ke sesama {bank} gratis, jadi sering kupakai',
        'biaya admin bulanannya worth it dengan semua kemudahan yang didapat',
        'gak ada biaya top up ke e-wallet dari {bank}, hemat!',
        'promo cashback {bank} sering banget, lumayan buat tambahan',
        'tabungan {bank} gak ada minimum saldo yang memberatkan',
        'biaya transfer online {bank} lebih murah dari yang offline'
    ],
    'promo': [
        'sering dapat promo menarik dari kartu kredit {bank}, diskonnya lumayan',
        '{bank} banyak kerjasama dengan merchant, jadi banyak diskon F&B',
        'pemegang kartu debit {bank} sering dapat cashback di supermarket',
        'cicilan 0% dari {bank} ngebantu banget buat beli barang elektronik',
        'program poin reward {bank} bisa ditukar berbagai hadiah menarik',
        'weekend sale {bank} selalu ada promo hotel dan travel',
        'birthday promo dari {bank} selalu menggiurkan setiap tahun',
        'kolaborasi {bank} dengan e-commerce sering ada flash sale'
    ],
    'pembukaan_rekening': [
        'buka rekening {bank} sekarang bisa full online, gak sampai 10 menit jadi',
        'proses verifikasi buka rekening {bank} via video call cepat dan mudah',
        'gak ada setoran awal minimum yang besar untuk buka tabungan di {bank}',
        'dokumen yang dibutuhkan buka rekening {bank} simpel, cuma KTP',
        'kartu debit {bank} langsung aktif setelah rekening jadi',
        'onboarding di {bank} dikasih welcome gift yang menarik'
    ],
    'investasi': [
        'fitur investasi di {bank} mudah dipahami pemula',
        'bisa beli emas digital langsung dari aplikasi {bank}',
        'SBN dan obligasi di {bank} pilihan investasinya beragam',
        'reksadana di {bank} performanya konsisten bagus',
        'robo advisor {bank} membantu pilih portofolio yang tepat'
    ],
    'teknologi': [
        'teknologi AI di {bank} membantu deteksi fraud dengan akurat',
        'sistem keamanan {bank} menggunakan enkripsi tingkat militer',
        'integrasi dengan berbagai platform digital di {bank} seamless',
        'API {bank} untuk developer sangat well-documented',
        'inovasi fintech {bank} selalu di depan dibanding kompetitor'
    ]
}

aspek_negatif = {
    'mobile_banking': [
        'aplikasi {app} sering banget maintenance, apalagi pas tanggal gajian, bikin emosi',
        '{app} lemot banget kalau dipakai pas jam sibuk, loadingnya lama',
        'UI/UX dari {app} agak membingungkan untuk orang tua, terlalu rumit',
        '{app} sering tiba-tiba logout sendiri, harus login ulang terus',
        'notifikasi transaksi dari {app} sering telat masuk, jadi was-was',
        'susah banget mau transfer pakai {app}, muter-muter terus menunya',
        'update {app} bukannya makin bagus malah makin banyak bug',
        '{app} makan banyak memori dan baterai hp',
        'fitur face ID di {app} sering gagal recognize, ribet',
        'font di {app} terlalu kecil, susah dibaca orang tua',
        'gak bisa customize dashboard di {app}, layout-nya kaku',
        'search function di {app} kurang akurat, susah nyari fitur',
        'loading time {app} makin lama setelah update terakhir',
        '{app} crash kalau hp storage penuh, gak ada warning',
        'night mode {app} malah bikin mata pusing, kontras kurang',
        'notifikasi {app} spam banget, banyak yang gak penting'
    ],
    'cs': [
        'telepon CS {bank} antrinya lama banget, habis pulsa banyak cuma buat nunggu',
        'CS {bank} kurang solutif, masalah saya dioper-oper terus tanpa ada kejelasan',
        'antrian di kantor cabang {bank} panjangnya bukan main, bisa habis setengah hari',
        'CS di social media {bank} balasnya lama dan sering template jawabannya',
        'sulit sekali bicara dengan CS manusia, selalu diarahkan ke bot',
        'CS {bank} jam operasionalnya terbatas, gak 24 jam',
        'email complaint ke {bank} gak pernah dibalas dengan tuntas',
        'CS {bank} sering putus sambungan di tengah pembicaraan',
        'petugas {bank} kurang update soal produk terbaru',
        'follow up dari CS {bank} lemah, janji gak ditepati'
    ],
    'atm': [
        'susah banget nyari ATM {bank} di daerah saya, harus pergi jauh',
        'ATM {bank} sering offline atau rusak, pas butuh malah gak bisa dipakai',
        'sering nemu ATM {bank} yang uangnya pecahan besar semua, gak ada 50 ribu',
        'layar sentuh di ATM {bank} sering tidak responsif',
        'antrian di ATM {bank} selalu panjang, terutama weekend',
        'ruang ATM {bank} sering kotor dan kurang terawat',
        'ATM {bank} gak ada fasilitas deposit, harus ke teller',
        'receipt ATM {bank} sering habis kertas atau blur printnya',
        'keamanan area ATM {bank} kurang, sering ada orang mencurigakan'
    ],
    'biaya': [
        'biaya admin bulanan {bank} lumayan mahal ya, apalagi kalau jarang dipakai',
        'banyak biaya tersembunyi kalau pakai {bank}, tiba-tiba saldo kepotong',
        'biaya transfer ke bank lain dari {bank} mahal, beda jauh sama yang lain',
        'kena biaya notifikasi SMS padahal sudah ada notif dari aplikasi',
        'biaya kartu kredit {bank} annual fee-nya tinggi',
        'penalty kalau saldo minimum gak terpenuhi di {bank} gede banget',
        'biaya tarik tunai di ATM bank lain dari {bank} selangit',
        'charge untuk layanan priority banking {bank} gak worth it',
        'biaya administrasi invest di {bank} tinggi, potong return'
    ],
    'kasus': [
        'sempat khawatir dengan kasus skimming di {bank}, jadi takut nabung banyak',
        'keamanan data di {bank} perlu ditingkatkan lagi, masih was-was soal phising',
        'proses blokir kartu {bank} kalau hilang ribet dan butuh waktu lama',
        'pernah ada kasus double charge di kartu kredit {bank}',
        'sistem {bank} pernah down berhari-hari, gak bisa akses dana',
        'data breach di {bank} beberapa waktu lalu bikin khawatir',
        'kasus fraud yang lambat ditangani tim {bank}'
    ],
    'layanan': [
        'jam operasional cabang {bank} terbatas, sulit pas hari kerja',
        'parkir di gedung {bank} mahal dan terbatas',
        'fasilitas di kantor cabang {bank} kurang nyaman untuk tunggu',
        'nomor antrian di {bank} sering error atau loncat-loncat',
        'petugas security {bank} kadang kurang ramah ke nasabah',
        'WiFi gratis di {bank} lemot dan sering putus',
        'AC di kantor cabang {bank} kurang dingin, gerah nunggu'
    ]
}

aspek_netral = [
    'saya adalah nasabah {bank} sudah 5 tahun',
    'baru saja memindahkan rekening gaji saya ke {bank}',
    'sedang mempertimbangkan antara {bank} dan {bank2} untuk KPR',
    'menggunakan {bank} untuk keperluan bisnis dan transaksi harian',
    'rekening {bank} saya gunakan khusus untuk tabungan',
    'saya punya rekening di {bank} dan juga di {bank2}',
    'tadi pagi ke kantor cabang {bank} untuk urusan administrasi',
    'lagi proses pengajuan kredit di {bank}',
    'anak saya baru buka tabungan pelajar di {bank}',
    'mau tanya-tanya produk investasi {bank} ke CS nya',
    'kemarin dapat sms dari {bank} soal promo terbaru',
    'lagi bandingkan suku bunga deposito antara {bank} dan {bank2}',
    '{bank} buka cabang baru di deket rumah saya'
]

# --- Memperkaya Struktur Kalimat ---
kata_sambung_kontras = ['tapi', 'namun', 'sayangnya', 'di sisi lain', 'beda cerita kalau', 'padahal', 'walaupun', 'meski', 'cuma', 'akan tetapi']
pembuka_opini = ['Jujur,', 'Menurutku,', 'Kalau boleh jujur,', 'Pengalaman pribadiku sih,', 'Sejauh ini,', 'Sejak pakai,', 'Dari pengalaman,', 'Kalau menurut saya,', 'Terus terang,', 'Honestly,']
kata_penghubung = ['soalnya', 'karena', 'makanya', 'jadinya', 'alhasil', 'akhirnya', 'yang bikin', 'sampai-sampai']
intensifier = ['banget', 'sangat', 'super', 'bener-bener', 'luar biasa', 'parah', 'gila', 'ekstrem', 'total']
temporal_markers = ['kemarin', 'tadi', 'minggu lalu', 'bulan ini', 'akhir-akhir ini', 'belakangan', 'sejak kemarin', 'dari tadi pagi']

# Ekspansi emosi dan konteks situasional
konteks_situasional = [
    'pas lagi butuh dana darurat',
    'waktu mau bayar tagihan',
    'saat transfer ke orang tua',
    'ketika lagi traveling',
    'pas weekend',
    'jam makan siang',
    'tengah malam',
    'pas tanggal tua',
    'saat gajian',
    'waktu lagi busy',
    'pas system maintenance'
]

perbandingan_eksplisit = [
    'jauh lebih baik dari',
    'lebih bagus daripada',
    'masih unggul dibanding',
    'beda tipis sama',
    'unggul dibanding',
    'masih di atas',
    'lebih worth it dibanding',
]

def generate_sentence():
    """Menghasilkan satu set data (teks, dan daftar target-sentimen) dengan variasi yang lebih kaya."""
    data_points = []
    
    # Pilih 1, 2, atau 3 bank secara acak untuk dibicarakan
    num_banks = random.randint(1, 3)
    selected_banks = random.sample(banks, min(num_banks, len(banks)))
    
    template_type = random.randint(1, 20)  # Expanded template options

    # Template 1-3: Perbandingan Positif vs Negatif (2 Bank)
    if template_type <= 3 and len(selected_banks) >= 2:
        bank1, bank2 = selected_banks[0], selected_banks[1]
        aspek_cat_pos = random.choice(list(aspek_positif.keys()))
        aspek_cat_neg = random.choice(list(aspek_negatif.keys()))
        
        kalimat_pos = random.choice(aspek_positif[aspek_cat_pos]).format(bank=bank1, app=apps[bank1])
        kalimat_neg = random.choice(aspek_negatif[aspek_cat_neg]).format(bank=bank2, app=apps[bank2])
        
        konjungsi = random.choice(kata_sambung_kontras)
        intensif = random.choice(intensifier)
        
        if random.choice([True, False]):
            teks = f"{kalimat_pos.capitalize()}, {konjungsi} {kalimat_neg}."
        else:
            teks = f"{random.choice(pembuka_opini)} {kalimat_pos}, {konjungsi} {kalimat_neg} {intensif}."
            
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'positif'})
        data_points.append({'teks': teks, 'target_bank': bank2, 'sentimen': 'negatif'})

    # Template 4-5: Pujian untuk satu bank dengan konteks situasional
    elif template_type <= 5 and len(selected_banks) >= 2:
        bank1, bank2 = selected_banks[0], selected_banks[1]
        aspek_cat_pos = random.choice(list(aspek_positif.keys()))
        konteks = random.choice(konteks_situasional)
        perbandingan = random.choice(perbandingan_eksplisit)

        kalimat_pos = random.choice(aspek_positif[aspek_cat_pos]).format(bank=bank1, app=apps[bank1])
        teks = f"{random.choice(temporal_markers).capitalize()}, {konteks}, {kalimat_pos}. {bank1} {perbandingan} {bank2} sih."
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'positif'})
        data_points.append({'teks': teks, 'target_bank': bank2, 'sentimen': 'negatif'})
        
    # Template 6-7: Keluhan kontekstual dengan emosi kuat
    elif template_type <= 7 and len(selected_banks) >= 2:
        bank1, bank2 = selected_banks[0], selected_banks[1]
        aspek_cat_neg = random.choice(list(aspek_negatif.keys()))
        kalimat_neg = random.choice(aspek_negatif[aspek_cat_neg]).format(bank=bank1, app=apps[bank1])
        pembuka = random.choice(pembuka_opini)
        intensif = random.choice(intensifier)
        konteks = random.choice(konteks_situasional)
        
        teks = f"{pembuka} {konteks}, {kalimat_neg} {intensif}. Mending pindah ke {bank2} aja kayaknya."
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'negatif'})
        data_points.append({'teks': teks, 'target_bank': bank2, 'sentimen': 'positif'})

    # Template 8-9: Ulasan campuran dengan aspek ganda
    elif template_type <= 9 and len(selected_banks) >= 1:
        bank1 = selected_banks[0]
        aspek_cats = random.sample(list(aspek_positif.keys()), 2)
        aspek_cat_pos, aspek_cat_pos2 = aspek_cats[0], aspek_cats[1]
        aspek_cat_neg = random.choice(list(aspek_negatif.keys()))
        
        # Pastikan aspek negatif berbeda
        while aspek_cat_neg in aspek_cats:
            aspek_cat_neg = random.choice(list(aspek_negatif.keys()))
            
        kalimat_pos1 = random.choice(aspek_positif[aspek_cat_pos]).format(bank=bank1, app=apps[bank1])
        kalimat_pos2 = random.choice(aspek_positif[aspek_cat_pos2]).format(bank=bank1, app=apps[bank1])
        kalimat_neg = random.choice(aspek_negatif[aspek_cat_neg]).format(bank=bank1, app=apps[bank1])
        konjungsi = random.choice(kata_sambung_kontras)

        teks = f"{random.choice(pembuka_opini)} {bank1} overall bagus, {kalimat_pos1} dan {kalimat_pos2}, {konjungsi} {kalimat_neg}."
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'campuran'})

    # Template 10-11: Keluhan spesifik dengan temporal marker
    elif template_type <= 11 and len(selected_banks) >= 1:
        bank1 = selected_banks[0]
        aspek_cat_neg = random.choice(list(aspek_negatif.keys()))
        kalimat_neg = random.choice(aspek_negatif[aspek_cat_neg]).format(bank=bank1, app=apps[bank1])
        temporal = random.choice(temporal_markers)
        intensif = random.choice(intensifier)
        
        if random.choice([True, False]):
            teks = f"{temporal.capitalize()} {kalimat_neg} {intensif}. Kecewa sama {bank1}."
        else:
            teks = f"Kesel {intensif} sama {bank1}, {temporal} {kalimat_neg}."
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'negatif'})

    # Template 12-13: Pujian dengan rekomendasi
    elif template_type <= 13 and len(selected_banks) >= 1:
        bank1 = selected_banks[0]
        aspek_cat_pos = random.choice(list(aspek_positif.keys()))
        kalimat_pos = random.choice(aspek_positif[aspek_cat_pos]).format(bank=bank1, app=apps[bank1])
        intensif = random.choice(intensifier)
        
        rekomendasi = random.choice([
            f"Recommend {intensif} buat yang mau coba {bank1}",
            f"Gaskeun deh ke {bank1}",
            f"Worth it banget pilih {bank1}",
            f"{bank1} emang the best"
        ])
        
        teks = f"{kalimat_pos.capitalize()}. {rekomendasi}!"
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'positif'})
        
    # Template 14-15: Pertanyaan dengan preferensi tersirat  
    elif template_type <= 15 and len(selected_banks) >= 2:
        bank1, bank2 = selected_banks[0], selected_banks[1]
        
        pertanyaan_templates = [
            f"Guys, {bank1} atau {bank2} ya buat kredit rumah? Lagi galau nih",
            f"Minta saran dong, antara {bank1} dan {bank2} mana yang lebih worth it?",
            f"Ada yang pernah pakai {bank1} dan {bank2}? Share pengalaman dong",
            f"Lagi compare {bank1} vs {bank2}, ada masukan?"
        ]
        
        teks = random.choice(pertanyaan_templates)
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'netral'})
        data_points.append({'teks': teks, 'target_bank': bank2, 'sentimen': 'netral'})

    # Template 16-17: Testimoni dengan latar belakang
    elif template_type <= 17 and len(selected_banks) >= 1:
        bank1 = selected_banks[0]
        backgrounds = [
            "sebagai freelancer", "untuk usaha kecil", "buat anak kuliah", 
            "pensiun dari bank lama", "first time banking", "ganti dari bank konvensional"
        ]
        background = random.choice(backgrounds)
        aspek_cat = random.choice(list(aspek_positif.keys()))
        kalimat = random.choice(aspek_positif[aspek_cat]).format(bank=bank1, app=apps[bank1])
        
        teks = f"Sebagai yang {background}, {kalimat}. {bank1} cocok banget buat kebutuhan saya."
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'positif'})

    # Template 18: Perbandingan multi-aspek
    elif template_type == 18 and len(selected_banks) >= 2:
        bank1, bank2 = selected_banks[0], selected_banks[1]
        aspek1 = random.choice(list(aspek_positif.keys()))
        aspek2 = random.choice(list(aspek_positif.keys()))
        
        kalimat1 = random.choice(aspek_positif[aspek1]).format(bank=bank1, app=apps[bank1])
        kalimat2 = random.choice(aspek_positif[aspek2]).format(bank=bank2, app=apps[bank2])
        
        teks = f"Kalau dari segi {aspek1}, {kalimat1}. Tapi kalau {aspek2}, {kalimat2}. Susah milihnya."
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'positif'})
        data_points.append({'teks': teks, 'target_bank': bank2, 'sentimen': 'positif'})

    # Template 19: Update status/pengalaman terbaru
    elif template_type == 19 and len(selected_banks) >= 1:
        bank1 = selected_banks[0]  
        update_templates = [
            f"Update: akhirnya pindah ke {bank1}, so far so good",
            f"1 bulan pakai {bank1}, impressi pertama positif",
            f"Baru seminggu di {bank1}, masih adaptasi tapi promising"
        ]
        teks = random.choice(update_templates)
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'positif'})

    # Template 20: Pernyataan Netral dengan konteks
    else:
        if not selected_banks: 
            selected_banks.append(random.choice(banks))
        
        bank1 = selected_banks[0]
        bank2 = random.choice([b for b in banks if b != bank1])
        kalimat_netral = random.choice(aspek_netral).format(bank=bank1, bank2=bank2)
        konteks_tambahan = random.choice([
            "", 
            f" {random.choice(temporal_markers)}", 
            f", sambil {random.choice(['ngurus dokumen', 'tanya-tanya produk', 'ngecek saldo'])}"
        ])
        
        teks = f"{kalimat_netral}{konteks_tambahan}."
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'netral'})
        
        if '{bank2}' in kalimat_netral and len(selected_banks) >= 2:
            data_points.append({'teks': teks, 'target_bank': selected_banks[1], 'sentimen': 'netral'})
    
    # Safety net
    if not data_points:
        bank1 = random.choice(banks)
        teks = f"Update status rekening {bank1} tadi pagi."
        data_points.append({'teks': teks, 'target_bank': bank1, 'sentimen': 'netral'})

    return data_points


# Hasilkan data dengan distribusi sentimen yang lebih seimbang
# Hasilkan data dengan jaminan keunikan dan batasan percobaan

all_data = []
generated_combinations = set()  # Set untuk melacak kombinasi (teks, target_bank) yang unik
target_rows = 3000
max_attempts = target_rows * 5  # Batas aman untuk mencegah infinite loop
attempts = 0

print(f"Mulai menghasilkan {target_rows} data unik. Ini mungkin memakan waktu...")

while len(all_data) < target_rows and attempts < max_attempts:
    # Panggil fungsi generator Anda
    generated_points = generate_sentence()
    
    for data_point in generated_points:
        # Buat kunci unik dari kombinasi teks dan target_bank
        # Gunakan tuple karena hashable (bisa dimasukkan ke set)
        unique_key = (data_point['teks'], data_point['target_bank'])
        
        # Cek apakah kombinasi ini sudah pernah dibuat
        if unique_key not in generated_combinations:
            # Jika belum, tambahkan ke list data dan set pelacak
            generated_combinations.add(unique_key)
            all_data.append(data_point)
            
            # Jika target sudah tercapai di tengah loop, langsung keluar
            if len(all_data) >= target_rows:
                break
    
    attempts += 1
    # Memberi feedback progress agar tidak terlihat hang
    if attempts % 1000 == 0:
        print(f"Percobaan ke-{attempts}... Data terkumpul: {len(all_data)}/{target_rows}")

# --- Akhir dari loop utama ---

# Memberi peringatan jika loop berhenti karena batas percobaan
if attempts >= max_attempts:
    print("\nPERINGATAN: Proses dihentikan karena mencapai batas percobaan maksimum.")
    print(f"Generator mungkin kesulitan membuat data unik baru setelah mencapai {len(all_data)} baris.")

# Shuffle data untuk distribusi yang lebih baik saat training model
random.shuffle(all_data)

# Tulis ke file CSV
output_filename = 'bank_sentiment_dataset_unique.csv'
with open(output_filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['teks', 'target_bank', 'sentimen'])
    writer.writeheader()
    writer.writerows(all_data)

# Hitung distribusi sentimen dari data final yang unik
sentiment_counts = {'positif': 0, 'negatif': 0, 'netral': 0, 'campuran': 0}
for row in all_data:
    sentiment_counts[row['sentimen']] += 1

# Print statistik
print(f"\nDataset unik berhasil dibuat: {output_filename}")
print(f"Total baris unik yang dihasilkan: {len(all_data)}")

# Cek duplikasi sebagai bukti (hasilnya harus 0)
import pandas as pd
df = pd.DataFrame(all_data)
print(f"\nJumlah duplikasi (teks, target_bank) setelah perbaikan: {df[['teks','target_bank']].duplicated().sum()}")


print("\nDistribusi sentimen:")
if all_data: # Mencegah error jika tidak ada data sama sekali
    for sentiment, count in sentiment_counts.items():
        percentage = (count / len(all_data)) * 100
        print(f"{sentiment.capitalize()}: {count} ({percentage:.2f}%)")

print("\nContoh data:")
for i in range(min(5, len(all_data))): # Mencegah error jika data < 5
    print(all_data[i])

print("\nDataset siap digunakan untuk analisis sentimen yang lebih mendalam!")
