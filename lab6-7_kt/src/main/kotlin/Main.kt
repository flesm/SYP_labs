// функцыя знаходжання дзельнікаў уведзенага ліку
fun findDivisors(p: Int): List<Int> {
    val divisors = mutableListOf<Int>()
    for (i in 1..p) {
        if (p % i == 0) {
            divisors.add(i)
        }
    }
    return divisors
}

fun main() {
    while (true) {
        print("Увядзіце натуральны лік: ")
        val input = readln()
        val p = input.toIntOrNull()
        if (p != null && p > 0) {
            val divisors = findDivisors(p)
            println("Усе дзельнікі ліку $p: $divisors")
            break
        } else {
            println("Няправільны ўвод. Паспрабуйце яшчэ раз.")
        }
    }
}