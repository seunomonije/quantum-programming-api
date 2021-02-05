#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

class Playground {
  public:
    /*
      Functions to play around with
    */
    void respond(){
        std::cout << "This is from C++!" << std::endl;
    }

    int* return_123(){
      // Allocates new memory so must be freed
      int* arr = new int[3] {1, 2, 3};
      return arr;
    }

    void print_int(int integer) {
      std::cout << integer << std::endl;
    }

    void free_addr(int* addr) {
      delete [] addr;
    }

};

extern "C" {
 Playground* Playground_new() {
   return new Playground();
 }

 void Playground_respond(Playground* playground) { 
    playground->respond(); 
  }

  void Playground_return_123(Playground* playground) {
    playground->return_123();
  }

  void Playground_print_int(Playground* playground, int integer) {
    playground->print_int(integer);
  }
  
  void Playground_free_addr(Playground* playground, int* addr) {
    playground->free_addr(addr);
  }

  void self_destruct(Playground* playground) {
    delete playground;
  }
}