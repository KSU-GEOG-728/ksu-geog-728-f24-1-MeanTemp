[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/lW00dzvG)
# GitHub-MeanTemp
*Exercise for GEOG 728 Programming for Geographic Analysis at Kansas State University*

### Objective

Become familiar with **GitHub Classroom** and submitting your work via an online GitHub repository.

### Task

Accept a GitHub assignment, clone the instructor repository to your GitHub account and locally as a new personal repository, edit a file in the repository, commit the changes made to your local copy of the file, and push those changes back to your GitHub account and assignment repository. Finally, seek assistance by posting an issue in GitHub.

### Required Software

The following software programs will be used in this exercise.  Each is available on the laboratory computers in S3014A.  If you plan to use your own personal computer this semester, please download and install.
1.  GitHubDesktop - https://desktop.github.com/
2.  Microsoft VS Code - https://code.visualstudio.com/download

### Procedures

**Step #1 - Create a GitHub Account**

This assignment assumes you already have a GitHub account.  If you do not, login to **GitHub** (https://github.com) and create a free personal account.  GitHub will serve as your online storage for coding work this semester.  I will be able to access your class-related code, provide feedback, answer your questions, and grade your assignments.  You will also have a permanent copy of your work that you retain and control after the semester ends.

**Step #2 - Accept an Assignment Invitation and Clone a Template Repository**

When you are assigned coding work this semester, an important link will be included in the assignment page in Canvas.  Simply click on this link and *accept* the assignment.  This automatically starts the process of cloning a template repository that contains instructions and other important files that I provide as a starting point.  The name of the cloned respository will follow the convention *template repository name - your GitHub username*. 

**Step #3 - Start GitHub Desktop**

After creating your GitHub acount, start and login to **GitHub Desktop** using your new GitHub account credentials.

**Step #4 - Create a Local Clone**

Within **GitHub**, find your newly created assignment repository, click the green Code button, and choose *Open with GitHub Desktop*.  **GitHub Desktop** gives you the option to open the locally cloned files in an editor program (e.g., Notepad++), viewing the repository files in Windows Explorer, or opening the repository page on GitHub in a Web browser.  

If this method for creating a local clone is not possible, open **GitHub Desktop** and select *File --> Clone a Repository*, then enter the URL to your repo that was created in the KSU-GEOG-728 organization upon acceptance of the assignment.

**Step #5 - View Files in Windows Explorer**

In **GitHub Desktop**, choose the option to view the files of your repository in Windows Explorer.

**Step #6 - Edit a File in Microsoft Visual Studio Code**

Find the file <code>mean_temp.py</code>, open it in **Microsoft VS Code**, and enter the code requested in the comments.  Run the code in the IDE to make sure it works and calculates a correct final value.  The trick here is to specify the correct Python interpreter within VS Code.  For most students using a lab computer, the correct path for the interpreter will be <code>c:\Program Files\ArcGIS\Pro\Bin\Python\envs\arcgispro-py3\python.exe</code>.  Enter "Ctrl+Shift+P" to open the window in VS Code needed to specify the interpreter.

**Step #7 - Describe and Commit Changes to Master**

After saving your edits to <code>mean_temp.py</code>, return to **GitHub Desktop** and you should see a snippet of the file that highlights the revisions you just made.  Characterize your edits with a summary and short description (bottom left corner of **GitHub Desktop**), then choose Commit to Main.  This workflow allows you to maintain a record of changes made - essentially multiple versions of the same file - without having to have multiple copies of your file (e.g., mean_temp1.py, mean_temp2.py, etc.).  This is version control!

**Step #8 - Push Changes to Origin Repository on GitHub**

After you have made all of the changes you want, you now have to sync these changes - which apply only to the local version of the repository - to your original repo on **GitHub**. Once you have committed changes to master, you will have the option to push the commits to the origin remote.  Click the blue *Push Origin* button.

**Step #9 - Verify Changes in GitHub**

In **GitHub Desktop**, choose the option to open your repository page on **GitHub** in your Web browser.  Alternatively, you can simply open a Web browser and navigate to https://github.com.  Find the updated <code>mean_temp.py</code> file and open it to confirm that your local changes are now reflected in your online repository.

**Step #10 - Raise an Issue**

You can ask questions of me directly in **GitHub** by raising an *issue*.  In your repo on **GitHub**, find and click *Issue* in the menu at the top of the page.  Next, click on the green *New Issue* button.  This opens a chat-style window that allows you to pose questions and for me to provide a response.  This feature also helps us maintain a permanent record of our online conversation.  Use this issue that you have generated to ask me a question.

### Submission

After completing the requested edits to <code>mean_temp.py</code> make sure that you have (1) committed the changes to the main branch and provided a short summary and description of your changes and (2) pushed those changes from your local repository to the origin repository on **GitHub**.  Double check your work by reviewing your repository on GitHub and make sure that you have also raised an *issue* to ask me a question.  Once you have pushed any revisions to your online assignment repository, both you and I can see the repository.  I'll take advantage of this to review your work and provide feedback.
