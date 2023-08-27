class Publication:
    def __init__(self, v_title: str, v_price: float) -> None:
        self._title = v_title
        self._price = v_price

    def getdata(self) -> dict:
        result_dict = { "title" : self._title, "price" : self._price }
        return result_dict

    def putdata(self, v_title: str, v_price: float) -> None:
        self._title = v_title
        self._price = v_price

