from tools.booking_tool import make_booking
class BookingAgent:
    def book(self,name,kind,time):
        return make_booking(name,kind,time)
