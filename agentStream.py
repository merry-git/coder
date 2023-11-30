import autogen

config_list_mistral = [
    {
        'base_url': "YOUR LOCAL LLM IP HERE",
        'api_key': "NULL"
    }
]

config_list_codellama = [
    {
        'base_url': "YOUR LOCAL LLM IP HERE",
        'api_key': "NULL"
    }
]

llm_config_mistral={
    "config_list": config_list_mistral,
}

llm_config_codellama={
    "config_list": config_list_codellama,
}

coder = autogen.AssistantAgent(
    name="Professor",
    llm_config=llm_config_codellama
)

user_proxy = autogen.UserProxyAgent(
    name="Student",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config_mistral,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task="""

ENTER YOUR TASK HERE!!! <-

"""

user_proxy.initiate_chat(coder, message=task)
