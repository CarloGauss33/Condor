# lib/code_extract.py

import re
import fnmatch
from github import Github, Auth
import functools

MAX_SUPPORTED_CHANGES = 1500

REVIEWABLE_FILES = [
    '*.md', '*.py', '*.html',
    '*.rb', '*.c', '*.cpp',
    '*.h', '*.go', '*.js',
    '*.ts', '*.css', '*.scss',
    '*.tsx', '*.jsx', '*.java',
]

class GithubPR:
    def __init__(self, _api_key, pull_request_url):
        self.pull_request_url = pull_request_url
        self._set_repository_name_and_pr_number()

        _auth = Auth.Token(_api_key)
        self.github = Github(auth=_auth)
        self.pr = self.get_pr()

    @functools.lru_cache(maxsize=None)
    def get_repo(self):
        return self.github.get_repo(self.repository_name)

    @functools.lru_cache(maxsize=None)
    def get_pr(self):
        return self.get_repo().get_pull(self.pull_request_number)
    
    @functools.lru_cache(maxsize=None)
    def get_files(self):
        return list(self.pr.get_files())
    
    def get_file(self, filename):
        matching_file = next((file for file in self.get_files() if file.filename == filename), None)
        return matching_file
    
    @functools.lru_cache(maxsize=None)
    def get_modified_files(self):
        files = {}
        for file in self.get_files():
            if self.__should_review_file(file):
                files[file.filename] = file

        return files

    @functools.lru_cache(maxsize=None)
    def get_commits(self):
        return self.pr.get_commits()
    
    @functools.lru_cache(maxsize=None)
    def get_commit_messages(self):
        return [commit.commit.message for commit in self.get_commits()]
    
    @functools.lru_cache(maxsize=None)
    def get_last_commit(self):
        return self.get_commits().reversed[0]

    def get_original_file_content(self, filename):
        file = self.get_file(filename)
        if (not file) or (file.status == 'added'):
            return ''
        
        return self.get_repo().get_contents(filename, ref=self.pr.base.sha).decoded_content.decode()
    
    def get_file_diff(self, filename):
        return self.get_modified_files()[filename].patch
    
    def get_pr_diff(self):
        return self.get_last_commit().files
    
    def get_languages_of_repo(self):
        return self.get_repo().get_languages()
    
    def get_total_pr_size(self):
        return self.pr.additions + self.pr.deletions
    
    def comment_on_file(self, filename, comment, line=1):
        self.pr.create_review_comment(
            comment,
            self.get_last_commit(),
            filename,
            line
        )

    def comment_on_pr(self, comment):
        self.pr.create_issue_comment(comment)
    
    def _set_repository_name_and_pr_number(self):
        owner, repo, number = self.__match_pull_request_url()

        self.repository_name = f"{owner}/{repo}"
        self.pull_request_number = number
        
    def __match_pull_request_url(self):
        stripped_url = self.pull_request_url.lstrip('https://')

        match = re.match(self.__pull_request_regex(), stripped_url)
        if not match:
            raise ValueError("Invalid pull request URL")
        
        return match.group('owner'), match.group('repo'), int(match.group('number'))
    
    def __should_review_file(self, file):
        filename = file.filename
        is_reviewable = any([fnmatch.fnmatch(filename, pattern) for pattern in REVIEWABLE_FILES])
        is_less_than_limit = file.changes < MAX_SUPPORTED_CHANGES

        return is_reviewable and is_less_than_limit

    @staticmethod
    def __pull_request_regex():
        return r"github.com/(?P<owner>[\w\-]+)/(?P<repo>[\w\-]+)/pull/(?P<number>\d+)"
