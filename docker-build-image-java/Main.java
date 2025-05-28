public class Main {
    public static void main(String[] args) {
        System.out.println("Benvenuto nella mia app Java in Docker!");

        for (int i = 1; i <= 5; i++) {
            System.out.println("Esecuzione step " + i);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println("Interrotto");
            }
        }

        System.out.println("Fine esecuzione.");
    }
}