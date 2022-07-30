package Personen;

public class Schueler extends Personen{
    private String classTeacher;
    private double finalGrade;

    Schueler(String firstName, String lastName, double height) {
        super(firstName, lastName, height);
    }

    public String getClassTeacher(){
        return this.classTeacher;
    }

    public void setClassTeacher(String classTeacher){
        this.classTeacher = classTeacher;
    }

    public double getFinalGrade(){
        return this.finalGrade;
    }

    public void setFinalGrade(double finalGrade){
        this.finalGrade = finalGrade;
    }

}
