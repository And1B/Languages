import java.util.ArrayList;

public class Language {
    protected String name;
    protected int numSpeakers;
    protected String regionsSpoken;
    protected String wordOrder;
    protected static ArrayList<Language> languages = new ArrayList<>();

    public Language(String langName, int speakers, String regions, String order) {
        this.name = langName;
        this.numSpeakers = speakers;
        this.regionsSpoken = regions;
        this.wordOrder = order;
    }

    // compiles a new language into an informative text about that certain language
    public void getInfo(){
        System.out.println(this.name + " is spoken by " + this.numSpeakers + " people mainly in " + this.regionsSpoken + ".");
        System.out.println("The language follows the word order: " + wordOrder + ".");
    }

    // lists all Information stored in the ArrayList languages compiled through the method getInfo
    public static void listAllInformation(ArrayList<Language> list){
        for (Language language : list) {
            language.getInfo();
        }
    }

 /*   public String setRegion(String region) {
        return this.regionsSpoken = region;
    }
    public static void changeNumbOfSpeakers(String language, int number){
    } */

    public static void main(String[] args){
        languages.add( new Language("English", 200000, "North America, Europe, Africa and Australia", "subject-verb-object"));
        languages.add( new Mayan("Chontal", 36810));
        languages.add( new SinoTibetan("Mandarin Chinese", 100000));
        listAllInformation(languages);
//      changeNumbOfSpeakers("English", 10000);
        System.out.println(languages.get(0));
    }
}
