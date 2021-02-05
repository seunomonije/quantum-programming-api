from ctypes import cdll
import ctypes

lib_playground = cdll.LoadLibrary('./cpp/libPlayground.so')
lib_int_array = cdll.LoadLibrary('./cpp/libIntArray.so')

"""
  Structure to offload computationally taxing problems to CPP.

  CURRENT ISSUES:
    - potential memory leaks/issues. Need to figure out how to diagnose.
"""
class CPPWrapper(object):
  lib = None
  obj = None

  def self_destruct(self):
    # Once you call this you can no longer use corresponding instance of class! 
    # Necessary for cleanup at end of program.
    # CURRENTLY BROKEN.
    self.lib.self_destruct(self.obj)

class Playground(CPPWrapper):
  lib = lib_playground
  def __init__(self):
    self.obj = self.lib.Playground_new()
    self.list_of_pointers = []
    
  def respond(self):
    return self.lib.Playground_respond(self.obj)

  def return_123(self):
    fn = self.lib.Playground_return_123
    fn.restype = ctypes.POINTER(ctypes.c_int * 3)
    array = fn(self.obj)
    self.list_of_pointers.append(array)

    result = [i for i in array.contents]
    return result

  def print_int(self, integer):
    # fn = lib.Foo_test
    # fn.argtypes = (ctypes.POINTER(ctypes.py_object), ctypes.POINTER(ctypes.c_int))
    return self.lib.Playground_print_int(self.obj, integer)

  def free_allocated_memory(self):
    for pointer in self.list_of_pointers:
      self.lib.Playground_free_addr(self.obj, pointer)

class IntArray(CPPWrapper):
    lib = lib_int_array
    def __init__(self):
        self.obj = self.lib.IntArray_new()
        self.list_of_pointers = []

    def free_allocated_memory(self):
      for pointer in self.list_of_pointers:
        self.lib.IntArray_free(self.obj, pointer)

    def generate_random_bit_array(self, size):
      fn = self.lib.IntArray_generate_random_bit_array
      fn.restype = ctypes.POINTER(ctypes.c_int * size)
      array = fn(self.obj, size)
      self.list_of_pointers.append(array)

      result = [i for i in array.contents]
      return result