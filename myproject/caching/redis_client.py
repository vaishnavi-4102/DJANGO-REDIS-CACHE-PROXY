import redis



def connect_client():
    return redis.StrictRedis(localhost="localhost", port = 6379, db=0)

if __name__ == "__main__":
    connect_client()