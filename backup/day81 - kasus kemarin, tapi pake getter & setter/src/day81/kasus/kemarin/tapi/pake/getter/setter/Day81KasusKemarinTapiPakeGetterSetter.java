package day81.kasus.kemarin.tapi.pake.getter.setter;
import java.util.Scanner;
public class Day81KasusKemarinTapiPakeGetterSetter {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        semen transaksi = new semen();
        totalHarga();
    }
    public static void totalHarga(){
        semen transaksi = new semen();
        transaksi.setsemen(500000);
        transaksi.setJumlah();
        if (transaksi.getJumlah() >= 150 && transaksi.getJumlah() <300){
            transaksi.setPotongan(transaksi.getJumlah() * transaksi.getsemen() * 3/100);
            transaksi.setTotal(transaksi.getJumlah() * transaksi.getsemen()-transaksi.getPotongan() );
            System.out.println("anda mendapatkan diskon 3%");
            System.out.println("harga yang harus anda bayar adalah : Rp."+transaksi.getTotal());}
        else if (transaksi.getJumlah() >= 300){
            transaksi.setPotongan(transaksi.getJumlah() * transaksi.getsemen() * 7/100);
            transaksi.setTotal(transaksi.getJumlah() * transaksi.getsemen()-transaksi.getPotongan() );
            System.out.println("anda mendapatkan diskon 7%");
            System.out.println("harga yang harus anda bayar adalah : Rp."+transaksi.getTotal());}
        else{
            transaksi.setTotal(transaksi.getJumlah() * transaksi.getsemen()-transaksi.getPotongan() );
            System.out.println("anda tidak mendapatkan diskon");
            System.out.println("harga yang harus anda bayar adalah : Rp."+transaksi.getTotal());}
        }
    
}
