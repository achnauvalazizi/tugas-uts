class _tinggi():
    def _init_(self, nama, tempat_lahir, tanggal_lahir, jenis_kelamin, tinggi_badan,):
        self.nama = nama
        self.tempat_lahir = tempat_lahir
        self.tanggal_lahir = tanggal_lahir
        self.jenis_kelamin = jenis_kelamin
        self.tinggi_badan = tinggi_badan
        
    def _set (self, nama, tempat_lahir, tanggal_lahir, jenis_kelamin, tinggi_badan,):
        self.nama = nama
        self.tempat_lahir = tempat_lahir
        self.tanggal_lahir = tanggal_lahir
        self.jenis_kelamin = jenis_kelamin
        self.tinggi_badan = tinggi_badan

    def _get (self):
        print('Nama lengkap   : ' + self.nama)
        print('TTL      : ' + self.tempat_lahir + ', ' +  self.tanggal_lahir)
        if self.jenis_kelamin in ['L', 'l']:
            jenis_kelamin = 'Laki-Laki'
        else:
            jenis_kelamin = 'Perempuan'
        print('jenis_kelamin      :' + jenis_kelamin)

        if self.tinggi_badan >190:
            print('tinggi badan tidak normal')
        else:
            if self.tinggi_badan >190:
                print('tinggi badan tidak normal')
            else:
                if self.tinggi_badan <190:
                    print('tinggi badan tida normal')

print('=====================================')
print('     PROGRAM CEK TINGGI BADAN      ')
print('=====================================')

nama      = input('Nama lengkap        :')
tempat_lahir = input('Tempat lahir        :')
tanggal_lahir  = input('Tanggal lahir       :')
jenis_kelamin     = input('jenis kelamin L/P          :')
tinggi_badan = float(input('masukkan tinggi badan :'))

print('======================================')

proses = _tinggi(nama,tempat_lahir,tanggal_lahir,jenis_kelamin,tinggi_badan)
print (proses._get())