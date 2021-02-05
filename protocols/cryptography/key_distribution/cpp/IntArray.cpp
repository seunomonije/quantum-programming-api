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
        int* generate_random_bit_array(int size) {
          srand(time(0)); // Unconventional..should only be done once. Singleton?
          // Allocates new memory so must be freed
          int* random_array = new int[size];
          for (int i = 0; i < size; i++) {
            random_array[i] = rand() % 2;
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

  void self_destruct(IntArray* arr) {
    delete arr;
  }
}