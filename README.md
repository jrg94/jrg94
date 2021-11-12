# Welcome to My Profile!

This week's code snippet, Quick Sort in C, is brought to you by [Subete](https://subete.therenegadecoder.com/en/latest/) and the [Sample Programs repo](https://sample-programs.therenegadecoder.com/).

```C
#include  <stdio.h>
#include <string.h>
#include <stdlib.h>

long long get_val(int tmp[],int len){
    long long value=0,mult=1;
    for(int i=len-1;i>-1;--i){
        if(tmp[i]==' '-'0'){
            printf("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n");
            exit(0);
        }
        value+=tmp[i]*mult;
        mult*=10;
    }
    return value;
}


void swap(long long* a, long long* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 

int partition (long long arr[], int low, int high) 
{ 
    long long pivot = arr[high];    
    int i = low-1;

    for (int j = low; j <= high- 1; j++) 
    { 
        if (arr[j] < pivot) 
        { 
            i++;
            swap(&arr[i], &arr[j]); 
        } 
    } 
    swap(&arr[i + 1], &arr[high]); 
    return i+1; 
} 

void quickSort(long long arr[], int low, int high) 
{ 
    if (low < high) 
    { 
        int pi = partition(arr, low, high); 
        quickSort(arr, low, pi - 1); 
        quickSort(arr, pi + 1, high); 
    } 
} 

void print(long long arr[], int size) 
{ 
    for (int i=0; i < size; i++) 
    {
        printf("%lld", arr[i]); 
        if(i!=size-1)printf(", ");
    }
        
    printf("\n"); 
} 

int main(int argc,char **argv)
{
    while(argv[1]==NULL||strlen(argv[1])==0){
        printf("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n");
        return 0;
    }
    int len = strlen(argv[1]);
    int tmp[10];
    int ind=0;
    int pos=0;
    long long arr[100000];

    for(int i=0;i<len;++i){
        if(argv[1][i]==','){
            long long val = get_val(tmp,ind);
            ind=0;
            i++;
            arr[pos++]=val;
            continue;
        }
        tmp[ind++]=argv[1][i]-'0';
    }
    arr[pos++]=get_val(tmp,ind);
    if(pos==1){
        printf("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n");
        return 0;
    }


    quickSort(arr,0,pos-1);
    print(arr,pos);
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :dango: [Sharing the Fruits of My Fourth Hackathon](https://therenegadecoder.com/blog/sharing-the-fruits-of-my-fourth-hackathon/)
- :milky_way: [The Sample Programs READMEs Now Feature Missing Solutions](https://therenegadecoder.com/meta/the-sample-programs-readmes-now-feature-missing-solutions/)
- :milky_way: [Stuck in Your Coding Journey? Try Leveraging Bloom’s Taxonomy](https://therenegadecoder.com/teach/stuck-in-your-coding-journey-try-leveraging-blooms-taxonomy/)
- :exclamation: [Translations of The Renegade Coder Content](https://therenegadecoder.com/blog/translations-of-the-renegade-coder-content/)
- :exclamation: [Recommended Reading: “Some Final Thoughts on the SAT and ACT” by Jon Boeckenstedt](https://therenegadecoder.com/blog/recommended-reading-some-final-thoughts-on-the-sat-and-act-by-jon-boeckenstedt/)
- :fu: [Support The Sample Programs Repo This Hacktoberfest](https://therenegadecoder.com/meta/support-the-sample-programs-repo-this-hacktoberfest/)
- :cat: [Programmatically Explore Code Snippets of Many Languages Using Python](https://therenegadecoder.com/code/programmatically-explore-code-snippets-of-many-languages-using-python/)
- :tea: [How to Generate Markdown in Python Using SnakeMD](https://therenegadecoder.com/code/how-to-generate-markdown-in-python-using-snakemd/)
- :exclamation: [I Passed My Qualifying Exam!](https://therenegadecoder.com/blog/i-passed-my-qualifying-exam/)
- :tea: [How to Automate Your GitHub Profile](https://therenegadecoder.com/code/how-to-automate-your-github-profile/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://newsletter.therenegadecoder.com/)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2021-11-12 using [SnakeMD](https://snakemd.therenegadecoder.com).