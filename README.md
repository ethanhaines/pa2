
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