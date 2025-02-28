class Todo_List:
    def __init__(self,owner:str, todo_list:list = []):

        for item in todo_list:
            if not isinstance(item, Todo_Item):
                raise Exception(f"Expected Todo Item got {type(item)}")

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

        pending_tasks_str = ', '.join(f'{k} - {v}' for k, v in pending_tasks.items())

        return f'Pending Tasks :\n{pending_tasks_str}\nFinished Tasks : {finished_tasks}'

# Example usage:
a = Todo_Item("Wash my dishes", "Low")
b = Todo_Item("connect ethernet cable", "Medium")
c = Todo_Item("Do laundry", "High", done=True)
d = Todo_Item("Clean room", "Low")
e = Todo_Item("Buy groceries", "Medium")
f = Todo_Item("Do homework", "High")
g = Todo_Item("Watch TV", "Low", done=True)
h = Todo_Item("Play games", "Medium", done=True)
i = Todo_Item("Read book", "High", done=True)

todo_list = Todo_List("John", [a, b, c, d, e, f, g, h, i])
print(todo_list)