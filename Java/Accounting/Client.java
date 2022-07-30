package Accounting;

public class Client {
    public static void main(String[] args) {
        Customer test = new Customer(0, "Max", "Mustermann");
        Account testAccount = new Account("1234314");
        Account realAccount = new Account("321895", 2500);
        System.out.println(testAccount.getAccountBalance());
        realAccount.depositMoney(2000);
        realAccount.depositMoney(200);
        realAccount.withdrawMoney(5000);
        realAccount.withdrawMoney(2000);
    }
}
