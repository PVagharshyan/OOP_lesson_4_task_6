from publication import Publication

class Tape(Publication):
    def __init__(self, v_title: str, v_price: float, v_playing_time: float) -> None:
        super().putdata(v_title, v_price)
        self._playing_time = v_playing_time

    def getdata(self) -> dict:
        result_dict = {
            "playing_time" : self._playing_time
        }
        result_dict = { **result_dict, **super().getdata() }
        return result_dict

    def putdata(self, v_title: str, v_price: float, v_playing_time: float) -> None:
        super().putdata(v_title, v_price)
        self._playing_time = v_playing_time
