package day81.kasus.kemarin.tapi.pake.getter.setter;
import java.util.Scanner;
public class semen {
    private int semen;
    private int jumlah;
    private int potongan;
    private int total;   
    Scanner input = new Scanner(System.in);

    public int getsemen() {
        return semen;
    }

    public void setsemen(int semen) {
        this.semen = semen;
    }

    public int getJumlah() {
        return jumlah;
    }

    public void setJumlah() {
        System.out.print("masukkan jumlah pembelian : ");
        this.jumlah = input.nextInt();
    }

    public int getPotongan() {
        return potongan;
    }

    public void setPotongan(int potongan) {
        this.potongan = potongan;
    }

    public int getTotal() {
        return total;
    }
    public void setTotal(int total) {
        this.total = total;
    }
    
}
