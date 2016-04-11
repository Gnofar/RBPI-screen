#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int main(){
    string getcontent;
    ifstream fin("sadface.txt");
    int c;
    if(fin.is_open())
    {
        while(! fin.eof())
        {
            fin >> getcontent;
            for(int i=0;i<70;i++)
            {
                if(getcontent[i]==':'){
                }
                if(getcontent[i]=='w'){
                }

                cout << getcontent[i];
            }
            cout<<endl;
        }
    }
    return 0;
}
