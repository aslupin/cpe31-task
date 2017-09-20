using namespace std;
int #include <iostream>

int main(){
int date=0;
int max = -9999;
int max_pos = 0;
int min = 9999;
int min_pos = 0;
int n=0;

cin >> n;
for(int i=0;i<n;i++){
        cin >> date;
        if(date > max){
            max = date;
            max_pos = i;
        }
        if(date < min){
            min = date;
            min_pos = i;
        }
    }
    cout <<  max_pos << " " << min_pos; 

}