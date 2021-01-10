class IBMQHandler:
  """
    NOTE: Make sure to install python SSL cerfiicates or you will not be able to access IBMQ
  """
  def __init__(self, API_KEY):
    # Connect to the IBMQ Experience to allow use of real quantum computers
    IBMQ.enable_account(API_KEY)

    # Initialize simulator for use as well
    self.simulatorBackend = Aer.get_backend('qasm_simulator')

  """
    Traverses through all providers associated with the current IMBQ account
    and selects the backend object associated with a provided device name.
    PARAMS:
      deviceName : String -> name of the IBMQ backend object
  """
  def select_device(self, deviceName):
    # Searches all providers, in most cases there will only be one
    backend = None
    for provider in IBMQ.providers():
      for potential_backend in provider.backends():
        if potential_backend.name() == deviceName:
          backend = potential_backend

    if backend:
      self.currentDeviceName = deviceName
      self.currentBackend = backend
    else:
      raise InvalidDeviceException("Given device name was unable to be accessed, or is wrong.")
  
  """
    Returns the IBMQ backend object for whenever needed.
  """
  def use_real_device(self):
    return self.currentBackend

  """
    Returns the simulator backend object for whenever needed.
  """
  def use_simulator(self):
    return self.simulatorBackend

  """
    Writes output results to file
  """
  def write_results_to_file(self, results):
    with open(f'results/raw_results_{self.currentDeviceName}.txt', 'w') as file:
      file.write(str(results))