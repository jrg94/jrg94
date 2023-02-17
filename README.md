# Welcome to My Profile!

This week's code snippet, Fraction Math in Swift, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Swift
// for System.exit()
import Foundation


/*
    Implementation of the Euclid's Algorithm.
    Used to simplify the fractions during initialization
*/
func gcd(_ a: Int, _ b:Int) -> Int {
    var a = a >= 0 ? a : -a
    var b = b
    var tmp = 0
    while b != 0 {
        tmp = b
        b = a % b
        a = tmp
    }
    return a
}

/*
    Used for Type conversion Bool => Int
*/
extension Bool {
    var intValue: Int {
        return self ? 1 : 0
    }    
}

struct IntFraction {
    var numerator, denominator: Int

    init(_ num:Int, _ denom:Int) {
        guard denom != 0 else {
            print("Error: Denominator cannot be 0")
            exit(0)
        }

        var num = num
        if denom < 0 {
            num = -num
        }
        let gcd_ = gcd(num, denom) 
        numerator = num / gcd_
        denominator = denom / gcd_
    }

    init?(fromString str:String) {
        let parts = str.components(separatedBy: "/")
        guard parts.count == 2, let num = Int(parts[0]), let denom = Int(parts[1]) else {
            return nil
        }

        self.init(num, denom)
    }


    static func +(lhs: IntFraction, rhs: IntFraction) -> IntFraction {
        let top = lhs.numerator*rhs.denominator + rhs.numerator*lhs.denominator
        let bottom = lhs.denominator*rhs.denominator
        return IntFraction(top, bottom)
    }

    static func -(lhs: IntFraction, rhs: IntFraction) -> IntFraction {
        let top = lhs.numerator*rhs.denominator - rhs.numerator*lhs.denominator
        let bottom = lhs.denominator*rhs.denominator
        return IntFraction(top, bottom)
    }

    static func *(lhs: IntFraction, rhs: IntFraction) -> IntFraction {
        return IntFraction(lhs.numerator*rhs.numerator, lhs.denominator*rhs.denominator)
    }

    static func /(lhs: IntFraction, rhs: IntFraction) -> IntFraction {
        let top = lhs.numerator*rhs.denominator
        let bottom = lhs.denominator*rhs.numerator
        return IntFraction(top, bottom);
    }

    static func ==(lhs: IntFraction, rhs: IntFraction) -> Bool {
        let res = lhs.numerator * rhs.denominator - rhs.numerator * lhs.denominator
        return res == 0
    }

    static func >(lhs: IntFraction, rhs: IntFraction) -> Bool {
        let res = lhs.numerator * rhs.denominator - rhs.numerator * lhs.denominator
        return res > 0
    }

    static func <(lhs: IntFraction, rhs: IntFraction) -> Bool {
        let res = lhs.numerator * rhs.denominator - rhs.numerator * lhs.denominator
        return res < 0
    }

    static func >=(lhs: IntFraction, rhs: IntFraction) -> Bool {
        return !(lhs < rhs)
    }

    static func <=(lhs: IntFraction, rhs: IntFraction) -> Bool {
        return !(lhs > rhs)
    }

    static func !=(lhs: IntFraction, rhs: IntFraction) -> Bool {
        return !(lhs == rhs)
    }
}


/*
    Check validity of command line arguments
*/
guard CommandLine.argc == 4 else {
    print("Usage: \(CommandLine.arguments[0]) operand1 operator operand2")
    exit(0)
}
guard let operand1 = IntFraction(fromString: CommandLine.arguments[1]), let operand2 = IntFraction(fromString: CommandLine.arguments[3]) else {
    print("Invalid operand. Usage: a/b => 3/4")
    exit(0)
}

let op = CommandLine.arguments[2]
switch op {
case "+":
    let res = operand1 + operand2
    print("\(res.numerator)/\(res.denominator)")
case "-":
    let res = operand1 - operand2
    print("\(res.numerator)/\(res.denominator)")
case "*":
    let res = operand1 * operand2
    print("\(res.numerator)/\(res.denominator)")
case "/":
    let res = operand1 / operand2
    print("\(res.numerator)/\(res.denominator)")
case "==":
    let res = operand1 == operand2
    print("\(res.intValue)")
case ">":
    let res = operand1 > operand2
    print("\(res.intValue)")
case "<":
    let res = operand1 < operand2
    print("\(res.intValue)")
case ">=":
    let res = operand1 >= operand2
    print("\(res.intValue)")
case "<=":
    let res = operand1 <= operand2
    print("\(res.intValue)")
case "!=":
    let res = operand1 != operand2
    print("\(res.intValue)")
default:
    print("No matching operation for symbol: '\(op)'")
    exit(0)
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :tea: [Design by Contract Hinges on Implication](https://therenegadecoder.com/code/design-by-contract-hinges-on-implication/)
- :cat: [Maybe It’s Not Okay to Test Private Methods—at Least When Using Design by Contract](https://therenegadecoder.com/code/maybe-its-not-okay-to-test-private-methods-at-least-when-using-design-by-contract/)
- :gem: [29 Things I’d Only Say If I Were Kidnapped](https://therenegadecoder.com/blog/29-things-id-only-say-if-i-were-kidnapped/)
- :milky_way: [Why Does == Sometimes Work on Strings in Java?](https://therenegadecoder.com/code/why-does-double-equals-sometimes-work-on-strings-in-java/)
- :door: [2022: Year in Review](https://therenegadecoder.com/meta/2022-year-in-review/)
- :milky_way: [Reflecting on My 8th Semester of Teaching: Autumn 2022](https://therenegadecoder.com/blog/reflecting-on-my-8th-semester-of-teaching-autumn-2022/)
- :cat: [There Has to Be a Better Way: Reflecting on My Automation Catchphrase](https://therenegadecoder.com/blog/there-has-to-be-a-better-way-reflecting-on-my-automation-catchphrase/)
- :fu: [I Am a PhD Candidate!](https://therenegadecoder.com/blog/i-am-a-phd-candidate/)
- :seedling: [Where Do Foo, Bar, and Baz Come From in Programming?](https://therenegadecoder.com/blog/where-do-foo-bar-and-baz-come-from-in-programming/)
- :milky_way: [How to Clamp a Floating Point Number in Python: Branching, Sorting, and More!](https://therenegadecoder.com/code/how-to-clamp-a-floating-point-number-in-python/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2023-02-17 using [SnakeMD](https://www.snakemd.io).