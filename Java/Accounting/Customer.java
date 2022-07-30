package Accounting;

public class Customer extends Client {
    private int customerNo;
    private String firstName;
    private String lastName;
    
    public Customer(int customerNo, String firstName, String lastName){
        this.customerNo = customerNo;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public int getCustomerNo(){
        return this.customerNo;
    }

    public void setCustomerNo(int customerNo){
        this.customerNo = customerNo;
        System.out.println("New Customer Number: " + this.customerNo);
    }

    public String getCustomerName(){
        return this.firstName + " " + this.lastName;
    }

    public void setCustomerName(String firstName, String lastName){
        this.firstName = firstName;
        this.lastName = lastName;
        System.out.println("New Account Name: " + getCustomerName());
    }

}
