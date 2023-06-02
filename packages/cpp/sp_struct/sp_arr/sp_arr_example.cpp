#include <iostream>
#include <sstream>
#include "arr.h"

using namespace std;

struct Student {
    std::string name;
    int standard;
};
std::ostream& operator <<(std::ostream& os, const Student& s) {
    return (os << "[" << s.name << ", " << s.standard << "]");
}

int main(int argc, const char * argv[]) {
    int nStudents;
    cout << "1반 학생 수를 입력 하슈";
    cin >> nStudents;
    
    dynamic_array<Student> classOne(nStudents);
    for (int i = 0 ; i  < nStudents; i++) {
        string name;
        int standart;
        cout << i + 1 << "번째 학생의 이름과 나이를 입력하슈";
        cin >> name >> standart;
        classOne[i] = Student{name, standart};
    }
    
    try {
        classOne.at(nStudents) = Student{"SP", 27};
    } catch (...) {
        cout << "예외 바를생~!!"<< endl;
    }
    
    // Deep Copy
    auto classTwo = classOne;
    cout << "Copy From ClassOne: " << classTwo.to_string() << endl;
    
    auto classThree = classOne + classTwo;
    cout << "Merge With Class One and Two: " << classThree.to_string() << endl;
    
    return 0;
}
