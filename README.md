CliMenuHelper.
==============

CliMenuHelper is a tool to help in the creation of cli menus.

Example:
```python
from CliMenuHelper import CliMenuHelper
cmh = CliMenuHelper(title="Please select an option", options=["Go to space", "Go to a new dimension"])
cmh.start()
Out:
##############################
# Please select an option    #
##############################
# 1. Go to space             #
# 2. Go to a new dimension   #
# Press q to exit.           #
##############################
Select the option:
```
Possible outputs:

 - If you select a listed option, CliMenuHelper will return the option that you selected.
 - If you do not select a listed option, the menu will reload.
 - If you select the option to exit, CliMenuHelper will return None
