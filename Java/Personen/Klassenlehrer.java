package Personen;

public class Klassenlehrer extends Personen {

    private Schueler[] pupil = new Schueler[32];
    private int anz_sch = 0;

    Klassenlehrer(String firstName, String lastName, double height){
        super(firstName, lastName, height);
    }

    public boolean setPupil(Schueler pupil){
        if (anz_sch < 33){
            System.out.println("The pupil " + pupil.getFirstName() + " " + pupil.getLastName() + " was added.");
            this.pupil[anz_sch] = pupil;
            anz_sch += 1;
            return true;
        } else{
            return false;
        }
    }

    public Schueler getPupil(int i){
        if (pupil[i] != null){
            return pupil[i];
        }
        return pupil[i];
    }

    public void setGradePupil(double grade, Schueler pupil){
        pupil.setFinalGrade(grade);
    }

    // public double getClassGradeAverage(){
    //     return  / pupil.length;
    // }

}
