# Welcome to My Profile!

This week's code snippet, Roman Numeral in C, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```C
#include  <stdio.h>
#include <stdlib.h>
#include <string.h>

int val[150];

int main(int argc,char **argv)
{
    if(argv[1]==NULL){
        printf("Usage: please provide a string of roman numerals");
        return 0;
    }
    if(strlen(argv[1])==0){
        printf("0");
        return 0;
    }
    
    int len=strlen(argv[1]);
    val['I']=1;
    val['V']=5;
    val['X']=10;
    val['L']=50;
    val['C']=100;
    val['D']=500;
    val['M']=1000;
    long long ans=0;
    
    for(int i=1;i<len;++i){
        if(!val[argv[1][i]]){
            printf("Error: invalid string of roman numerals");
            return 0;
        }
        if(val[argv[1][i]]>val[argv[1][i-1]])ans-=2*val[argv[1][i-1]];
        ans+=val[argv[1][i]];
    }
    if(!val[argv[1][0]]){
        printf("Error: invalid string of roman numerals");
        return 0;
    }
    printf("%lld",ans+val[argv[1][0]]);
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :gem: [Why Does == Sometimes Work on Strings in Java?](https://therenegadecoder.com/code/why-does-double-equals-sometimes-work-on-strings-in-java/)
- :notes: [2022: Year in Review](https://therenegadecoder.com/meta/2022-year-in-review/)
- :door: [Reflecting on My 8th Semester of Teaching: Autumn 2022](https://therenegadecoder.com/blog/reflecting-on-my-8th-semester-of-teaching-autumn-2022/)
- :seedling: [There Has to Be a Better Way: Reflecting on My Automation Catchphrase](https://therenegadecoder.com/blog/there-has-to-be-a-better-way-reflecting-on-my-automation-catchphrase/)
- :seedling: [I Am a PhD Candidate!](https://therenegadecoder.com/blog/i-am-a-phd-candidate/)
- :seedling: [Where Do Foo, Bar, and Baz Come From in Programming?](https://therenegadecoder.com/blog/where-do-foo-bar-and-baz-come-from-in-programming/)
- :fu: [How to Clamp a Floating Point Number in Python: Branching, Sorting, and More!](https://therenegadecoder.com/code/how-to-clamp-a-floating-point-number-in-python/)
- :fu: [Master Chief Collection’s Halo 2 Co-op Campaign Is Unplayable: Here Are Some Tips](https://therenegadecoder.com/blog/master-chief-collections-halo-2-co-op-campaign-is-unplayable-here-are-some-tips/)
- :exclamation: [How to Convert sqlite3 Rows into Python Objects](https://therenegadecoder.com/code/how-to-convert-sqlite3-rows-into-python-objects/)
- :door: [5 Ways to Share Code in Discord](https://therenegadecoder.com/code/5-ways-to-share-code-in-discord/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2023-02-03 using [SnakeMD](https://www.snakemd.io).