class Publication:
    def __init__(self) -> None:
        self.putdata()

    def getdata(self) -> dict:
        result_dict = { "title" : self._title, "price" : self._price }
        return result_dict

    def putdata(self) -> None:
        v_title = input("input title: ")
        self._title = v_title
        while True:
            try:
                v_price = input("input price: ")
                v_price = float(v_price)
                break
            except ValueError as err:
                print(err)
        self._price = v_price

