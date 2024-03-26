import argparse
from .reviewer import Reviewer

def main():
    parser = argparse.ArgumentParser(description='Review a GitHub pull request.')
    parser.add_argument('openai_key', help='Your OpenAI API key')
    parser.add_argument('assistant_id', help='Your OpenAI Assistant ID')
    parser.add_argument('gh_api_key', help='Your GitHub API key')
    parser.add_argument('pull_request_url', help='The URL of the pull request to review')

    args = parser.parse_args()

    reviewer = Reviewer(args.openai_key, args.assistant_id, args.gh_api_key, args.pull_request_url)

if __name__ == '__main__':
    main()
