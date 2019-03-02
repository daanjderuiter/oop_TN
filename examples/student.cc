#include <string> 
using namespace std;

class Student {


  public:
    Student(string name, string student_id, string programme) 
      : name(move(name)), student_id(move(student_id)), programme(move(programme))
    {};

    string association() {
      return associations.at(name);
    }

    string programme;
    string student_id;
    string programme;

    std::unordered_map<string, string> associations = ...;

};
