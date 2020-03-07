import pickle
import datetime
import sys



class Todo:
    def __init__(self, todo, todo_id, status="not complete"):
        self.todo = todo
        self.status = status
        self.todo_id = todo_id
        self.time_date = datetime.datetime.now()
        self.complete_time = status

    def search_b(self, string_item):
        if string_item in search_in:
            return True
        else:
            return False


class Container:
    def __init__(self):
        self.container = []
        self.filename = ""
        self.todo_id = 0

    def add_todo(self, todo_obj):
        self.todo_id += 1
        self.container.append(Todo(todo_obj, self.todo_id))

    def find_id(self, id, container):
        """get the note based on a certain provided ID"""
        for note in container:
            if str(id) == str(note.todo_id):
                return note
        return None

    def search_id(self, container):
        id = input("Enter ID: ")
        result = self.find_id(id, container)
        if result == None:
            print("This is not a valid ID")
        else:
            return [result]

    def search_string(self, container):
        search_string = input("Enter search term: ")
        search_list = []
        for item in container:
            if search_string in item.todo:
                search_list.append(item)
        return search_list

    def search_status(self, container):
        search_string = input("Enter \"complete\" or \"not complete\" term: ")
        search_list = []
        for item in container:
            if str(search_string) == item.status:
                search_list.append(item)

        return search_list

    def time_complete(self, item):
        complete_time = datetime.datetime.now()
        item.complete_time = complete_time - item.time_date
        print("Time to complete: {}".format(item.complete_time))

    def save_object(self, obj):
        try:
            output = open((self.filename + ".pkl"), 'wb')
        except AttributeError:
            print("There are no to-do items to save!")
        else:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
            output.close()

    def load_object(self):
        try:
            input = open((self.filename + ".pkl"), 'rb')
        except FileNotFoundError:
            print("This user does not have any stored data!")
        else:
            print("Previous session loaded")
            obj = pickle.load(input)
            input.close()
            print("Load complete")
            return obj


class Menu:
    def __init__(self):
        self.menu_contain = Container()
        self.exit_program = True
        self.options = {"1": self.add, "2": self.alltodo, "3": self.search, "4": self.mark_complete, "5": self.quit}
        self.serach_options = {"1": self.menu_contain.search_id, "2": self.menu_contain.search_string,
                               "3": self.menu_contain.search_status}

    def add(self):
        todo_list = input("Please enter the To-do item: ")
        self.menu_contain.add_todo(todo_list)
        print("New To-do item created!")

    def show_menu(self):
        print("\n",
              """Please use the following commands:
                  1: Create a new to do
                  2: List all to do items
                  3: Search To-do's
                  4: Mark To-do as Complete
                  5: Quit program"""
              )

    def alltodo(self):
        self.display(self.menu_contain.container)

    def save(self):
        self.menu_contain.save_object(self.menu_contain)

    def load(self):
        loaded_object = self.menu_contain.load_object()
        if loaded_object != None:
            self.menu_contain = loaded_object

    def display(self, items):
        if not items:
            print("There is no to-do items!")
        else:
            for item in items:
                print("\nTo-do ID: {}\nTime stated: {}\nTo-do status: {}".format(item.todo_id, item.time_date,
                                                                                 item.status))
                if item.complete_time != "not complete":
                    print("Completed in {}".format(item.complete_time))
                print("--{}".format(item.todo))

    def search_menu(self):
        print(("""Would you like to: 
            1: Search ID
            2: Search key word
            3: Search complete and not complete status"""))

    def mark_complete(self):
        change_todo = self.menu_contain.search_id(self.menu_contain.container)
        try:
            item_to_change = change_todo[0]
        except TypeError:
            pass
        else:
            if item_to_change.status == "complete":
                pass
            else:
                item_to_change.status = "complete"
                self.menu_contain.time_complete(item_to_change)

    def search(self):
        self.search_menu()
        search_req = input("Search type: ")
        search_option = self.serach_options.get(search_req)
        if search_option:
            search_results = search_option(self.menu_contain.container)
            self.display(search_results)
        else:
            print("This is not a valid option, quiting search")

    def run(self, file):
        print("-" * 40, "\n", " " * 15, "Welcome!", "\n", "-" * 40, )
        self.menu_contain.filename = file
        self.load()
        self.show_menu()
        while self.exit_program:
            option = input("\nMain Menu, Enter command: ")
            action = self.options.get(option)
            if action:
                action()
            else:
                print("Please enter a valid option")

    def quit(self):
        print("-" * 40, "\n", "Thank you for using the To-do program!", "\n", "-" * 40, )
        self.save()
        self.exit_program = False


if __name__ == "__main__":
    m = Menu()
    m.run()

