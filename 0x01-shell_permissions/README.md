Each scripts function:
0-iam_betty - switches user from the current user to betty
1-who_am_i - prints the effective username of the current user
2-groups - prints all the groups the current user is part of
3-new_owner - changes the owner of file hello to betty
4-empty - creates an empty file called hello
5-execute - add execute permission for owner of file hello
6-multiple_permissions - adds execute permission to owner and group and read permission to other users
7-everybody - adds execute permission to owner, group and other users for file hello
8-James_Bond - sets only other users to have all permissions
9-John_Doe - sets the mode of file hello to -rwxr-x-wx
10-mirror_permissions - sets the mode of file hello same as file olleh
11-directories_permissions - adds execute permission to all subdirectories of the current working directory
12-directory_permissions - creates directory my_dir with permissions 751
13-change_group - changes the group of file hello to school
100-change_owner_and_group - changes the owner of each file and directory to vincent and the group to staff
101-symbolic_link_permissions - changes the owner of symbolic link _hello to vincent and group to staff
102-if_only - changes the user of hello to betty only if hello is owned by guillaume
