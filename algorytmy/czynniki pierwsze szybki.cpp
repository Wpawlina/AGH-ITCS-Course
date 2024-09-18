#include <iostream>
#include <cmath>
#include <time.h>
#include <cstdlib>


using namespace std;


int main()
{
    int n;
    clock_t start,stop;
    cout<<"Podaj liczbe"<<endl;
    cin >> n;
    start=clock();
    for(int i=2;i<=sqrt(n);i++)
    {
        while(n%i==0)
        {
            cout << i << endl;
            n=n/i;
        }
    }
    if(n>1)
    {

        cout << n<<endl;
    }
    stop=clock();
    double czas=(double)(stop - start)/CLOCKS_PER_SEC;
    cout << "Czas wykonania: "<< czas;
}
