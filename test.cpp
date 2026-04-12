#include <iostream>
#include<cmath>
using namespace std;
int main() {
    float n;
    n = 60 * 60*24*1. / 365;
    cout<<n<<endl;
    for (int i = 0; i <= 24*60*60; i++)
    {
        if(abs(i - (n*(363+(i/(60*60*24)))))<= 1)
            cout<< i/(60*60)*1. << " " << i % (60*60)<<endl;
    }
    return 0;
}