
class Todo_Item:
    priority_options = ["High", "Medium", "Low"]

    def __init__(self,task:str,priority:str = None,done:bool = False):
        if type(task) == str:
            if task:
                self.task = task
            else:
                raise Exception("Task should not be empty") 
        else:
            raise Exception("Task needs to be a string")

        if type(done) == bool:
            self.done = done
        else:
            raise Exception("Done argument needs to be a boolean")

        if priority:
            if priority in self.priority_options:
                self.priority = priority
            else:
                raise Exception(f"priority setting should be one of {self.priority_options}")
        else:
            self.priority = None

    def __str__(self):
        return f'[{"x" if self.done else "o"}] - {self.priority if self.priority else ""} : {self.task}'

    def finish(self):
        self.done = True

    def raise_priority(self):
        if not self.priority:
            return

        if self.priority == "Low":
            self.priority = "Medium"
        if self.priority == "Medium":
            self.priority = "High"


class Todo_List:
    def __init__(self, owner: str, todo_list: list = []):

        for item in todo_list:
            if not isinstance(item, Todo_Item):
                raise Exception(f"Expected Todo Item got {type(item)}")

        self.owner = owner
        self.todo_items = todo_list

    def __str__(self):
        pending_tasks = {}
        finished_tasks = 0

        for item in self.todo_items:
            if item.done:
                finished_tasks += 1
            else:
                if item.priority in pending_tasks:
                    pending_tasks[item.priority] += 1
                else:
                    pending_tasks[item.priority] = 1

        pending_tasks_str = ','.join(f'{k} - {v}' for k, v in pending_tasks.items())

        return f'{self.owner}\'s Todo List:\nPending Tasks :\n{pending_tasks_str}\nFinished Tasks : {finished_tasks}'



a = Todo_Item("Wash my dishes", "Low")
b = Todo_Item("connect ethernet cable", "Medium")
c = Todo_Item("Start study", "High", done=True)
d = Todo_Item("Clean room", "Low")
e = Todo_Item("Buy groceries", "Medium")
f = Todo_Item("Do homework", "High")
g = Todo_Item("Watch TV", "Low", done=True)
h = Todo_Item("Play games", "Medium", done=True)
i = Todo_Item("Read book", "High", done=True)
j = Todo_Item("Play Guitar", "High", done=True)

todo_list = Todo_List("John", [a, b, c, d, e, f, g, h, i,j])
print(todo_list)