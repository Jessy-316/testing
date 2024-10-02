import pickle

# Serializing a dictionary
data = {"name": "John", "age": 30, "city": "New York"}

with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

# Deserializing the data
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)
