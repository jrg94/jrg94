# Welcome to My Profile!

This week's code snippet, Bubble Sort in Dart, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Dart
import 'dart:io';

main(List<String> args) {
  try {
    List<double> numbersList = parseInput(args.join());
    if (numbersList.length <= 1) exitWithError();
    print(bubbleSort(numbersList));
  } catch (e) {
    exitWithError();
  }
}

String bubbleSort(List<double> numbersList) {
  bool pairSwapped = true;
  int listLength = numbersList.length;

  while (pairSwapped) {
    pairSwapped = false;

    for (int position = 0; position < listLength - 1; position++) {
      if (numbersList[position] > numbersList[position + 1]) {
        numbersList = swapPair(numbersList, position, (position + 1));
        pairSwapped = true;
      }
    }
  }

  return formatOutput(numbersList);
}

List<double> swapPair(
    List<double> numbersList, int currentPosition, int nextPosition) {
  double currentValue = numbersList[currentPosition];

  numbersList[currentPosition] = numbersList[nextPosition];
  numbersList[nextPosition] = currentValue;

  return numbersList;
}

String formatOutput(List<double> numbersList) {
  List<String> output = [];

  numbersList.forEach((number) {
    output.add((number * 10) % 10 != 0 ? "$number" : "${number.toInt()}");
  });

  return output.join(", ");
}

List<double> parseInput(String input) {
  List<double> parsedList = [];

  for (String item in input.replaceAll(" ", "").split(",")) {
    parsedList.add(double.parse(item));
  }

  return parsedList;
}

exitWithError() {
  print(
      'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
  exit(1);
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [What It Takes to Throw a Celebration of Life](https://therenegadecoder.com/blog/what-it-takes-to-throw-a-celebration-of-life/)
- :black_nib: [Using Ethnography to Advocate for Student Needs in Computer Science Education](https://therenegadecoder.com/blog/using-ethnography-to-advocate-for-student-needs-in-computer-science-education/)
- :computer: [3 Key Programming Best Practices for Beginners](https://therenegadecoder.com/code/programming-best-practices-for-beginners/)
- :black_nib: [What Restoring a 20-Year-Old Deck Looks Like](https://therenegadecoder.com/blog/what-refreshing-a-20-year-old-deck-looks-like/)
- :black_nib: [Java Has A Remainder Operator—Not a Mod Operator](https://therenegadecoder.com/blog/java-has-a-remainder-operator-not-a-mod-operator/)
- :black_nib: [5 Things You Should Know Before You Pick Up Python](https://therenegadecoder.com/blog/things-you-should-know-before-you-pick-up-python/)
- :black_nib: [Flexible Interfaces With Optional Methods Are Good: A Java List Case Study](https://therenegadecoder.com/blog/flexible-interfaces-with-optional-methods-are-good-a-java-list-case-study/)
- :computer: [Poetry Is The Best Way to Manage Your Python Projects](https://therenegadecoder.com/code/poetry-is-the-best-way-to-manage-your-python-projects/)
- :black_nib: [Making a Sandwich is Not Rocket Science: How Elitists Always Stay on Top](https://therenegadecoder.com/blog/making-a-sandwich-is-not-rocket-science-how-elitists-always-stay-on-top/)
- :computer: [How to Version Your Python Projects for Pip](https://therenegadecoder.com/code/how-to-version-your-python-projects-for-pip/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-06-30 using [SnakeMD](https://www.snakemd.io).