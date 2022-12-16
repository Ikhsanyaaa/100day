import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner masukkan = new Scanner(System.in);
        BangunDatar hasil = new BangunDatar();
        hasil.persegi(sisi);
    }
}

class BangunDatar {
    public void persegi(int sisi) {
        System.out.println("masukkan panjang sisi : ");
        sisi = masukkan.nextInt();
        int luas = sisi * sisi;
        System.out.println("luas = " + luas);
    }
}