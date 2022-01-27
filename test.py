from Client import Client


testclient = Client("http://127.0.0.1:8080")
# response = testclient.register(name = "test", email = "testtest@test.te", password = "123453")
print(testclient.login_check(username = "testtest@test.te", password = "123453"))
# print(testclient.create_task(text = "asdasd"))
# print(testclient.create_task(text = "asdasd"))
print(testclient.get_all_tasks().text)
print(testclient.edit_task(text = "hhhhhh", num = 1))
print(testclient.delete_task(num = 2))
print(testclient.get_all_tasks().text)