package guessnumbergame;

import java.util.Random;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        NumberGuessingGame game = new NumberGuessingGame();
        game.start();
    }
}

class NumberGuessingGame {
    private int randomNumber;
    private int attempts;

    public NumberGuessingGame() {
        Random random = new Random();
        this.randomNumber = random.nextInt(10) + 1;
        this.attempts = 0;
    }

    public void start() {
        Scanner scanner;
        scanner = new Scanner(System.in);
        System.out.println("Добро пожаловать в игру Угадай число!");
        System.out.println("Я выбрал случайное число от 1 до 10. Попробуйте угадать!");

        while (true) {
            System.out.print("Введите вашу догадку: ");
            int userGuess = scanner.nextInt();
            attempts++;

            if (userGuess < 1 || userGuess > 10) {
                System.out.println("Пожалуйста, введите число от 1 до 10.");
            } else if (userGuess < randomNumber) {
                System.out.println("Попробуйте еще раз! Мое число больше.");
            } else if (userGuess > randomNumber) {
                System.out.println("Попробуйте еще раз! Мое число меньше.");
            } else {
                System.out.println("Поздравляем! Вы угадали число " + randomNumber + " за " + attempts + " попыток.");
                break;
            }
        }

        scanner.close();
    }
}
