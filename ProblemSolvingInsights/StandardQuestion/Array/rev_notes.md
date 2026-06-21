# Rev Notes for Array Based Problem

## Two Pointers

**3Sum**
- skip duplicates caused by i `if(i>0 and nums[i] == nums[i-1]) continue;`
- Don't forget to skip from both ends, after target has been found

**3Sum Closest**
- Similar to 3Sum, just keep track of minmum distance from target
- The condition to skip the duplicates in 3sum, need not be tracked, as we're just tracking the minimum distance from target

