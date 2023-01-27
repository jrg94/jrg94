# Welcome to My Profile!

This week's code snippet, Rot13 in Dart, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Dart
import 'dart:io';

main(List<String> args) {
  if (args.isEmpty || args[0].isEmpty) {
    print("Usage: please provide a string to encrypt");
    exit(1);
  } else {
    print( rot13(args[0]) );
  }
}

String rot13(String input) {
  int aLower = "a".codeUnitAt(0);
  int aUpper = "A".codeUnitAt(0);
  int nLower = "n".codeUnitAt(0);
  int nUpper = "N".codeUnitAt(0);
  int zLower = "z".codeUnitAt(0);
  int zUpper = "Z".codeUnitAt(0);

  List<String> coded = [];

  input.codeUnits.forEach((char) {
    if ((char >= aLower && char < nLower) ||
        (char >= aUpper && char < nUpper)) {
      coded.add(new String.fromCharCode(char + 13));
    } else if ((char >= nLower && char <= zLower) ||
        (char >= nUpper && char <= zUpper)) {
      coded.add(new String.fromCharCode(char - 13));
    } else {
      coded.add(new String.fromCharCode(char));
    }
  });

  return coded.join();
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :seedling: [Why Does == Sometimes Work on Strings in Java?](https://therenegadecoder.com/code/why-does-double-equals-sometimes-work-on-strings-in-java/)
- :lock: [2022: Year in Review](https://therenegadecoder.com/meta/2022-year-in-review/)
- :dango: [Reflecting on My 8th Semester of Teaching: Autumn 2022](https://therenegadecoder.com/blog/reflecting-on-my-8th-semester-of-teaching-autumn-2022/)
- :gem: [There Has to Be a Better Way: Reflecting on My Automation Catchphrase](https://therenegadecoder.com/blog/there-has-to-be-a-better-way-reflecting-on-my-automation-catchphrase/)
- :exclamation: [I Am a PhD Candidate!](https://therenegadecoder.com/blog/i-am-a-phd-candidate/)
- :lock: [Where Do Foo, Bar, and Baz Come From in Programming?](https://therenegadecoder.com/blog/where-do-foo-bar-and-baz-come-from-in-programming/)
- :lock: [How to Clamp a Floating Point Number in Python: Branching, Sorting, and More!](https://therenegadecoder.com/code/how-to-clamp-a-floating-point-number-in-python/)
- :cat: [Master Chief Collection’s Halo 2 Co-op Campaign Is Unplayable: Here Are Some Tips](https://therenegadecoder.com/blog/master-chief-collections-halo-2-co-op-campaign-is-unplayable-here-are-some-tips/)
- :lock: [How to Convert sqlite3 Rows into Python Objects](https://therenegadecoder.com/code/how-to-convert-sqlite3-rows-into-python-objects/)
- :seedling: [5 Ways to Share Code in Discord](https://therenegadecoder.com/code/5-ways-to-share-code-in-discord/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2023-01-27 using [SnakeMD](https://www.snakemd.io).