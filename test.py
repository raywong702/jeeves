import tag
import tag_list
import task

def main():
    house = tag.tag('house', 3)
    master_tag_list = tag_list.tag_list(house)
#    print(master_tag_list)

    dishes = task.task(0, "do the dishes #house #chores", master_tag_list)

    print(dishes)
    print(dishes.master_tag_list)
    print(master_tag_list)

if __name__ == "__main__":
    main()
