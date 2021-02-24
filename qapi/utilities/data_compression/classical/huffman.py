import os
import heapq

class HeapNode:
  def __init__(self, char, frequency):
    self.char = char
    self.frequency = frequency
    self.left = None
    self.right = None

  def __lt__(self, other):
    return self.frequency < other.frequency

  def __eq__(self, other):
    if other == None:
      return False
    elif not isinstance(other, HeapNode):
      return False
    
    return self.frequency == other.frequency

class HuffmanCoding:
  def __init__(self, file_path):
    self.file_path = file_path
    self.heap = []
    self.codes = {}
    self.reverse_codes = {}

  def compress(self):
    filename, file_extension = os.path.splitext(self.file_path)
    output_path = filename + '.bin'

    with open(self.file_path, 'r+') as file, open(output_path, 'wb') as output:
      text = file.read().rstrip() # Trim whitespace

      frequency_map = self._create_frequency_map(text)
      self._make_heap(frequency_map)
      self._merge_codes()
      self._make_codes()

      encoded_text = self._get_encoded_text(text)
      padded_encoded_text = self._pad_encoded_text(encoded_text)

      encoded_bytes = self._get_byte_array(padded_encoded_text)
      output.write(bytes(encoded_bytes))

    print ("Compressed successfully")
    return output_path

  def decompress(self, input_path):
    filename, file_extension = os.path.splitext(input_path)
    output_path = filename + '_decompressed.txt'

    with open(input_path, 'rb') as file, open(output_path, 'w') as output:
      bit_string = ''

      byte = file.read(1)
      while(len(byte) > 0):
        byte = ord(byte)
        bits = bin(byte)[2:].rjust(8, '0') # removes 0b, and rjust puts it in 8 bits
        bit_string += bits
        byte = file.read(1)
      
      encoded_text = self._remove_padding(bit_string)
      decoded_text = self._decode_text(encoded_text)
      output.write(decoded_text)

    print("Decompressed")
    return output_path

  """
  COMPRESSION
  """
  def _create_frequency_map(self, text):
    frequency_map = {}
    for character in text:
      if not character in frequency_map:
        frequency_map[character] = 0
      frequency_map[character] += 1

    return frequency_map

  def _make_heap(self, frequency_map):
    for key in frequency_map:
      node = HeapNode(key, frequency_map[key])
      heapq.heappush(self.heap, node)  
    return

  def _merge_codes(self):
    while len(self.heap) > 1:
      first_node = heapq.heappop(self.heap)
      second_node = heapq.heappop(self.heap)

      merged_frequency = first_node.frequency + second_node.frequency

      merged_node = HeapNode(None, merged_frequency)
      merged_node.left = first_node
      merged_node.right = second_node

      heapq.heappush(self.heap, merged_node)
    return

  def _build_codestring(self, node, current_code):
    if node == None:
      return

    if node.char != None:
      self.codes[node.char] = current_code
      self.reverse_codes[current_code] = node.char
      return

    self._build_codestring(node.left, current_code + '0')
    self._build_codestring(node.right, current_code + '1')

  def _make_codes(self):
    root = heapq.heappop(self.heap)
    current_code = ''
    self._build_codestring(root, current_code)
  
  def _get_encoded_text(self, text):
    encoded_text = ''
    for character in text:
      encoded_text += self.codes[character]
    return encoded_text

  def _pad_encoded_text(self, encoded_text):
    padding = 8 - len(encoded_text) % 8
    for _ in range(padding):
      encoded_text += '0'
    
    padded_info = '{0:08b}'.format(padding)
    encoded_text = padded_info + encoded_text
    return encoded_text
  
  def _get_byte_array(self, padded_encoded_text):
    if(len(padded_encoded_text) % 8 != 0):
      print('Encoded text not padded properly')
      exit(0)

    b_array = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
      byte = padded_encoded_text[i:i+8]
      b_array.append(int(byte, 2))
    return b_array

  """
  DECOMPRESSION
  """
  def _remove_padding(self, bit_string):
    padded_info = bit_string[:8]
    extra_padding = int(padded_info, 2)

    bit_string = bit_string[8:]
    encoded_text = bit_string[:-1*extra_padding]

    return encoded_text

  def _decode_text(self, encoded_text):
    current_code = ''
    decoded_text = ''

    for bit in encoded_text:
      current_code += bit
      if current_code in self.reverse_codes:
        character = self.reverse_codes[current_code]
        decoded_text += character
        current_code = ''
    
    return decoded_text

def main():
  path = './sample.txt'
  H = HuffmanCoding(path)
  H.compress()
  path = './sample.bin'
  H.decompress(path)

  return

if __name__ == '__main__':
  main()
