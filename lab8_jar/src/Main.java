public class Main {
    public static void main(String[] args) {
        // ствараем аб'ект класу Person без параметраў і з параметрамі
        Person p1 = new Person();
        Person p2 = new Person("Іваноў Іван Іванавіч", 52);

        p1.move();
        p1.talk();
        p2.move();
        p2.talk();
    }
}
