# Welcome to My Profile!

This week's code snippet, Minimum Spanning Tree in Euphoria, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/sequence.e
include std/utils.e
include std/math.e
include std/mathcons.e

-- Indices for value() return value
enum VALUE_ERROR_CODE, VALUE_VALUE, VALUE_NUM_CHARS_READ

-- Indices for parse_int() return value
enum PARSE_INT_VALID, PARSE_INT_VALUE

function parse_int(sequence s)
    -- Trim off whitespace and parse string
    s = trim(s)
    sequence result = stdget:value(s,, GET_LONG_ANSWER)

    -- Error if any errors, value is not an integer, or any leftover characters
    boolean valid = (
        result[VALUE_ERROR_CODE] = GET_SUCCESS
        and integer(result[VALUE_VALUE])
        and result[VALUE_NUM_CHARS_READ] = length(s)
    )

    -- Get value if invalid
    integer value = 0
    if valid
    then
        value = result[VALUE_VALUE]
    end if

    return {valid, value}
end function

-- Indices for parse_int_list() return value
enum PARSE_INT_LIST_VALID, PARSE_INT_LIST_VALUES

function parse_int_list(sequence s)
    -- Split string on comma
    sequence list = split(s, ",")

    -- Parse each item
    integer valid = FALSE
    sequence values = {}
    for n = 1 to length(list)
    do
        sequence result = parse_int(list[n])
        valid = result[PARSE_INT_VALID]
        values &= result[PARSE_INT_VALUE]
        if not valid
        then
            exit
        end if
    end for

    return {valid, values}
end function

procedure usage()
    puts(STDOUT, "Usage: please provide a comma-separated list of integers\n")
    abort(0)
end procedure

-- Indices for node values
enum NODE_INDEX, NODE_WEIGHT

-- Create graph from weights.
-- The graph consists of a sequence of nodes.
-- Each node consists of a weight and sequence of neighbor indices
function create_graph(sequence weights, integer num_vertices)
    -- Initialize nodes
    sequence nodes = repeat({}, num_vertices)

    -- Get neighbors for this node based on weights
    integer num_weights = length(weights)
    integer index = 0
    for row = 1 to num_vertices
    do
        -- Add neighbor node indices and weights to this node
        for col = 1 to num_vertices
        do
            index += 1
            if weights[index] > 0
            then
                nodes[row] &= {{col, weights[index]}}
            end if
        end for
    end for

    return nodes
end function

-- Indices for Minimum Spanning Tree
enum MST_VERTEX1, MST_VERTEX2, MST_WEIGHT

-- Prim's Minimum Spanning Tree (MST) Algorithm based on C implementation of
-- https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
function prim_mst(sequence graph)
    integer num_vertices = length(graph)

    -- Array to store constructed MST. Indicate no parents yet
    sequence parents = repeat(0, num_vertices)

    -- Key values used to pick minimum weight edge. Initialize to infinity
    sequence keys = repeat(PINF, num_vertices)

    -- Array used to indicate if vertex is in MST. Indicate nothing in MST yet
    sequence mst_set = repeat(FALSE, num_vertices)

    -- Include first vertex in MST
    keys[1] = 1

    -- The MST will include all vertices
    for i = 1 to num_vertices - 1
    do
        -- Pick index of the minimum key value not already in MST
        integer u = find_min_key(keys, mst_set)

        -- Add picked vertex to MST set
        mst_set[u] = TRUE

        -- Update key values and parent indices of picked adjacent
        -- vertices. Only consider vertices not yet in MST
        for j = 1 to length(graph[u])
        do
            integer v = graph[u][j][NODE_INDEX]
            integer graph_value = graph[u][j][NODE_WEIGHT]
            if not mst_set[v] and graph_value < keys[v]
            then
                parents[v] = u
                keys[v] = graph_value
            end if
        end for
    end for

    -- Construct MST information to return
    sequence mst = {}

    -- Skip over root and adjust vertex numbers to account for 1-based indexing
    for k = 2 to num_vertices
    do
        mst &= {{parents[k] - 1, k - 1, keys[k]}}
    end for

    return mst
end function

-- Find vertex with minimum key values not already in MST
function find_min_key(sequence keys, sequence mst_set)
    atom min_value = PINF
    integer min_index
    for v = 1 to length(keys)
    do
        if keys[v] < min_value and not mst_set[v]
        then
            min_value = keys[v]
            min_index = v
        end if
    end for

    return min_index
end function

-- Get total MST weight
function get_total_mst_weight(sequence mst)
    return sum(vslice(mst, MST_WEIGHT))
end function

-- Check command-line arguments
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Parse 1st command-line argument and make sure number of values is a square
sequence list_result = parse_int_list(argv[4])
sequence weights = list_result[PARSE_INT_LIST_VALUES]
integer num_weights = length(weights)
integer sqrt_num_weights = round(sqrt(num_weights))
if (
    not list_result[PARSE_INT_LIST_VALID]
    or num_weights != sqrt_num_weights * sqrt_num_weights
)
then
    usage()
end if

-- Create graph from weights
sequence graph = create_graph(weights, sqrt_num_weights)

-- Get MST using Prim's algorithm
sequence mst = prim_mst(graph)

-- Calculate total weight of MST and display
integer total_weight = get_total_mst_weight(mst)
printf(STDOUT, "%d\n", total_weight)
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [Obfuscation Techniques: Magic Numbers](https://therenegadecoder.com/code/obfuscation-techniques-magic-numbers/)
- :computer: [Obfuscation Techniques: No More Type Hints](https://therenegadecoder.com/code/obfuscation-techniques-no-more-type-hints/)
- :computer: [Obfuscation Techniques: Visually Similar Characters](https://therenegadecoder.com/code/obfuscation-techniques-visually-similar-characters/)
- :computer: [Obfuscation Techniques: Shadowing Built-in Functions](https://therenegadecoder.com/code/obfuscation-techniques-shadowing-built-in-functions/)
- :computer: [Obfuscation Techniques: Writing Malicious Comments](https://therenegadecoder.com/code/obfuscation-techniques-writing-malicious-comments/)
- :computer: [Obfuscation Techniques: The Yoda Conditional](https://therenegadecoder.com/code/obfuscation-techniques-the-yoda-conditional/)
- :apple: [Students Should Be Able to Build a Portfolio From Their Coursework](https://therenegadecoder.com/teach/students-should-be-able-to-build-a-portfolio-from-their-coursework/)
- :apple: [Why I’m No Longer Giving Paper Exams in My Computer Science Courses](https://therenegadecoder.com/teach/why-im-no-longer-giving-paper-exams-in-my-computer-science-courses/)
- :black_nib: [Make TODO Lists More Meaningful By Reflecting on Your Values](https://therenegadecoder.com/blog/make-todo-lists-more-meaningful-by-reflecting-on-your-values/)
- :black_nib: [Speed Up Your Data Structures With Hashing](https://therenegadecoder.com/blog/speed-up-your-data-structures-with-hashing/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-11-17 using [SnakeMD](https://www.snakemd.io).