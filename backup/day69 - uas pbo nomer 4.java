package inunguas;
import java.util.Scanner;
class Semen {
    Scanner input = new Scanner(System.in);
    public Semen(int jumlah){
        int harga = 60000;
        int potongan;
        int total;
        if (jumlah > 100){
            potongan = (harga * jumlah) * 2/100;
            total = harga * jumlah - potongan;
            System.out.println("total pembayaran = "+total);}
        else if (jumlah >= 200) {
            potongan = (harga * jumlah) * 5/100;
            total = harga * jumlah - potongan;
            System.out.println("total pembayaran = "+total);}
        
        }   
}
public class InungUas {
    public static void main(String[] args) {
      Scanner input = new Scanner(System.in);
      System.out.print("masukkan jumlah pembelian : ");
      int jumlah = input.nextInt();
      Semen baru = new Semen(jumlah);
      
        
    }
    
}
