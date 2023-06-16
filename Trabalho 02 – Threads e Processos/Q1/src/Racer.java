public class Racer implements Runnable {
    private int racerNumber;

    public Racer(int racerNumber) {
        this.racerNumber = racerNumber;
    }

    @Override
    public void run() {
        while (true) {
            System.out.println("Racer " + racerNumber + " - imprimindo");
        }
    }

    public static void main(String[] args) {
        // Criação e instanciação da thread
        Thread racerThread = new Thread(new Racer(1));

        // Inicia a thread
        racerThread.start();

    }
}