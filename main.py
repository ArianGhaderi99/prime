import pandas as pd
import numpy as np

class Cache:
    def to_csv(self):
        primes = self.to_list()
        dataframe = pd.DataFrame(primes, columns=["Prime Numbers"])
        dataframe.to_csv("data.csv", index=False)

    def load_csv(self):
        try:
            data = pd.read_csv("data.csv")
            return data["Prime Numbers"].tolist()
        except FileNotFoundError:
            return []

    def to_list(self):
        raise NotImplementedError("Error .. This Method Only Use On Prime Class")

class Prime(Cache):
    def __init__(self, number: int):
        self.number = number
        self.__primes = []
        self.__start = 2

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError("Number Must Be Int-type")

        if value > 1:
            self.__number = value
        else:
            raise ValueError("Number Must Be Bigger than 1")

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start >= self.__number:
            raise StopIteration

        while True:
            flag = 0
            for div in range(2, int(self.__start**0.5) + 1):
                if self.__start % div == 0:
                    flag += 1
                    break
            if flag == 0:
                prime_number = self.__start
                self.__start += 1
                return prime_number
            self.__start += 1

    def __str__(self):
        return f"Prime Numbers: {self.to_list()}"

    def generator(self):
        sieve = np.ones(self.number, dtype=bool)
        sieve[:2] = False
        for i in range(2, int(self.number**0.5) + 1):
            if sieve[i]:
                sieve[i*i:self.number:i] = False
        for num in range(2, self.number):
            if sieve[num]:
                yield num

    def to_list(self):
        if not self.__primes:
            self.__primes = list(self.generator())
        return self.__primes


    def process(self):
        data = self.load_csv()
        if data:
            start = data[-1] + 1
        else:
            start = 2

        sieve = np.ones(self.new_number, dtype=bool)
        sieve[:2] = False
        for i in range(2, int(self.new_number**0.5) + 1):
            if sieve[i]:
                sieve[i*i:self.new_number:i] = False

        for num in range(start, self.new_number):
            if sieve[num]:
                yield num

    def collation(self, new_number):
        self.new_number = new_number
        new_data = list(self.process())

        dataframe = pd.DataFrame(new_data, columns=["Prime Numbers"])
        dataframe.to_csv("data.csv", mode='a', index=False, header=False)



if __name__ == "__main__":
    object1 = Prime(123456)
    object1.to_csv()
    object1.collation(1234567)
    object1.collation(12345678)
    object1.collation(123456789)
