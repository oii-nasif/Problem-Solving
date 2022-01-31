#include <iostream>
 
using namespace std;
 
int main() {
     int t;
     cin >> t;

    for (int i = 0; i < t; ++i) {
        string s;
        cin >> s;
        int zeros = 0, ones = 0;

        for (char i : s) {
            if (i == '1'){
                ones++;
            } 
            else{
                zeros++;
            }
        }
        if (zeros == ones){
            cout << zeros - 1 << endl;
        } else if (zeros < ones){
            cout << zeros << endl;
        } else if (zeros > ones){
            cout << ones << endl;
        }
    }

    return 0;
}