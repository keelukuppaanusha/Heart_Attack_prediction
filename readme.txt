steps to follow to  create virtual environment in visual studio:
>>Go to Powershell command prompt
	1.(winows+R)-->enter --->Powershell
>>copy pastethis below command
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
>>Go to visual studio ,Add an folder to workspace.
	>>Go to terminal in tool.
>>Command to create virtual environment(one timein a folder)
	>>python -m venv .venv
>>To activate(activate every time for terminal open)
	>>.\.venv\Scripts\Activate.ps1

>>TO install libraries all at a time
  >>pip install -r <file_name>requiremnts.txt
>>Make sure that what libraries are necessary for a project all are put in that text file.