#include <iostream>
#include <cstdlib>
#include <fstream>
#include <windows.h>

using namespace std;

int main(){
    HANDLE hConsole;
    hConsole = GetStdHandle (STD_OUTPUT_HANDLE);

    string getcontent;
    ifstream fin("gladface1.txt");
    int c;
    if(fin.is_open())
    {
        while(! fin.eof())
        {
            fin >> getcontent;
            for(int i=0;i<70;i++)
            {
                if(getcontent[i]==':'){
                    c=238;
                    SetConsoleTextAttribute(hConsole, c);
                }
                if(getcontent[i]=='a'){
                    c=204;
                    SetConsoleTextAttribute(hConsole, c);
                }

                cout << getcontent[i];
                c=0;
                SetConsoleTextAttribute(hConsole, c);
            }
            cout<<endl;
        }
    }
}
