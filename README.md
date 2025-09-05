# Welcome to My Profile!

This week's code snippet, Factorial in C, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```C
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

int uint64_overflow(long, long);

int main (int argc, char *argv[])
{
	long n;
	char *endptr;
	uint64_t result = 1;
	long i;

	/* Correct nmber of args? */
	if (argc != 2) {
		printf("Usage: please input a non-negative integer\n");
		exit(0);
	}

	/* Convert argument to number */
	errno = 0;
	n = strtol(argv[1], &endptr, 10);
	if ((errno == ERANGE && (n == LONG_MAX || n == LONG_MIN))
			|| (errno != 0 && n == 0)) {
		perror("strtol");
		exit(1);
	}

	if (endptr == argv[1] ||
			!(*endptr == '\0' || *endptr == '\n') ||
			n < 0) {
		fprintf(stderr, "Usage: please input a non-negative integer\n");
		exit(1);
	}

	/* For non-zero numbers, compute factorial */
	if (n) {
		for (i = 1; i <= n; i++) {
			if (uint64_overflow(result, i)) {
				printf("Results overflowed\n");
				exit(1);
			}

			result *= i;
		}
	}

	/* Priunt result */
	printf("%ld\n", result);

	return 0;
}

/*
 * Detects overflow from 64-bit multiplication.
 *
 * Returns 1 if an overflow occurs, 0 if not
 */
int uint64_overflow(long a, long b) {
	uint64_t x;
	uint64_t b_64;

	x = a * b;
	b_64 = b;

	return (a != 0 && x / a != b_64) ? 1 : 0;
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [Technology Will Not Liberate Us](https://therenegadecoder.com/blog/technology-will-not-liberate-us/)
- :black_nib: [The Future of AI Is Ubiquitous Surveillance](https://therenegadecoder.com/blog/the-future-of-ai-is-ubiquitous-surveillance/)
- :black_nib: [Y’all Need to Stop Using Generative AI for Summaries](https://therenegadecoder.com/blog/yall-need-to-stop-using-generative-ai-for-summaries/)
- :computer: [Loop Invariants Are Necessary for Writing Proper Loops](https://therenegadecoder.com/code/loop-invariants-are-necessary-for-writing-proper-loops/)
- :computer: [Dark Arts: Labeled Statements in Java](https://therenegadecoder.com/code/dark-arts-labeled-statements-in-java/)
- :apple: [Gamification Will Not Solve “America’s Education Crisis”](https://therenegadecoder.com/teach/gamification-will-not-solve-americas-education-crisis/)
- :black_nib: [“Just Ask Chat”: The Evolution of an Isolating Mantra](https://therenegadecoder.com/blog/just-ask-chat-the-evolution-of-an-isolating-mantra/)
- :black_nib: [Life Update: I’m Doing Well](https://therenegadecoder.com/blog/life-update-im-doing-well/)
- :black_nib: [The Worst Use Cases for Generative AI That Are Already Mainstream](https://therenegadecoder.com/blog/the-worst-use-cases-for-generative-ai-that-are-already-mainstream/)
- :black_nib: [ChatGPT Is Stack Overflow for the Lazy and Helpless](https://therenegadecoder.com/blog/chatgpt-is-stack-overflow-for-the-lazy-and-helpless/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-09-05 using [SnakeMD](https://www.snakemd.io).