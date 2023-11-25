def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return[badge_maker(name) for name in names]
# batch_badge_creator(["Arel", "Carol"])

def assign_rooms(names):
    rooms = range(1,8)
    return [f"Hello, {name}! You'll be assigned to room {room}!" for name, room in zip(names, rooms)]
       
# assign_rooms(["Arel", "Carol","Arel", "Carol","Arel", "Carol"])
def printer(names):
    x= f"{batch_badge_creator(names) + assign_rooms(names)}"
    print(x)
printer(["Arel", "Carol"])  