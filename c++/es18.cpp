#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){

    ifstream file;
    file.open("es18.txt");

    int** triangle = new int*[15];

    for (int i=0; i<15; i++){
        triangle[i] = new int[i+1];
    }

    for (int i=0; i<15; i++){
        for(int j=0; j<i+1;j++){
            file >> triangle[i][j];
        }
    }
    
    for (int i=0; i<15; i++){
        for(int j=0; j<i+1;j++){
            cout << triangle[i][j];
        }
        cout << endl;
    }
    
    for (int i=0; i<15; i++){
        delete [] triangle[i];
    }

    delete [] triangle;

    return 0;
}