//  https://www.hackerrank.com/challenges/sum-numbers-c/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int n, m;
    float p, q;
    
    scanf("%d %d", &n, &m);
    scanf("%f %f", &p, &q);
	
    printf("%d %d\n", n + m, n - m);
    printf("%.1f %.1f\n", p + q, p - q); 
    
    return 0;
}