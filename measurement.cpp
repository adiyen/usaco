#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
using namespace std;

// bool same_cows()

bool comparison(int log[], string cow_change_name, int n) {
    string leading_cow;
    
}

int main() {
    ifstream fin("measurement.in");
    ofstream fout("measurement.out");

    int n;
    fin >> n;

    map<int, int> day_to_adding;
    map<int, string> days_to_cow;
    map<string, int> correspondence;
    int day, adding;
    int days[n];
    string cow;

    int log[3] = {7, 7, 7};
    correspondence["Bessie"] = 0;
    correspondence["Elsie"] = 1;
    correspondence["Mildred"] = 2;

    for(int i = 0; i < n; i++) {
        fin >> day >> cow >> adding;
        days[i] = day;
        days_to_cow[day] = cow;
        day_to_adding[day] = adding;
    }

    sort(days, days+n);

    // for (const auto& p : day_to_adding ) {
    //     std::cout << p.first << ' ' << p.second << endl;

    // }

    // for (const auto& p : days_to_cow) {
    //     std::cout << p.first << ' ' << p.second << endl;
    // }

    string cow_change_name;
    int adding_change;
    int count = 0;
    for(int i = 0; i < n; i++) {
        adding_change = day_to_adding[days[i]];
        cow_change_name = days_to_cow[days[i]];
        log[correspondence[cow_change_name]]+=adding_change;

        cout << cow_change_name << ' ' << log[correspondence[cow_change_name]] << endl;
    }
}