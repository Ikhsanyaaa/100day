package hitungkalori;
import java.util.Scanner;
public class HitungKalori {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Kalori baru = new Kalori();
        int gender;
        System.out.println("1. laki-laki");
        System.out.println("2. perempuan");
        System.out.println("pililh no gender anda : ");
        gender = input.nextInt();
        switch (gender) {
            case 1:               
                baru.hitungpria();
                break;
            case 2:
                baru.hitungwanita();
                break;
            default:
                System.out.println("masukkan pilihan dengan benar!");
                break;
        }
        
    }
    
}
