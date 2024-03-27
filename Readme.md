# Condor: Automated PR Review Tool

## Description

Condor is an automated Pull Request (PR) review tool designed to provide personalized feedback for Computer Science courses. It leverages the power of generative AI to offer insightful and constructive feedback on PRs, helping students improve their coding skills effectively.

## Features

- **Personalized Feedback**: Condor provides personalized and timely feedback on your code, directly in your PRs.
- **AI-Powered Review Process**: Condor uses generative AI to offer constructive criticism and suggestions for improvement.
- **Adaptive Learning Experience**: Condor adapts to individual needs, helping students grow as programmers.
- **CI/CD Integration (Coming Soon)**: Condor will soon support integration with Continuous Integration/Continuous Deployment (CI/CD) systems, allowing automated reviews to be triggered by events such as PR creation or code push.
- **Docker Support (Coming Soon)**: We are working on a Docker runner for Condor, which will make it even easier to deploy and run in any environment.

## Running Condor Locally

To run Condor locally, you need to install the required Python packages and set up the necessary environment variables. Here are the steps:

1. Install the module
`pip install -e code-reviewer`

2. Run!
`condor OPENAI_KEY ASSISTANT_ID GH_API_KEY PR_URL`

## Running Condor with Docker

Condor is also available as a Docker image on DockerHub. You can pull and run the Docker image with the following commands:

```sh
docker pull carlogauss33/condor
docker run -e OPENAI_KEY=your_openai_api_key -e ASSISTANT_ID=your_assistant_id -e GH_API_KEY=your_github_api_key -e PR_URL=url_of_the_pull_request carlogauss33/condor
```

Again, please replace `your_openai_api_key`, `your_assistant_id`, `your_github_api_key`, and `url_of_the_pull_request` with your actual OpenAI API key, OpenAI Assistant ID, GitHub API key, and the URL of the PR you want to review, respectively.

## Running Condor as a GitHub Action

Condor can also be run as a GitHub Action. This allows it to automatically review pull requests when they are created.

To set up the Condor GitHub Action in any repository, follow these steps:

1. Create a new file in your repository at the following path: `.github/workflows/condor_review.yml`

2. Copy the content from the [condor_review.yml](https://github.com/CarloGauss33/Condor/blob/main/integrations/github-actions/condor_review.yml) into your new file. The content should look like this:

```yml
name: Condor Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install condor_code_reviewer

    - name: Run Condor
      run: condor --openai-key ${{ secrets.OPENAI_KEY }} --gh-api-key ${{ secrets.GH_API_KEY }}  --assistant-id ${{ secrets.ASSISTANT_ID }} --pull-request-url ${{ github.event.pull_request.html_url }}
```

3. You need to set up the following secrets in your GitHub repository: `OPENAI_KEY`, `GH_API_KEY`, and `ASSISTANT_ID`. These secrets should contain your OpenAI API key, GitHub API key, and OpenAI Assistant ID, respectively. To set up secrets, go to your repository's settings, then click on "Secrets", and then "New repository secret".

4. Once you've set up the secrets and added the workflow file, the GitHub Action will automatically run whenever a pull request is created in your repository.

Please note that this GitHub Action is designed to work with the Condor automated PR review tool. If you haven't already, you'll need to set up Condor as described in the [Condor README](https://github.com/CarloGauss33/condor/blob/main/README.md).

## Development

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
