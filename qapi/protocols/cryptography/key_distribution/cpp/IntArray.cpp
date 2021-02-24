#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

class IntArray {
    public:
        /*
          General utilities
        */
        void free_addr(int* addr) {
          delete [] addr;
        }

        /* 
          Specific use-cases
        */

        void set_time_based_random_seed() {
          srand(time(0)); // Should only be done once per program
        }

        int* generate_random_bit_array(int size) {
          // Allocates new memory so must be freed
          int* random_array = new int[size];
          for (int i = 0; i < size; i++) {
            try
            {
              std::random_device rd;
              random_array[i] = rd() % 2;
            } catch(...)
            {
              random_array[i] = rand() % 2;
            }
          }
          return random_array;
        }
};

extern "C" {
  IntArray* IntArray_new() { 
    return new IntArray(); 
  }

  void IntArray_free(IntArray* arr, int* addr) {
    arr->free_addr(addr);
  }

  void IntArray_generate_random_bit_array(IntArray* arr, int size) {
    arr->generate_random_bit_array(size);
  }

  void IntArray_set_time_based_random_seed(IntArray* arr) {
    arr->set_time_based_random_seed();
  }

  void self_destruct(IntArray* arr) {
    delete arr;
  }
}
