from jira import JIRA
from jira.client import JIRA

# jira login
jira_user = " "  # Jira username
jira_pswd = " "  # jira password
options = {'server': ''}  # jira server url

try:
    jira = JIRA(options=options, basic_auth=(jira_user, jira_pswd))
except JIRAError as e:
    if e.status_code == 401:
        print ("Login to JIRA failed.")

print("Login!!")
