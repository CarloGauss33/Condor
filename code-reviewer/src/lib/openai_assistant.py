import functools
import time
from openai import OpenAI

class OpenAIAssistant:
    def __init__(self, api_key, assistant_id, thread_id=None):
        self.assistant_id = assistant_id
        self.client = OpenAI(api_key=api_key)

        self.thread_id = thread_id if thread_id else self.__create_thread()

    @functools.lru_cache(maxsize=None)
    def __create_thread(self):
        response = self.client.beta.threads.create()
        return response.id
    
    def add_message(self, message, role):
        self.client.beta.threads.messages.create(
            thread_id=self.thread_id,
            role=role,
            content=message
        )

    def get_messages(self):
        return self.client.beta.threads.messages.list(thread_id=self.thread_id)
    
    def get_last_message(self):
        return self.get_messages().data[0]
    
    def create_run(self):
        response = self.client.beta.threads.runs.create(
            thread_id=self.thread_id,
            assistant_id=self.assistant_id,
        )

        return response

    def wait_on_run(self, run):
        while run.status == "queued" or run.status == "in_progress":
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread_id,
                run_id=run.id,
            )
            time.sleep(0.5)
        return run
    
    def add_and_retrieve_message(self, message, role):
        self.add_message(message, role)

        run = self.create_run()
        self.wait_on_run(run)
        
        msg = self.get_last_message()
        try:
            return msg.content[0].text.value
        except AttributeError:
            return 'APIError: No response'
    
