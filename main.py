# main.py
from agents.concierge import ConciergeAgent

def main():
    agent = ConciergeAgent()
    print("Welcome to Concierge Booking Agent (Demo Mode)")
    print("Type 'exit' to quit. Try: 'I want to book a doctor visit' or 'Book salon for me at 1 PM'")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit","quit"):
            print("Goodbye!")
            break
        print("Agent:", agent.handle_user(user_input))

if __name__=='__main__':
    main()
