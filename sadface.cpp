#include <iostream>
#include <cstdlib>
#include <fstream>
#include <windows.h>

using namespace std;

int main(){
    HANDLE hConsole;
    hConsole = GetStdHandle (STD_OUTPUT_HANDLE);

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
                    c=238;
                    SetConsoleTextAttribute(hConsole, c);
                }
                if(getcontent[i]=='w'){
                    c=255;
                    SetConsoleTextAttribute(hConsole, c);
                }

                cout << getcontent[i];
                c=0;
                SetConsoleTextAttribute(hConsole, c);
            }
            cout<<endl;
        }
    }
    c=15;
    SetConsoleTextAttribute(hConsole, c);
    return 0;
}
