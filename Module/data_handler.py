from collections import deque

class DataHandler:
    def load_data(self, file_path):
        with open(file_path, "r") as Data_File:
            for line in Data_File.readlines():
                data_deque = deque(line.strip().split("/"))
        
        return data_deque
    
    def write_data(self, file_path, read_write_mode, write_data):
        try:
            with open(file_path, read_write_mode, encoding="utf8") as Data_File:
                Data_File.write(write_data)
        except IOError:
            print("\n============\nAn error occurred while writing to the file.\n============\n")
            
    def write_file(self, file_path, read_write_mode, write_file):
        try:
            with open(file_path, read_write_mode) as Data_File:
                Data_File.write(write_file)
        except IOError:
            print("\n============\nAn error occurred while writing to the file.\n============\n")
            
            