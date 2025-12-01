from tools.search_tool import search_availability
class SearchAgent:
    def search(self, kind:str):
        return search_availability(kind)
