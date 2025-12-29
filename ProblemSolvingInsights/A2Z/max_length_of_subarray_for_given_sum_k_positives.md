
## Largest subarray with given sum k (positives)


```cpp
int subarraySumPositive(vector<int>& nums, int k) {
    int st = 0, sum = 0, maxLen = 0;

    for (int ed = 0; ed < nums.size(); ed++) {
        sum += nums[ed];

        while (sum > k) {
            sum -= nums[st];
            st++;
        }

        if (sum == k) {
            maxLen = max(maxLen, ed - st + 1);
        }
    }

    return maxLen;
}

```
