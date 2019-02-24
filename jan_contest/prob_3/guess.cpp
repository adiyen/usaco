#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

vector<string> chars[100];
int num_counter(int i, int j) {
    vector<string> &a1 = chars[i], &a2 = chars[j];
    
    int counter = 0;
    for(int i = 0; i < a1.size(); i++){
        for(int j = 0; j < a2.size(); j++){
            if(a1[i] == a2[j]) {
                counter++;
            }
        }
    }
    return counter;
}


int main() {
    ifstream fin ('guess.in')
    int numb_ani;
    int numb_of_chars;
    string animal;
    fin >> numb_ani;

    for(int i = 0; i < numb_ani; i++) {
        list_arr = [];

        fin >> animal >> numb_of_chars;
    } 
}