import datetime

class Handler:
  def get_backend(self):
    return self.current_backend

  def write_results_to_file(self, results):
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    with open(f'results/results_{time_stamp}.txt', 'w') as file:
      file.write(str(results))