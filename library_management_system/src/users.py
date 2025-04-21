class User:
    def __init__(self, user_id: int, username: str, password: str, name: str, date_joined: date):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.name = name
        self.date_joined = date_joined

    def __repr__(self):
        return (f"User{{ID={self.user_id}, username='{self.username}', "
                f"name='{self.name}', joined={self.date_joined}}}")

def find_user_by_id(user_id: int, users) -> User:
    for u in users:
        if u.user_id == user_id:
            return u
    return None

def find_user_by_credentials(username: str, password: str, users) -> User:
    for u in users:
        if u.username == username and u.password == password:
            return u
    return None
