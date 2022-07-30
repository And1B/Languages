package Accounting;

public class Account extends Client {
    private double accountBalance;
    private String accountNo;

    public Account(String accountNo){
        this.accountNo = accountNo;
        this.accountBalance = 0;
        System.out.println("Thank you for creating an Account with our Bank!");
        sayAccountNo();
        sayBalance();
    }

    public Account(String accountNo, double accountBalance){
        this.accountNo = accountNo;
        this.accountBalance = accountBalance;
        System.out.println("Thank you for creating an Account with our Bank!");
        sayAccountNo();
        sayBalance();
    }

    public double getAccountBalance(){
        return this.accountBalance;
    }

    public void setAccountBalance(double accountBalance){
        this.accountBalance = accountBalance;
        sayBalance();
    }

    public String getAccountNo(){
        return this.accountNo;
    }

    public void setAccountNo(String accountNo){
        sayAccountNo();
        this.accountNo = accountNo;
    }

    public boolean booking(double amount){
        if(amount > this.accountBalance){
            System.out.println("You don't have enough money!");
            return false;
        } else {
            this.accountBalance -= amount;
            System.out.println("Booking was successfull.");
            sayBalance();
            return true;
        }
    }

    public boolean withdrawMoney(double amount){
        if(amount > this.accountBalance){
            System.out.println("You tried withdrawing more money than you own. Nice try.");
            sayBalance();
            return false;
        } else {
            this.accountBalance -= amount;
            System.out.println("Withdrawing succeeded. Please don*t forget your card and your money.");
            sayBalance();
            return true;
        }
    }

    public void sayAccountNo(){
        System.out.println("Your Account Number is: " + this.accountNo);
    }

    public void sayBalance(){
        System.out.println("Your balance is: " + this.accountBalance + " Euro");
    }

    public boolean depositMoney(double amount){
        if(amount <= 0){
            System.out.println("Please select a value above Zero..");
            return false;
        } else {
            this.accountBalance += amount;
            System.out.println("Thank you for using our depositing service.");
            sayBalance();
            return true;
        }
    }

}
