import java.util.Scanner;
class Debit {
    Scanner input = new Scanner(System.in);
    int panjang,lebar, tinggi, volume, waktu,debit_air;
    
    public void hitung(){
        volume = panjang * lebar * tinggi;
        debit_air = volume / (waktu * 60);
        System.out.println("debit air anda adalah : "+debit_air+ " liter/detik");}
    
}
public class App {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Debit air = new Debit();
        System.out.print("masukkan panjang bak dalam cm : ");
        air.panjang = input.nextInt();
        System.out.print("masukkan lebar bak dalam cm : ");
        air.lebar = input.nextInt();
        System.out.print("masukkan tinggi bak dalam cm : ");
        air.tinggi = input.nextInt();
        air.volume = air.panjang * air.lebar * air.tinggi;
        System.out.print("berapa waktu yang dibutuhkan agar air mengisi penuh bak mandi : ");
        air.waktu = input.nextInt();
        air.hitung();
    }

    
}
