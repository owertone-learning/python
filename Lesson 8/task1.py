class Data:
    def __init__(self, data_str):
        self.data_str = data_str

    @staticmethod
    def data_int(np):
        data = list(map(int, np.split('-')))
        return f'{data[0]}.{data[1]}.{data[2]}'

    @classmethod
    def data_correction(cls, local_data):
        local_data = list(map(int, local_data.split('-')))
        if local_data[0] > 31:
            raise DataCheck(local_data[0])
        elif local_data[1] > 12:
            raise DataCheck(local_data[1])
        elif local_data[2] > 2022:
            raise DataCheck(local_data[2])
        else:
            return cls(local_data)


class DataCheck(Exception):
    def __init__(self, l_date):
        self.l_date = l_date

    def __str__(self):
        print(self.l_date)
        return f'{self.l_date}'


my_data = '30-12-2022'
try:
    new_data = Data.data_correction(my_data)
    print(Data.data_int(my_data))
except DataCheck as f:
    print(f'получены неверные данные: {f.l_date}')
