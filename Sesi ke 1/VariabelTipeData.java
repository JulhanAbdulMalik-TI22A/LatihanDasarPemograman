
import java.util.Scanner;
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author ASUS
 */

//PIC -> Package, Import, Class

public class VariabelTipeData {
    
    static String nama;
    static int nilai;
    static Integer sks;
    static final int biaya_sks = 50000;
    static double total_diskon;
    static double total;
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        //Inputan Nama
        System.out.print("Isikan Nama: ");
        nama = sc.nextLine();
        
        //Inputan Nilai atau Umur
        System.out.print("Berapa Umur: ");
        nilai = sc.nextInt();
        
        //Inputan SKS
        System.out.print("Jumlah SKS: ");
        sks = sc.nextInt();
        double total_biaya = sks * biaya_sks;
        
        if (total_biaya > 2000000) {
            total = total_biaya * sks;
            total_biaya = total_biaya - total_biaya * 0.2;
            total_diskon = total_biaya * 0.2;
        }
        else if (total_biaya > 1000000) {
            total_biaya = total_biaya - total_biaya * 0.1;
            total_diskon = total_biaya * 0.1;
        }
        
        System.out.println("========================");
        System.out.println("Nama anda: " + nama);
        System.out.println("Umur anda: " + nilai + " Tahun");
        
        System.out.println("Total Harga sebelum Diskon :" + total);
        System.out.println("Total Diskon : " + total_diskon);
        System.out.println("Total Harga SKS anda: " + total_biaya);
        
        
    }
}
