import Tag
import TagList
import Task

def main():
    house = Tag.Tag("house", 3)
    master_tag_list = TagList.TagList(house)
#    print(master_tag_list)

    dishes = Task.Task(0, "do the dishes #house #chores", master_tag_list)

    print("initialize with dishes and chores")
    print(dishes)
#    print(dishes.master_tag_list)
#    print(master_tag_list)

    dishes.add_tags("a b c d")
    print()
    print("add a b c d")
    print(dishes)

    dishes.remove_tags("a b c d")
    print()
    print("remove a b c d")
    print(dishes)

    threat_level_midnight = Tag.Tag("threat_level_midnight", 5)
    master_tag_list.append(threat_level_midnight)
    print()
    print("add threat_level_midnight to master_tag_list")
    print("master_tag_list")
    print(master_tag_list)
    print("dishes")
    print(dishes)

    dishes.add_tags("threat_level_midnight")
    print()
    print("add threat_level_midnight to dishes")
    print(dishes)

    dishes.remove_tags("threat_level_midnight")
    print()
    print("remove threat_level_midnight from dishes")
    print(dishes)

if __name__ == "__main__":
    main()
