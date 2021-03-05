from ..Simulator import Simulator
from ..exceptions import *

from qiskit import Aer, execute

class QiskitSimulator(Simulator):
  def __init__(self, backend='qasm_simulator'):
    print(f'Active simulator: {backend}')

    try:
      self.backend = Aer.get_backend(backend)
    except:
      raise InvalidBackendError('Invalid backend name entered')
    