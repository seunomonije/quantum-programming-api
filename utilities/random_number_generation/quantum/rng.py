import random
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, Aer

"""
IMPROVEMENTS
  - figure out an easier for way for people to see the results rather than
    having to access public variable result
"""
class QuantumCoinFlip: # Maybe change this name later to something more generic as we refactor code
  def __init__(self):
    self.result = self.generate_random_flip()

  def generate_random_flip(self):
    registers = self._build_registers()
    circuit = self._build_circuit(registers)
    counts = self._run_circuit(circuit)
    converted_output = self._convert_counts(counts)

    return converted_output # Sloppy, leaving for now

  def print_counts(self, converted_output):
    print(converted_output)

  def _build_registers(self, register_size=1):
    # not ready for register_size != 1 yet
    return (QuantumRegister(register_size), ClassicalRegister(register_size))

  def _build_circuit(self, registers):
    quantum_register = registers[0]
    classical_register = registers[1]

    circuit = QuantumCircuit(quantum_register, classical_register)
    circuit.h(quantum_register[0]) #Hadamard on 0th bit of register
    circuit.measure(quantum_register, classical_register) 

    return circuit

  def _run_circuit(self, circuit):
    backend = Aer.get_backend('qasm_simulator')

    job_simulation = execute(circuit, backend, shots=1)
    result = job_simulation.result()
    counts = result.get_counts(circuit) #get_counts() returns either a dict or list of dicts

    return counts

  def _convert_counts(self, counts):
    counts = dict(counts) # Hard coding as a dict for now since qiskit is sloppy
    if type(counts) is list:
      raise Exception('Unimplemented')
    elif type(counts) is dict:
      key_list = list(counts)
      for key in key_list:
        return int(key) # Broken implementation, only doing this for one case
    else:
      raise Exception('Invalid input in convert_counts')

flip = QuantumCoinFlip()
print(flip.result)
