package belajarclass2;
import java.util.Scanner;

class Kalkulator {
    int bil1;
    int bil2;
    int hasil;
    
    public void penjumlahan(){
        hasil = bil1 + bil2;
        System.out.println(hasil);}
}

public class BelajarClass2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Kalkulator tambah = new Kalkulator();
        System.out.println("masukkan bilangan");
        tambah.bil1 = input.nextInt();
        System.out.println("masukkan bilangan");
        tambah.bil2 = input.nextInt();
        tambah.penjumlahan();
    }
    
}
