#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, n, m, l;
    cin >> t;

    while (t--)
    {
        cin >> n;
        if(n % 7 == 0) printf("%d \n",n);
        else
        {
            m = n % 7;
            l = n % 10;

            if (l - m > -1) printf("%d \n", n - m);
            else printf("%d \n", n + 7 - m);
            
        }
    }

    return 0;
    
}