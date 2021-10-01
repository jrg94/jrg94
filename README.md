# Welcome to My Profile!

This week's code snippet, Linear Search in Java, is brought to you by [Subete](https://subete.therenegadecoder.com/en/latest/) and the [Sample Programs repo](https://sample-programs.therenegadecoder.com/).

```Java
import java.util.*;

public class LinearSearch {

    public static void main(String[] args) {
        try {
            ArrayList<Integer> listOfNumbers = new ArrayList<>();
            Integer keyToSearch = Integer.parseInt(args[1]);
            String[] NumberArray = args[0].split(",");
            for(String Number: NumberArray) {
                listOfNumbers.add(Integer.parseInt(Number.trim()));
            }
            if(listOfNumbers.size() >= 1){
                StringBuilder output = new StringBuilder();
                Boolean searched = linearSearch(listOfNumbers, keyToSearch);
                System.out.println(searched);
            }else{
                System.out.println("Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")");
            }
        }
        catch(Exception e) {
            System.out.println("Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")");
        }
    }

    private static Boolean linearSearch(ArrayList<Integer> list, Integer keyToSearch) {
        Boolean ans = false;
        for (Integer number : list) {
            if(number == keyToSearch) {
                ans = true;
                break;
            }
        }
        return ans;
    }
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :seedling: [Programmatically Explore Code Snippets of Many Languages Using Python](https://therenegadecoder.com/code/programmatically-explore-code-snippets-of-many-languages-using-python/)
- :gem: [How to Generate Markdown in Python Using SnakeMD](https://therenegadecoder.com/code/how-to-generate-markdown-in-python-using-snakemd/)
- :door: [I Passed My Qualifying Exam!](https://therenegadecoder.com/blog/i-passed-my-qualifying-exam/)
- :lock: [How to Automate Your GitHub Profile](https://therenegadecoder.com/code/how-to-automate-your-github-profile/)
- :door: [Practice Your Coding Skills With the Sample Programs Template](https://therenegadecoder.com/meta/practice-your-coding-skills-with-the-sample-programs-template/)
- :exclamation: [Sample Programs Docs Generator 2.3.0 Features How To Python README Automation](https://therenegadecoder.com/meta/sample-programs-docs-generator-2-3-0-features-how-to-python-readme-automation/)
- :seedling: [Making a Discord Bot Roll a Die in Python](https://therenegadecoder.com/code/making-a-discord-bot-roll-a-die-in-python/)
- :gem: [Making Sense of the Discord Webhook Object in Python](https://therenegadecoder.com/code/making-sense-of-the-discord-webhook-object-in-python/)
- :door: [Breaking Down a Hello World Discord Bot in Python](https://therenegadecoder.com/code/breaking-down-a-hello-world-discord-bot-in-python/)
- :dango: [Chiropractors Have Broken My YouTube Recommendations](https://therenegadecoder.com/blog/chiropractors-have-broken-my-youtube-recommendations/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://newsletter.therenegadecoder.com/)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2021-10-01 using [SnakeMD](https://snakemd.therenegadecoder.com).