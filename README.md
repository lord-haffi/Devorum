# Devorum
### A customizable forum software API using Django

This project is a tag- and type-based forum software using Django. This means, there will be no "real" subforums. You can create kind of subforums in the Frontend with the filtering functionality. This means that subforums are more like stored procedures to filter threads. The big difference: A thread is not binded to a specific subforum and can appear in several subforums depending on the filtering options.

Here is an example of how you could achieve this in your Django-forum:

```python
print("Later here should be an example code")
```

Additionally, forum threads can be of different types. Depending on these types threads may differ in structure and appearance in Frontend. E.g. `Question` and `Discussion` are types included in this API. However, the API contains a simple way to create your own thread types for your personal forum:

```python
print("Later here should be an example code")
```

The access to forum threads can be modified by the creator by defining a white- or a black-list of Usernames and / or Userroles. (If a user-role is on a white-list all user-roles with higher position in the hierarchy (if existent) will have access too. Respectively if a user-role is on a black-list all user-roles with lower position in the hierarchy (if existent) will not have access.)
