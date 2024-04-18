import re
from .lib.github_pr import GithubPR 
from .lib.openai_assistant import OpenAIAssistant

class Reviewer:
    def __init__(self, openai_api_key, assistant_id, gh_api_key, pull_request_url):
        self.gh = GithubPR(gh_api_key, pull_request_url)
        self.assistant = OpenAIAssistant(openai_api_key, assistant_id)

        self.steps = [
            self.add_step(self.add_pr_description),
            self.add_step(self.add_commit_messages, "Review the commit messages. Provide feedback on how the PR is structured"),
            self.add_step(self.review_files, "You are gonna receive each file diff"),
            self.add_step(self.summary_review, "All files reviewed. Give a general overview of the quality of the PR from 0 to 10")
        ]

        self.__run_steps()

    def __run_steps(self):
        for step in self.steps:
            step()

    def add_pr_description(self):
        message = f"Pull Request Description: {self.gh.pr.title}\n\n{self.gh.pr.body}"
        message += f"\n\nPR Author: @{self.gh.pr.user.login}"

        self.assistant.add_message(message, "user")

    def add_commit_messages(self):
        messages = "\n".join(self.gh.get_commit_messages())
        self.assistant.add_and_retrieve_message(messages, "user")

    def review_files(self):
        for filename in self.gh.get_modified_files():
            diff = self.gh.get_file_diff(filename)
            message = f"Reviewing file: {filename}.\nDiff:\n\n{diff}"

            response = self.assistant.add_and_retrieve_message(message, "user")

            first_change_line = self._get_first_change_line(diff)
            if response and response != 'APIError: No response':
                self.gh.comment_on_file(filename, response, first_change_line)

    def _get_first_change_line(self, diff):
        match = re.search(r'@@ -\d+,\d+ \+(\d+),', diff)
        if match:
            return int(match.group(1))
        else:
            return 1

    def summary_review(self):
        summary = self.assistant.add_and_retrieve_message("Summary Review", "user")
        self.gh.comment_on_pr(summary)

    def add_step(self, func, system_message=None):
        def wrapper(*args, **kwargs):
            print(f"Running step: {func.__name__}")
            if system_message:
                self.assistant.add_message(system_message, "user")

            func(*args, **kwargs)

        return wrapper
