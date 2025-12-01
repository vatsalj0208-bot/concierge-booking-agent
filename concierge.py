from agents.search_agent import SearchAgent
from agents.booking_agent import BookingAgent
from tools.memory_tool import MemoryTool
from tools.logger import Logger

class ConciergeAgent:
    def __init__(self):
        self.search_agent = SearchAgent()
        self.booking_agent = BookingAgent()
        self.memory = MemoryTool()
        self.logger = Logger()

    def handle_user(self, text: str) -> str:
        self.logger.log({'agent': 'concierge', 'input': text})
        lower=text.lower()
        if 'book' in lower or 'reserve' in lower:
            if 'doctor' in lower: kind='doctor'
            elif 'salon' in lower: kind='salon'
            elif 'repair' in lower: kind='repair'
            else: kind='general'
            found_time=None
            for token in ['10 AM','1 PM','2 PM','4 PM','11 AM','3 PM']:
                if token.lower() in lower:
                    found_time=token
                    break
            if found_time:
                self.memory.set('last_preferred_time',found_time)
            avail=self.search_agent.search(kind)
            if found_time and found_time in avail:
                booking=self.booking_agent.book('Demo User',kind,found_time)
                return f"Booked {kind} at {found_time}. Booking ID: {booking['id']}"
            if avail:
                return f"I found these times for {kind}: {', '.join(avail)}. Reply with 'Book {kind} at <time>' to confirm."
            return f"Sorry, no availability found for {kind}."
        elif any(w in lower for w in ['remember','preference','last']):
            pref=self.memory.get('last_preferred_time')
            return f"I remember your last preferred time as: {pref}" if pref else "I don't have any saved preferences."
        return "I can help you search availability and make bookings. Say 'I want to book a doctor' to start."
