public class Solution {
    public int Fib(int N)
    {
        if ((N == 0) || (N == 1))
        {
            return N;
        }
        else
        {
            return Fib(N -1) + Fib(N - 2);
        }
    }
}