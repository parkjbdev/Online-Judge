import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double w = Double.parseDouble(br.readLine());
        double h = Double.parseDouble(br.readLine());

        double bmi = w / (h * h);
        if (bmi < 18.5) {
            System.out.println("Underweight");
        } else if (bmi >= 18.5 && bmi <= 25) {
            System.out.println("Normal weight");
        } else {
            System.out.println("Overweight");
        }
    }
}
