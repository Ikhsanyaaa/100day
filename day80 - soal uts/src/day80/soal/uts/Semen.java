package day80.soal.uts;
public class Semen {
    int semen = 500000;
    int potongan;
    int total;
    public void Semen(int jumlah){
        if (jumlah >= 150 && jumlah <300){
            potongan = jumlah * semen * 3 / 100;
            total = jumlah * semen - potongan;
            System.out.println("anda mendapatkan diskon 3%");
            System.out.println("harga yang anda harus bayar adalah : Rp."+total);}
        else if (jumlah >= 300){
            potongan = jumlah * semen * 7 / 100;
            total = jumlah * semen - potongan;
            System.out.println("anda mendapatkan diskon 7%");
            System.out.println("harga yang anda harus bayar adalah : Rp."+total);}
        else{
            total = jumlah * semen;
            System.out.println("anda tidak mendapatkan diskon");
            System.out.println("harga yang anda harus bayar adalah : Rp."+total);}
    }
}
