import os
import sys

class Cache:
    def __init__(self, type: str, filename: str): # k >= 1
        self.type = type
        self.capacity = 0
        self.r_size = 0
        self.__memory = []
        self.__filename = filename
        self.__miss = 0
    
    

    def run(self):
        if self.type == "FIFO":
            return self.__FIFO()
        elif self.type == "LRU":
            return self.__LRU()
        elif self.type == "OPTFF":
            return self.__OPTFF()
        else:
            raise ValueError("Invalid cache type")
    
    def __FIFO(self):
        with open(self.__filename, 'r') as f:
            first_line = f.readline().strip()
            self.capacity = int(first_line.split()[0])
            self.r_size = int(first_line.split()[1])
            for line in f:
                line = line.strip()
                if line:
                    vals = line.split()
                    for val in vals:
                        if val in self.__memory:
                            continue

                        self.__miss += 1
                        if len(self.__memory) >= self.capacity:
                            self.__memory.pop(0)
                        self.__memory.append(val)
        return self.__miss
    
    def __LRU(self):
        with open(self.__filename, 'r') as f:
            first_line = f.readline().strip()
            self.capacity = int(first_line.split()[0])
            self.r_size = int(first_line.split()[1])
            for line in f:
                line = line.strip()
                if line:
                    vals = line.split()
                    for val in vals:
                        if val in self.__memory:
                            self.__memory.remove(val)
                            self.__memory.append(val)
                            continue

                        self.__miss += 1
                        if len(self.__memory) >= self.capacity:
                            self.__memory.pop(0)
                        self.__memory.append(val)
        return self.__miss
    
    def __OPTFF(self):
        requests = []
        with open(self.__filename, 'r') as f:
            first_line = f.readline().strip()
            self.capacity = int(first_line.split()[0])
            self.r_size = int(first_line.split()[1])
            for line in f:
                line = line.strip()
                if line:
                    requests.extend(line.split())

        for i in range(len(requests)):
            val = requests[i]
            if val in self.__memory:
                continue

            self.__miss += 1
            if len(self.__memory) < self.capacity:
                self.__memory.append(val)
                continue

            farthest_item = None
            farthest_index = -1
            future_requests = requests[i + 1:]

            for item in self.__memory:
                if item not in future_requests:
                    farthest_item = item
                    break

                next_index = future_requests.index(item)
                if next_index > farthest_index:
                    farthest_index = next_index
                    farthest_item = item

            self.__memory.remove(farthest_item)
            self.__memory.append(val)
        return self.__miss



def main():
    if len(sys.argv) < 2:
        raise ValueError("Usage: python src/cache.py <input_file> [output_file]")

    input_file = sys.argv[1]

    fifo_miss = Cache("FIFO", input_file).run()
    lru_miss = Cache("LRU", input_file).run()
    optff_miss = Cache("OPTFF", input_file).run()

    output = (
        f"FIFO  : {fifo_miss}\n"
        f"LRU   : {lru_miss}\n"
        f"OPTFF : {optff_miss}\n"
    )

    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
        with open(output_file, 'w') as f:
            f.write(output)
    else:
        print(output, end="")

if __name__ == "__main__":
    main()
