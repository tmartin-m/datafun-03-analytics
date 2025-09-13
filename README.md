# datafun-03-analytics

# Machine Setup
https://github.com/denisecase/pro-analytics-01/blob/main/01-machine-setup/MACHINE-SETUP.md

# Project Initialization
- Either Copy an existing project of create a new on from scratch (choose 1)
  - https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/01a-copy-existing-repo-in-github.md
  - https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/01b-create-repo-in-github.md
- ALWAYS Use Git to clone the new repository to your local machine
- If starting from scratch only : Add key files such as .gitignore and requirements.txt
  - https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/03-add-gitignore-and-requirements.md
  - Create a new file in your root repo folder named exactly: .gitignore IMPORTANT: Spelling, capitalization, and name are critical. If the name or location is not exact, it will not work. Find the .gitignore file in the root of this pro-analytics-01 repo and paste the entire contents into your .gitignore file. This is a good starting point for many Python projects. Actual .gitignore contents will vary by project.
  - Create a new file in your root project folder named exactly: requirements.txt. IMPORTANT: Spelling, capitalization, and name are critical. If the name or location is not exact, the commands we provide will not work. Find the requirements.txt file in the root of this pro-analytics-01 repo and paste the entire contents into your requirements.txtfile. This is a good starting point for many Python projects. Actual requirements.txt contents will vary by project.
- If starting from scratch only: Use Git to add, commit, and push your new files to GitHub:
  - https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/04-git-add-commit-push.md
  - git add .
  - git commit -m "Add .gitignore and requirements.txt files"
  - git push -u origin main
- ALWAYS create a python virtual environment for your project:
  - https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/05-create-virtual-environment.md
  - py -m venv .venv

# Repeatable Project Workflow
- Pull Changes
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/01-git-pull-before-changes.md
  - git pull origin main
- Activate Virtual Environment
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/02-activate-virtual-environment.md
  - .venv\Scripts\activate
    - https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.5
      - cmd.exe
      - pwsh.exe -ExecutionPolicy AllSigned
- Install Dependencies
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/03-install-dependencies.md
  - .\.venv\Scripts\activate
  - py -m pip install --upgrade pip setuptools wheel
  - py -m pip install -r requirements.txt
- Run Scripts and/or Jupyter notebooks
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/04a-activate-and-run-python-script.md
    - Ctrl+Shift+P
    - Python: Select Interpreter
    - Choose an Interpreter - Look for the recommended local .venv option.
    - Activate and Execute
      - .\.venv\Scripts\activate
      - py myfile.py
    - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/04b-activate-and-run-jupyter-notebook.md
      - NOT COMPLETEING YET
- Modify Code and test
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/05-modify-and-test.md
- Save
  - https://github.com/denisecase/pro-analytics-01/blob/main/03-repeatable-workflow/06-git-add-commit-push.md
  - git add .
  - git commit -m "Add .gitignore and requirements.txt files"
  - git push -u origin main

# To Dos
https://www.stepsize.com/blog/best-vs-code-extensions-to-handle-todos

# Example Repo
https://github.com/denisecase/datafun-03-analytics

# Trouble Shooting
If you see the error No module named `requests`:

The requests module is an external module (that is not part of the Python Standard Library) and you must install it into your active local project virtual environment. Use the commands provided to create your project virtual environment in the .venv folder and activate it. Then use the commands provided to install the requests module into your .venv. 

Once installed into .venv, you can import an external module like requests in your Python files:

import requests 


