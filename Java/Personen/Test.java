package Personen;

public class Test {
    public static void main(String[] args){
        String[][] pupil_data = {
            {"Hans", "Meiser"},
            {"Peter", "Adler"},
            {"Maria", "Kranich"},
            {"Edith", "Spatz"},
            {"Karl", "Taube"},
            {"Max", "Mustermann"}
        };

        Klassenlehrer classTeacher = new Klassenlehrer("Michael", "Müller", 1.78);
        
        for(int i = 0; i < pupil_data.length; i++){
            Schueler s = new Schueler(pupil_data[i][0], pupil_data[i][1], 1.80);
            classTeacher.setPupil(s);
        }
        String[] classTrip = new String[33];
        classTrip[0] = "Class Teacher: " + classTeacher.getFirstName() + " " + classTeacher.getLastName();
        System.out.println();

        for(int i = 0; i < 33; i++){
            if (classTeacher.getPupil(i) == null){
                break;
            } else{
                classTrip[i + 1] = i + 1 + ". " + classTeacher.getPupil(i).getFirstName() + " " + classTeacher.getPupil(i).getLastName();
            }
        }

        for(int i = 0; i < classTrip.length; i++){
            if (classTrip[i] != null){
                System.out.println(classTrip[i]);
            }
        }
    }
}