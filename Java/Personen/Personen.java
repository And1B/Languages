package Personen;

public class Personen {
    private String firstName;
    private String lastName;
    private double height;

    Personen(String firstName, String lastName, double height){
        this.firstName = firstName;
        this.lastName = lastName;
        this.height = height;
    }

    public void writing(String sentence){
        System.out.println(sentence);
    }

    public String sayName(){
        return this.firstName + " " + this.lastName;
    }

    public String getFirstName(){
        return this.firstName;
    }

    public void setFirstName(String firstName){
        this.firstName = firstName;
    }

    public String getLastName(){
        return this.lastName;
    }

    public void setLastName(String lastName){
        this.lastName = lastName;
    }

    public double getHeight(){
        return this.height;
    }

    public void setHeight(double height){
        this.height = height;
    }
}
