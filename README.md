# Welcome to My Profile!

This week's code snippet, Palindromic Number in Perl, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Perl
# accept an integer, reverse it, compare it with original
# print true, if original and reversed number are same
# print false, if original and reversed number are same
#!/usr/bin/env perl
use strict;
use warnings;

# no input
usage() unless @ARGV == 1;

# accept input as argument
my ($number) = @ARGV;

# if not provided, read from standard input
if (!defined $number) {
	$number = <STDIN>;
	chomp $number;
}

if (!defined $number || $number !~ /^\d+$/ || $number < 0) {
	usage();
}

my $temp = $number;
my $noofdigits = 0;
my $reversed_number = 0;
while ($temp > 0){
  $reversed_number = ($reversed_number * 10) + ($temp % 10);
  $temp = int($temp / 10);
  $noofdigits += 1;
}

if ($number < 0){
  print("Usage: please input a non-negative integer")
}

else{
  if ($reversed_number == $number){
    print("true");
    }
  else{
    print("false");
  }

}

sub usage {
	print "Usage: please input a non-negative integer";
	exit;
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [How to Version Your Python Projects for Pip](https://therenegadecoder.com/code/how-to-version-your-python-projects-for-pip/)
- :black_nib: [No One Uses Loop Invariants: Just Ask Google](https://therenegadecoder.com/blog/no-one-uses-loop-invariants-just-ask-google/)
- :computer: [How to Migrate to SnakeMD 2.0.0](https://therenegadecoder.com/code/how-to-migrate-to-snakemd-2-0-0/)
- :thought_balloon: [The Renegade Coder Is Taking a Little Break](https://therenegadecoder.com/meta/the-renegade-coder-is-taking-a-little-break/)
- :computer: [Why Is Adding Two Random Numbers Not the Same as Generating One in the Same Range?](https://therenegadecoder.com/code/why-is-adding-two-random-numbers-not-the-same-as-generating-one-in-the-same-range/)
- :computer: [Design by Contract Hinges on Implication](https://therenegadecoder.com/code/design-by-contract-hinges-on-implication/)
- :computer: [Maybe It’s Not Okay to Test Private Methods—at Least When Using Design by Contract](https://therenegadecoder.com/code/maybe-its-not-okay-to-test-private-methods-at-least-when-using-design-by-contract/)
- :black_nib: [29 Things I’d Only Say If I Were Kidnapped](https://therenegadecoder.com/blog/29-things-id-only-say-if-i-were-kidnapped/)
- :computer: [Why Does == Sometimes Work on Strings in Java?](https://therenegadecoder.com/code/why-does-double-equals-sometimes-work-on-strings-in-java/)
- :thought_balloon: [2022: Year in Review](https://therenegadecoder.com/meta/2022-year-in-review/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-05-02 using [SnakeMD](https://www.snakemd.io).