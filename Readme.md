# Condor: Automated PR Review Tool

## Description

Condor is an automated Pull Request (PR) review tool designed to provide personalized feedback for Computer Science courses. It leverages the power of generative AI to offer insightful and constructive feedback on PRs, helping students improve their coding skills effectively.

## Features

- **Personalized Feedback**: Condor provides personalized and timely feedback on your code, directly in your PRs.
- **AI-Powered Review Process**: Condor uses generative AI to offer constructive criticism and suggestions for improvement.
- **Adaptive Learning Experience**: Condor adapts to individual needs, helping students grow as programmers.
- **CI/CD Integration (Coming Soon)**: Condor will soon support integration with Continuous Integration/Continuous Deployment (CI/CD) systems, allowing automated reviews to be triggered by events such as PR creation or code push.
- **Docker Support (Coming Soon)**: We are working on a Docker runner for Condor, which will make it even easier to deploy and run in any environment.

## How to Use

Condor is implemented as a Python class `Reviewer` in the `code-reviewer/reviewer.py` file. To use it, you need to initialize an instance of the `Reviewer` class with the necessary API keys and the URL of the PR you want to review.

Here is a basic example:

```py
    from code-reviewer.reviewer import Reviewer

    openai_api_key = "your_openai_api_key"
    assistant_id = "your_assistant_id"
    gh_api_key = "your_github_api_key"
    pull_request_url = "url_of_the_pull_request"

    reviewer = Reviewer(openai_api_key, assistant_id, gh_api_key, pull_request_url)
```

This will automatically start the review process for the specified PR. The review process includes adding PR description, adding commit messages, reviewing files, and providing a summary review.

Please note that you need to replace `"your_openai_api_key"`, `"your_assistant_id"`, `"your_github_api_key"`, and `"url_of_the_pull_request"` with your actual OpenAI API key, OpenAI Assistant ID, GitHub API key, and the URL of the PR you want to review, respectively.

## Requirements

- Python 3.6 or higher
- OpenAI Python client
- PyGithub

You can install the required Python packages using pip:
`pip install openai PyGithub`
