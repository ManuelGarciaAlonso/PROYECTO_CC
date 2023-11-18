class UserProfile:
    def __init__(self, username, skills, experience):
        self.username = username
        self.skills = skills
        self.experience = experience
        self.services_offered = []
        self.received_ratings = []

    def add_service(self, service):
        self.services_offered.append(service)

    def remove_service(self, service):
        self.services_offered.remove(service)

    def receive_rating(self, rating):
        self.received_ratings.append(rating)

class Service:
    def __init__(self, name, description, price, provider, category, available=True):
        self.name = name
        self.description = description
        self.price = price
        self.provider = provider
        self.category = category
        self.available = available
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

class Rating:
    def __init__(self, reviewer, score, review, service):
        self.reviewer = reviewer
        self.score = score
        self.review = review
        service.add_rating(self)

class Transaction:
    def __init__(self, buyer, seller, service, amount):
        self.buyer = buyer
        self.seller = seller
        self.service = service
        self.amount = amount
        self.status = "Pending"

    def complete_transaction(self):
        self.status = "Completed"

class Chat:
    def __init__(self, user1, user2):
        self.participants = [user1, user2]
        self.messages = []

    def send_message(self, sender, message):
        self.messages.append((sender, message))

    def get_latest_message(self):
        return self.messages[-1] if self.messages else None

class ServiceMarketplace:
    def __init__(self):
        self.users = []
        self.services = []

    def register_user(self, user):
        self.users.append(user)

    def add_service(self, service):
        self.services.append(service)

    def search_services(self, filter_criteria):
        filtered_services = [service for service in self.services if self._matches_filter(service, filter_criteria)]
        return filtered_services

    def _matches_filter(self, service, filter_criteria):
        for key, value in filter_criteria.items():
            if key == "category" and service.category != value:
                return False
            if key == "price":
                price_limit = float(value.lstrip('<='))
                if service.price > price_limit:
                    return False
            if key == "available" and service.available != value:
                return False
        return True

    def rate_service(self, service, rating):
        service.add_rating(rating)

    def create_transaction(self, buyer, seller, service, amount):
        transaction = Transaction(buyer, seller, service, amount)
        return transaction

    def start_chat(self, user1, user2):
        chat = Chat(user1, user2)
        return chat
