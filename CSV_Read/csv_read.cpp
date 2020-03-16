#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
using namespace std;

int main() {
    //cout<<"test";
    ifstream input_file("test_data.csv");
    string desiredColumn = "Annual Income (k$)";//Enter desired column here

    if (!input_file) {        
        cout << "Error: Cannot open file." << endl;        
        return 1;    
    }    
    string line,colname;
    
    getline(input_file, line);//Gets first row of column names
    stringstream ss(line);
    vector<string> colNames;
    int colIndex = -1;
    int i = 0;
    while(getline(ss, colname, ',')){//Stores column names in ColNames vector
        colNames.push_back(colname);
        if(colname==desiredColumn){
            colIndex = i;//Index we want
        }
        i++;
    }
    if(colIndex == -1){
        cout<<"Column not found nice typing."<<endl;
        return -1;
    }
    vector<vector<string>> vec2;
    vector<string> vec1;
    vec1.push_back("1");
    vec1.push_back("2");
    //cout<<vec1[0];
    vec2.push_back(vec1);
    //cout<<vec2[0][1]<<endl;

    vector<vector<string>> fullVec;
    try {        
        string data;
        while(getline(input_file, line)){
            int i = 0;
            stringstream st(line);
            vector<string> dataVec;
            while(getline(st, data, ',')){
                if(i==colIndex ||i==colIndex+1){//change the second param to whatever other index you want
                    dataVec.push_back(data);//The pair array of the two datas
                }
                i++;
            }
            fullVec.push_back(dataVec);
            dataVec={};
        }
        //close the file.        
        input_file.close();    
    } catch (const ifstream::failure &f) {        
        cout << "Error: An I/O error occurred.";        
        return 1;    
    }
    cout<<fullVec[0][0]<<", "<<fullVec[0][1]<<endl;//Example output 15, 39
    return 0;
}
