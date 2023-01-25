package hitungkalori;
import java.util.Scanner;
public class Kalori {
    Scanner input = new Scanner(System.in);
    double berat;
    double tinggi;
    double usia;
    int keseharian;
    double aktivitas;
    double BMR;
    double kalori;
    
    public void hitungpria(){
        System.out.print("masukkan berat badan : ");
        berat = input.nextDouble();
        System.out.print("masukkan tinggi badan : ");
        tinggi = input.nextDouble();
        System.out.print("berapa usia anda? : ");
        usia = input.nextDouble();
        System.out.print("dari skala 1-8, berapa keseharian anda : ");
        keseharian = input.nextInt();
        switch (keseharian) {
            case 1 -> aktivitas = 1.2;
            case 2 -> aktivitas = 1.3;
            case 3 -> aktivitas = 1.4;
            case 4 -> aktivitas = 1.5;
            case 5 -> aktivitas = 1.6;
            case 6 -> aktivitas = 1.7;
            case 7 -> aktivitas = 1.8;
            case 8 -> aktivitas = 1.9;
            default -> System.out.println("inputan salah!");
        }
        BMR =  66.5 + (13.75 * berat) + (5.003 * tinggi) - (6.75 * usia);
        kalori = BMR * aktivitas;
        System.out.println("kebutuhan kalori anda adalah sebanyak : "+kalori+"kkal");
    }
    public void hitungwanita(){
        System.out.print("masukkan berat badan : ");
        berat = input.nextDouble();
        System.out.print("masukkan tinggi badan : ");
        tinggi = input.nextDouble();
        System.out.print("berapa usia anda? : ");
        usia = input.nextDouble();
        System.out.print("dari skala 1-8, berapa keseharian anda : ");
        keseharian = input.nextInt();
        switch (keseharian) {
            case 1:
                aktivitas = 1.2;
                break;
            case 2:
                aktivitas = 1.3;
                break;
            case 3:
                aktivitas = 1.4;
                break;
            case 4:
                aktivitas = 1.5;
                break;
            case 5:
                aktivitas = 1.6;
                break;
            case 6:
                aktivitas = 1.7;
                break;
            case 7:
                aktivitas = 1.8;
                break;
            case 8:
                aktivitas = 1.9;
                break;
            default:
                System.out.println("inputan salah!");
                break;
        }
        BMR =  665.1 + (9.563 * berat) + (1.850 * tinggi) - (4.676 * usia);
        kalori = BMR * aktivitas;
        System.out.println("kebutuhan kalori anda adalah sebanyak : "+kalori+"kkal");
    }
    
    
    
    
}