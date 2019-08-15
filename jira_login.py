from jira import JIRA
from jira.exceptions import JIRAError

# jira login


class JiraLogin:
    def __init__(self, server, user, pas):
        self.server = server
        self.user = user
        self.pas = pas

    def login(self):

        jira_user = self.user  # Jira username
        jira_pswd = self.pas  # jira password
        options = {'server': self.server}  # jira server url

        try:
            jira = JIRA(options=options, basic_auth=(jira_user, jira_pswd))

        except JIRAError as e:
            if e.status_code == 401:
                print ("Login to JIRA failed.")

        print("Login!!")

        return


# jira_login = JiraLogin("server", "username", "password")

# jira_login.login()
