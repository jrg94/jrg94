# Welcome to My Profile!

This week's code snippet, Rot 13 in Php, is brought to you by [Subete](https://subete.therenegadecoder.com/en/latest/) and the [Sample Programs repo](https://sample-programs.therenegadecoder.com/).

```Php
<?php

if (empty($argv[1]) || $argv[1] == "" || count($argv) == 0) {
    die("Usage: please provide a string to encrypt\n");
}

function rot13(string $string) {
    return strtr($string,
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm');
}

echo rot13($argv[1]) . "\n";
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :notes: [Practice Your Coding Skills With the Sample Programs Template](https://therenegadecoder.com/meta/practice-your-coding-skills-with-the-sample-programs-template/)
- :exclamation: [Sample Programs Docs Generator 2.3.0 Features How To Python README Automation](https://therenegadecoder.com/meta/sample-programs-docs-generator-2-3-0-features-how-to-python-readme-automation/)
- :milky_way: [Making a Discord Bot Roll a Die in Python](https://therenegadecoder.com/code/making-a-discord-bot-roll-a-die-in-python/)
- :cat: [Making Sense of the Discord Webhook Object in Python](https://therenegadecoder.com/code/making-sense-of-the-discord-webhook-object-in-python/)
- :seedling: [Breaking Down a Hello World Discord Bot in Python](https://therenegadecoder.com/code/breaking-down-a-hello-world-discord-bot-in-python/)
- :door: [Chiropractors Have Broken My YouTube Recommendations](https://therenegadecoder.com/blog/chiropractors-have-broken-my-youtube-recommendations/)
- :tea: [Introduction to Python Coding With Discord Bots](https://therenegadecoder.com/code/introduction-to-python-coding-with-discord-bots/)
- :gem: [Write-Only Discord Bots Are Surprisingly Easy to Code in Python](https://therenegadecoder.com/code/write-only-discord-bots-are-surprisingly-easy-to-code-in-python/)
- :lock: [Sample Programs Docs Generator 2.0.3 Features README Automation](https://therenegadecoder.com/meta/sample-programs-docs-generator-2-0-3-features-readme-automation/)
- :tea: [Visualizing My 2020 Hum Driving History Using Python](https://therenegadecoder.com/code/visualizing-my-2020-hum-driving-history-using-python/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://newsletter.therenegadecoder.com/)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2021-09-03 using [SnakeMD](https://snakemd.therenegadecoder.com).