## Student Info and Instructions

Ethan Haines

35007385

To run, use the following command:

```bash
python src/cache.py data/example.in data/example.out
```

Where example.in and example.out are the input and output files respectively. Three other input files are provided: 1.in, 2.in, and 3.in.

The only assumptions are that files are formatted correctly and k >= 1.

## Question 1
Input File| k | m | FIFO misses| LRU misses| OPTFF misses|
:----| :---: | :---: | :---: | :---: | :---: |
| 1.in | 3 | 60 | 48 | 49 | 34 |
| 2.in | 4 | 56 | 52 | 50 | 31 |
| 3.in | 5 | 64 | 62 | 62 | 37 |
 - OPTFF Does have the fewest misses across the board.
 - LRU performed ever so slightly better (1 less overall miss) but both are very close.
 
## Question 2

Yes, there is a sequence that exists for which OPTFF incurs strictly fewer misses than LRU. The sequence below is one.

```
1 2 3 4 1
```

The miss counts for this sequence are:
- OPTFF: 4 misses
- LRU: 5 misses

After the first three requests, the cache becomes full, then on request 4, all three policies need to evict something. LRU and FIFO would both evict 1, but OPTFF looks ahead and sees that 1 will be used again, so it evicts either 2 or 3. Finally, it arrives at 1, and under LRU and FIFO this would be a miss, but under OPTFF it would be a hit.

This shows that OPTFF can incur strictly fewer misses than LRU for certain sequences since it uses future knowledge to avoid eviction of a request that will be needed soon.

## Question 3
Let A be any offline algorithm that knows the whole request sequence ahead of time. I will show that OPTFF never has more misses than A on the same sequence.

Suppose there is some optimal offline algorithm S that does not always make the same eviction choice as OPTFF. Look at the first step where they differ. At that step, both algorithms have seen the same requests so far, so they have the same cache contents before the eviction.

Now say the requested item is not in cache. OPTFF evicts item e, while S evicts item f. Since OPTFF is farthest-in-future, that means e is needed later than f, or maybe e is never needed again at all. So keeping f in the cache instead of e cannot be worse, because f will be useful at least as soon as e would be.

Because of that, we can modify S so that at this step it evicts e instead of f, and then continue following S afterward. This change does not increase the number of misses. So we get another optimal algorithm that agrees with OPTFF for one more step.

Repeating this argument again and again, we can transform an optimal offline algorithm into one that makes the exact same eviction choices as OPTFF on the whole sequence, without increasing misses. That means OPTFF is also optimal.

So for any fixed request sequence,

```text
misses(OPTFF) <= misses(A)
```

for every offline algorithm A.
