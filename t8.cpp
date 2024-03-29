// made by Esteban Santacruz (https://github.com/Jestebansamt)

#include <bits/stdc++.h>

using namespace std;


vector<int> vecB;
void generateBinary(int n, string& binary, int index) {
    if (index == n) {
        string currentB = "0";
        bool cvan = 0;
        for(int i = 0; i <6; ++i){
            if(cvan = 0 && binary[i] == 1){
                cvan = 1;
                currentB[0] = 1;
            }
            if(cvan = 1){
                currentB+= binary[i];
            }
        }
        vecB.push_back(stoi(currentB));
        return;
    }
    binary[index] = '0';
    generateBinary(n, binary, index + 1);
    binary[index] = '1';
    generateBinary(n, binary, index + 1);
}


int main(){
    freopen("std.in", "r", stdin);
    freopen("std.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    string binary="000000";
    generateBinary(6, binary, 0);

    int t; cin >> t;
    int q = t;
    while(t--){
        int n; cin >> n;
        int qn = n;
        while(true){
            bool van = false;
            for(int i = vecB.size()-1; i >= 3; --i){
                int m = vecB[i];
                if(n % m == 0){
                    n /= m;
                    van = true;
                }
            }
            if(van == false || n == 1){
                break;
            }
        }
        while(true){
            bool van2 = false;
            for(int i = 2; i <= vecB.size(); ++i){
                int m = vecB[i];
                if(qn % m == 0){
                    qn /= m;
                    van2 = true;
                }
            }
            if(van2 == false || qn == 1){
                break;
            }
        }
        cout << ((n == 1 || qn == 1) ? "YES" : "NO") << "\n";       
    }




    return 0;
}
