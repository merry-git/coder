# DURI 2023 / 2024
# Multiple Agent Testing using Local Fined Tuned Models

Before, agents were limited to one model, ex. `chatGPT`. This is not the most effective way because `chatGPT` may not specialize in coding, creative writing, or *specific* actions in general. In the DURI Project, each person in the hospital simulation will need to have access to different data (Doctors / Nurses / Patients), thus, we could use multiple fined tuned models to accomplish this task (doctor model, nurse model, overlaps where necessary, ect.)

To showcase this, I created a simulation on my local computer using models that I downloaded, being Mistral 7B and CodeLlama, two open source and very capable models for testing. In this, I am simulating Professor and Student (Professor knows how to code, student asks questions), similar to a Doctor and a Nurse (Doctor knows medical decisions and nurse knows patient info, ect.)

`Mistral 7B`- ask questions, create responses in human like style (cannot code)

`codeLlama`- generate code, run code, confirm if output is correct (not as good with human language)

# Conversations

To see results, navigate to the `conversations` folder where I ask this agent chain multiple coding questions. I will attach the source code above along with setup instructions below. In the conversation, I instructed the back-and-forth to stop once the task is complete (it will send the word TERMINATE, stopping the code.) If the conversation goes into an infinite loop of back-and-forth, the maximum iterations parameter will stop after 10 iterations.

`conversations` ^ above

## Setup


