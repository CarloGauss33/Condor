import json
from lib.github_pr import GithubPR 
from lib.openai_assistant import OpenAIAssistant 

class Reviewer:
    def __init__(self, openai_api_key, assistant_id, gh_api_key, pull_request_url):
        self.gh = GithubPR(gh_api_key, pull_request_url)
        self.assistant = OpenAIAssistant(openai_api_key, assistant_id)

    def add_pr_description(self):
        message = f"Pull Request Description: {self.gh.pr.title}\n\n{self.gh.pr.body}"
        self.assistant.add_message(message, "user")

    def review_files(self):
        for filename in self.gh.get_modified_files():
            diff = self.gh.get_file_diff(filename)
            message = f"Reviewing file: {filename}.\nDiff:\n\n{diff}"

            response = self.assistant.add_and_retrieve_message(message, "user")
            if response and response != 'APIError: No response':
                self.gh.comment_on_file(filename, response, 1)

    def summary_review(self):
        summary = self.assistant.add_and_retrieve_message("Summary Review", "user")
        self.gh.comment_on_pr(summary)
