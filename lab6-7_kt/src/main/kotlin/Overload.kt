class Solution {
    // метад для падліку сярэдняга арыфметычнага элементаў масіва
    fun solve(numbers: IntArray): Double {
        var sum = 0
        for (number in numbers) {
            sum += number
        }
        return sum.toDouble() / numbers.size
    }

    // метад для знаходжання лікаў у радку
    fun solve(text: String): Int {
        var count = 0
        for (char in text) {
            if (char.isLetter()) {
                count++
            }
        }
        return count
    }
}

fun main() {
    // аб'ект класа
    val solution = Solution()
    print("Выберыце тып увода: масіў або тэкст: ")
    val choice = readln()
    when (choice) {
        "масіў" -> {
            print("Увядзіце лікі праз прабел: ")
            val substrings = readln().split(" ")
            val numbers = substrings.filter { it.toIntOrNull() != null }.map { it.toInt() }.toIntArray()
            val average = solution.solve(numbers)
            println("Сярэдняя арыфметычнае лікаў: $average")
        }
        "тэкст" -> {
            print("Увядзіце тэкст: ")
            val text = readln()
            val letters = solution.solve(text)
            println("Колькасць літар у радку: $letters")
        }
        else -> {
            println("Няправільны выбар. Праграма завершана.")
        }
    }
}
