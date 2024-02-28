public class Person {
    // палі імя і узрост
    private String fullName;
    private int age;

    // канструктар без параметраў
    public Person() {
        fullName = "Невядомы";
        age = 0;
    }

    // канструкар з параметрамі
    public Person(String fullName, int age) {
        this.fullName = fullName;
        this.age = age;
    }

    // метад move
    public void move() {
        System.out.println(fullName + " рухаецца");
    }

    // метад talk
    public void talk() {
        System.out.println(fullName + " размаўляе");
    }
}
