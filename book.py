from publication import Publication


class Book(Publication):
    def __init__(self, v_title: str, v_price: float, v_page_cout: int) -> None:
        super().putdata(v_title, v_price)
        self._page_count = v_page_cout

    def getdata(self) -> dict:
        result_dict = {
            "page_count" : self._page_count
        }
        result_dict = { **result_dict, **super().getdata() }
        return result_dict

    def putdata(self, v_title: str, v_price: float, v_page_cout: int) -> None:
        super().putdata(v_title, v_price)
        self._page_count = v_page_cout
