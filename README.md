# Welcome to My Profile!

This week's code snippet, Merge Sort in Objective C, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Objective C
#import <Foundation/Foundation.h>

// Function to convert and validate the input string
// Source: ChatGPT
NSInteger convertAndValidateInput(NSString *inputString) {
    NSScanner *scanner = [NSScanner scannerWithString:inputString];
    NSInteger integerValue = 0;

    // Check if the scanner successfully scanned an integer
    if ([scanner scanInteger:&integerValue] && [scanner isAtEnd]) {
        return integerValue;
    } else {
        // Raise an exception for invalid input
        @throw [NSException exceptionWithName:@"InvalidInputException"
            reason:@"Input is not a valid integer"
            userInfo:nil];
    }
}

// Function to convert a comma-separated string to an array of integers
// Source: ChatGPT
NSArray *convertStringToListOfIntegers(NSString *inputString) {
    NSMutableArray *resultArray = [NSMutableArray array];

    // Separate the input string into components using the comma as a delimiter
    NSArray *components = [inputString componentsSeparatedByString:@","];

    // Convert each component to an integer using the previous function
    for (NSString *component in components) {
        NSNumber *numberValue = [NSNumber numberWithInteger:convertAndValidateInput(component)];
        [resultArray addObject:numberValue];
    }

    return [resultArray copy];
}

// Display array of integers
void displayListOfIntegers(NSArray *integerArray) {
    NSString *displayString = [integerArray componentsJoinedByString:@", "];
    printf("%s\n", [displayString UTF8String]);
}

////////////////MERGE-SORT////////////////
NSArray* mergeArrays(NSArray* A, NSArray* B) 
{
    NSMutableArray *orderedArray = [NSMutableArray new];
    long indexLeft = 0;
    long indexRight = 0;
    
    while (indexLeft < [A count] && indexRight < [B count]) {
        int leftValue = [[A objectAtIndex:indexLeft] intValue];
        int rightValue = [[B objectAtIndex:indexRight] intValue];
        if (leftValue < rightValue) {
            [orderedArray addObject:[A objectAtIndex:indexLeft++]];
        }else if (leftValue > rightValue){
            [orderedArray addObject:[B objectAtIndex:indexRight++]];
        }else { //equal values
            [orderedArray addObject:[A objectAtIndex:indexLeft++]];
            [orderedArray addObject:[B objectAtIndex:indexRight++]];
        }
    }
    
    //If one array has more positions than the other (odd lenght of the inital array)
    NSRange rangeRestLeft = NSMakeRange(indexLeft, A.count - indexLeft);
    NSRange rangeRestRight = NSMakeRange(indexRight, B.count - indexRight);
    NSArray *arrayTotalRight = [B subarrayWithRange:rangeRestRight];
    NSArray *arrayTotalLeft = [A subarrayWithRange:rangeRestLeft];
    arrayTotalLeft = [orderedArray arrayByAddingObjectsFromArray:arrayTotalLeft];
    NSArray *orderedArrayCompleted = [arrayTotalLeft arrayByAddingObjectsFromArray:arrayTotalRight];
    return orderedArrayCompleted;
}

NSArray* mergeSort(NSArray* randomArray){
    
    if ([randomArray count] < 2)
    {
        return randomArray;
    }
    int middlePivot = (int)[randomArray count]/2;
    NSRange rangeLeft = NSMakeRange(0, middlePivot);
    NSRange rangeRight = NSMakeRange(middlePivot, randomArray.count-middlePivot);
    NSArray *leftArray = [randomArray subarrayWithRange:rangeLeft];
    NSArray *rightArray = [randomArray subarrayWithRange:rangeRight];
    return mergeArrays(mergeSort(leftArray),mergeSort(rightArray));
}

int main(int argc, char *argv[]) {
    NSAutoreleasePool *pool =[[NSAutoreleasePool alloc] init];
    NSString *usage = @"Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"";
    if (argc < 2) {
        printf("%s\n", [usage UTF8String]);
    }
    else {
        NSString* inputStr = [NSString stringWithUTF8String:argv[1]];
        @try {
            NSArray *inputArray = convertStringToListOfIntegers(inputStr);
            if ([inputArray count] < 2) {
                printf("%s\n", [usage UTF8String]);
            }
            else {
                NSArray *sortedArray = mergeSort(inputArray);
                displayListOfIntegers(sortedArray);
            }
        }
        @catch (NSException *) {
            printf("%s\n", [usage UTF8String]);
        }
    }

    [pool drain];
    return 0;
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :thought_balloon: [2024: Year in Review](https://therenegadecoder.com/meta/2024-year-in-review/)
- :black_nib: [Is Anyone Else Bothered by How Quickly We Adopted Generative AI?](https://therenegadecoder.com/blog/is-anyone-else-bothered-by-how-quickly-we-adopted-generative-ai/)
- :black_nib: [31 Lessons Learned as a New Dad](https://therenegadecoder.com/blog/31-lessons-learned-as-a-new-dad/)
- :apple: [So You’re Not Sure If Computer Science Is for You](https://therenegadecoder.com/teach/so-youre-not-sure-if-computer-science-is-for-you/)
- :apple: [You Should Give Open-Ended Projects to Your Students](https://therenegadecoder.com/teach/you-should-give-open-ended-projects-to-your-students/)
- :computer: [How to Move Your Extensions Folder in VS Code](https://therenegadecoder.com/code/how-to-move-your-extensions-folder-in-vs-code/)
- :thought_balloon: [Sample Programs Repo Celebrates 1,000 Code Snippets](https://therenegadecoder.com/meta/sample-programs-repo-celebrates-1000-code-snippets/)
- :apple: [Canvas Is Not Built With Educators in Mind](https://therenegadecoder.com/teach/canvas-is-not-built-with-educators-in-mind/)
- :computer: [Workshopping a Tier List Generator](https://therenegadecoder.com/code/workshopping-a-tier-list-generator/)
- :black_nib: [No, The GRE Should Not Be Reinstated](https://therenegadecoder.com/blog/no-the-gre-should-not-be-reinstated/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-02-28 using [SnakeMD](https://www.snakemd.io).