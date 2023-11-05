package com.company;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.println(toGreyCode(-16, 5));
    }
    public static String toGreyCode(int num, int length){

        String bin = sanitize(num, length);

        if (bin == "-1"){
            System.out.println("Invalid Precision!!!");
            return "Error converting to grey code, invalid number of bits..";
        }

        String output = String.valueOf(bin.charAt(0));

        for (int i = 1; i < bin.length(); i++){
            String res = (bin.charAt(i) != bin.charAt(i - 1)) ? "1" :"0";
            output += res;
        }

        return output;
    }

    public static String sanitize(int num, int precision){

        String bin = Integer.toBinaryString(num);

        double convert = Math.log10(Math.abs(num)) / Math.log10(2);

        double limit = (num < 0) ? Math.floor(convert + 2) : Math.floor(convert + 1);

        if (precision < limit){

            return  "-1";
        }

        if ( num >= 0){

            bin = "0".repeat(precision - bin.length()) + bin;

        }else{
            if (precision <= bin.length()){
                bin = bin.substring(bin.length() - precision);
            }else {
                bin = "1".repeat(precision - bin.length()) + bin;
            }
        }
        return bin;

    };
}