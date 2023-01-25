function cowok(nama_depan, nama_belakang) {
	//properti
	this.nama_depan = nama_depan;
	this.nama_belakang = nama_belakang;

	//method
	this.nama_lengkap = function(){
		return this.nama_depan + this.nama_belakang
	}
	this.tampilkan_nama = function(){
		document.write("nama anda adalah : " + this.nama_lengkap());
	}
}

nama_depan = prompt("masukkan nama depan : ")
nama_belakang = prompt("masukkan nama belakang : ")
// alert(nama_depan + " " + nama_belakang)
var cowok1 = new cowok(nama_depan,nama_belakang);

cowok1.tampilkan_nama();