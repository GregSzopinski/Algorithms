public class Solution {
    Dictionary<int, int> fibCache = new Dictionary<int, int>();

    public int Fib(int N)
    {
        int value;
        if (fibCache.ContainsKey(N))
        {
            return fibCache[N];
        }
        else if ((N == 0) || (N == 1))
        {
            value =  N;
        }
        else
        {
            value = Fib(N -1) + Fib(N - 2);
        }
        fibCache[N] = value;
        return value;
    }
}